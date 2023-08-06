'''
Provides common commands to manipulate domains

Author: 2022 A. Karmanov
'''

import abc
import datetime
import fnmatch

from typing import List
from typing import Set
from typing import Tuple

import libvirt
import rich

from rich.prompt import Prompt
from virtbulk.formatter import ActionStatus
from virtbulk.formatter import FormatterBase
from virtbulk.formatter import FormatterPlainText
from virtbulk.utils import DomainState
from virtbulk.utils import LibvirtConnection


class CommandBase(abc.ABC):
    ''' Base class for commands hierarhy '''
    def __init__(
            self,
            uri: str,
            targets: List[str],
            formatter: FormatterBase = FormatterPlainText(),
            ignore_case=False):
        self._uri = uri
        self._targets = targets
        self._formatter = formatter
        self._ignore_case = ignore_case

    def _normalize(self, string: str) -> str:
        if self._ignore_case:
            return string.lower()
        return string

    def _match(self, name: str) -> bool:
        for tgt in self._targets:
            if fnmatch.fnmatchcase(self._normalize(name), self._normalize(tgt)):
                return True
        return False

    def list(self) -> List[libvirt.virDomain]:
        """ Get list of matched libvirt domains
        """
        result = []
        with LibvirtConnection(self._uri) as virt:
            domains = virt.listAllDomains()
            for dom in domains:
                if self._match(dom.name()):
                    result.append(dom)
        return result

    @abc.abstractmethod
    def commit(self, dry_run: bool = False) -> None:
        ''' Execute command respecting falgs'''

    @property
    @classmethod
    @abc.abstractmethod
    def name(cls) -> str:
        ''' Name of the command will be used in command line interface '''


class CommandList(CommandBase):
    ''' Only list matched domains '''
    name = 'list'

    def commit(self, dry_run: bool = False) -> None:
        for dom in self.list():
            self._formatter.add_line(dom.name(), 'list', ActionStatus.NOOP)


class CommandState(CommandBase):
    ''' List matched domains with current statuses '''
    name = 'state'

    def commit(self, dry_run: bool = False) -> None:
        for dom in self.list():
            self._formatter.add_line(
                dom.name(),
                action=DomainState.make(dom.state()).name,
                status=ActionStatus.NOOP)


class StateCommandBase(CommandBase):
    ''' Base class for commands which changes state of domains '''
    @property
    @classmethod
    @abc.abstractmethod
    def _good_initial_states(cls) -> Set[DomainState]:
        ...

    @property
    @classmethod
    @abc.abstractmethod
    def _target_states(cls) -> Set[DomainState]:
        ...

    @property
    @classmethod
    @abc.abstractmethod
    def _method(cls) -> str:
        ...

    def _change_state(self, dom: libvirt.virDomain, dry_run: bool) -> Tuple[str, ActionStatus]:
        status = ActionStatus.NOOP
        initial_state = DomainState.make(dom.state())

        if initial_state in self._target_states:
            return f'{initial_state.name}', status
        if initial_state not in self._good_initial_states:
            return (
                f'{initial_state.name} -X',
                ActionStatus.ERROR)
        if dry_run:
            return (
                f'{initial_state.name} -> ...',
                ActionStatus.DRY_RUN)

        try:
            getattr(dom, self._method)()
        except libvirt.libvirtError as error:
            # TODO Logging
            return (
                f'{initial_state.name} -!',
                ActionStatus.ERROR)

        status = ActionStatus.CHANGED
        new_state = DomainState.make(dom.state())
        if new_state == initial_state:
            new_state_str = '...'
        else:
            new_state_str = new_state.name

        return f'{initial_state.name} -> {new_state_str}', status

    def commit(self, dry_run: bool = False) -> None:
        for dom in self.list():
            change_str, status = self._change_state(dom, dry_run)

            self._formatter.add_line(dom.name(), change_str, status)


class CommandStart(StateCommandBase):
    ''' Powers on domains, make they RUNNING '''
    name = 'start'

    _method = 'create'

    _good_initial_states = {
        DomainState.SHUTOFF,
    }

    _target_states = {
        DomainState.RUNNING,
        DomainState.PAUSED,
        DomainState.PMSUSPENDED
    }


class CommandForceShutdown(StateCommandBase):
    ''' Instantly shutdown domains, usafe for data '''
    name = 'force-shutdown'

    _method = 'destroy'

    _good_initial_states = {
        DomainState.RUNNING,
        DomainState.PAUSED,
        DomainState.PMSUSPENDED
    }

    _target_states = {
        DomainState.SHUTOFF,
        DomainState.SHUTDOWN,
    }


