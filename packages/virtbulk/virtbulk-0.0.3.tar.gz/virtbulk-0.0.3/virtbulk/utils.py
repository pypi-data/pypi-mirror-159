'''
Helper functions

Author: 2022 A. Karmanov
'''

import enum

from typing import Tuple

import libvirt


class LibvirtConnection:
    ''' Context manger for libvirt connector
    '''
    @staticmethod
    def _libvirt_callback(*_):
        ...

    libvirt.registerErrorHandler(
        f=_libvirt_callback, ctx=None)

    def __init__(self, uri="qemu:///system"):
        self._connection = libvirt.open(name=uri)

    def __enter__(self) -> libvirt.virConnect:
        return self._connection

    def __exit__(self, *exc):
        self._connection.close()


class DomainState(enum.IntEnum):
    ''' Common domain states from modern libvirt Python API
    '''

    NOSTATE = libvirt.VIR_DOMAIN_NOSTATE
    RUNNING = libvirt.VIR_DOMAIN_RUNNING
    BLOCKED = libvirt.VIR_DOMAIN_BLOCKED
    PAUSED = libvirt.VIR_DOMAIN_PAUSED
    SHUTDOWN = libvirt.VIR_DOMAIN_SHUTDOWN
    SHUTOFF = libvirt.VIR_DOMAIN_SHUTOFF
    CRASHED = libvirt.VIR_DOMAIN_CRASHED
    PMSUSPENDED = libvirt.VIR_DOMAIN_PMSUSPENDED

    @staticmethod
    def make(state: Tuple[int, int]) -> 'DomainState':
        ''' Helper instantiates object with a libvirt.virDomain.state() return
        '''
        return DomainState(state[0])
