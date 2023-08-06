'''
Output formatters

Author: 2022 A. Karmanov
'''

import abc

from enum import Enum

import rich

from rich.live import Live
from rich.table import Table


class ActionStatus(Enum):
    ''' States of commands to colornames mapping
    '''
    NOOP = 'bold white'
    CHANGED = 'bold green'
    ERROR = 'bold red'
    DRY_RUN = 'bold yellow'


class FormatterBase(abc.ABC):
    ''' Interface for output formatter class
    '''
    @property
    @classmethod
    @abc.abstractmethod
    def name(cls) -> str:
        ...

    @abc.abstractmethod
    def add_line(self, domain_name: str, action: str, status: ActionStatus) -> None:
        ''' Supposed to print state of command over one domain

        :param domain_name:
        :param action: descriptive designation of operation
        :param status: status of ended operation
        '''


def decorate(string: str, status: ActionStatus) -> str:
    ''' Rich format string with color of satatus
    '''
    return f'[{status.value}]{string}[/{status.value}]'


class FormatterRichGrid(FormatterBase):
    ''' Prints statuses aligned line-by-line with color
    '''
    name = 'grid'

    def __init__(self):
        self._grid = Table.grid(padding=(0, 1), pad_edge=False)
        self._live = Live(self._grid)

    def add_line(self, domain_name: str, action: str, status: ActionStatus) -> None:
        if not self._live.is_started:
            self._live.start()
        self._grid.add_row(
            f'[bold]{domain_name}[/bold]',
            f'[{status.value}]{action}[/{status.value}]')

    def __del__(self):
        self._live.stop()
        rich.print(
            '___\n',
            decorate("\u2B24", ActionStatus.NOOP), '- no changes',
            decorate("\u2B24", ActionStatus.CHANGED), '- changed',
            decorate("\u2B24", ActionStatus.ERROR), '- error',
            decorate("\u2B24", ActionStatus.DRY_RUN), '- dry run')


class FormatterPlainText(FormatterBase):
    ''' Prints statuses line-by-line as a plain text
    '''
    name = 'plain'

    def add_line(self, domain_name: str, action: str, status: ActionStatus) -> None:
        print(f'{domain_name} {action}')