class CommandShutdown(StateCommandBase):
    ''' Send command to shutdown a.k.a soft poweroff

    Command sends signals to domains and exit, so their statuses change with
    delay.
    '''
    name = 'shutdown'

    _method = 'shutdown'

    _good_initial_states = {
        DomainState.RUNNING,
        DomainState.PAUSED,
        DomainState.PMSUSPENDED
    }

    _target_states = {
        DomainState.SHUTOFF,
        DomainState.SHUTDOWN,
    }


class CommandPause(StateCommandBase):
    ''' Pause domain

    In such suspended state a domain spare IO resouces and may be instantly
    unsuspended.
    '''
    name = 'pause'

    _method = 'suspend'

    _good_initial_states = {
        DomainState.RUNNING,
        DomainState.PMSUSPENDED
    }

    _target_states = {
        DomainState.PAUSED,
    }


class CommandResume(StateCommandBase):
    ''' Ususpend paused domain '''
    name = 'resume'

    _method = 'resume'

    _good_initial_states = {
        DomainState.PAUSED,
    }

    _target_states = {
        DomainState.RUNNING,
        DomainState.PMSUSPENDED
    }


class CommandDelete(CommandBase):
    ''' Totally delete domains, destructive operation '''
    name = 'delete'

    _undefine_flags = (
        libvirt.VIR_DOMAIN_UNDEFINE_CHECKPOINTS_METADATA |
        libvirt.VIR_DOMAIN_UNDEFINE_MANAGED_SAVE |
        libvirt.VIR_DOMAIN_UNDEFINE_SNAPSHOTS_METADATA |
        libvirt.VIR_DOMAIN_UNDEFINE_NVRAM)

    def _delete_domain(self, dom: libvirt.virDomain, dry_run: bool) -> None:
        action = 'delete'
        if dry_run:
            self._formatter.add_line(
                dom.name(),
                action=action,
                status=ActionStatus.DRY_RUN)
        else:
            try:
                dom.destroy()
            except libvirt.libvirtError as error:
                if error.get_error_code() != libvirt.VIR_ERR_OPERATION_INVALID:
                    # TODO log
                    ...
            try:
                dom.undefineFlags(self._undefine_flags)
            except libvirt.libvirtError as error:
                # TODO log
                self._formatter.add_line(
                    dom.name(),
                    action='error while deleting',
                    status=ActionStatus.ERROR)
            else:
                self._formatter.add_line(
                    dom.name(),
                    action=action,
                    status=ActionStatus.CHANGED)

    # TODO Implement force
    def commit(self, dry_run: bool = False, force: bool = False) -> None:
        domains = self.list()

        if len(domains) > 0 and not force and not dry_run:
            confirmation = Prompt.ask(
                'It will delete your virtual machines, are you sure?',
                choices=['y', 'n'])
            if confirmation != 'y':
                rich.print('Only dry run then')
                dry_run = True

        for dom in domains:
            self._delete_domain(dom, dry_run)


# TODO write snapshot name
class CommandTakeSnapshot(CommandBase):
    ''' Take snaphots for domains

    Snapshotting stopped domains may significantly spares storage.

    Try refresh button in Virt manager if you see no the new snapshot.

    EFI virtual machines is not supported.
    '''
    name = 'take-snapshot'

    @property
    def _timestamp(self) -> str:
        return datetime.datetime.today().strftime('%d.%m.%Y_%H:%M:%S')


    def commit(self, dry_run: bool = False) -> None:
        for dom in self.list():
            state = DomainState.make(dom.state()).name
            name = f'{self._timestamp}-VirtBulk'
            action = f'take snapshot "{name}" on {state}'
            if dry_run:
                self._formatter.add_line(
                    dom.name(),
                    action=action,
                    status=ActionStatus.DRY_RUN)
            else:
                try:
                    dom.snapshotCreateXML(
                        f'<domainsnapshot><name>{name}</name></domainsnapshot>')
                except libvirt.libvirtError as error:
                    # TODO Log
                    self._formatter.add_line(
                        dom.name(),
                        action=f'failed to take snapshot "{name}" on {state}',
                        status=ActionStatus.ERROR)
                else:
                    self._formatter.add_line(
                        dom.name(),
                        action=action,
                        status=ActionStatus.CHANGED)
