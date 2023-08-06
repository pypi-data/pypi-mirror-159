# VirtBulk

## Description

`virtbulk` is a CLI to apply basic operations on multiple libvirt virtual
machines (so called "domains") matched with globs.

## Installation

```shell
pip3 install virtbulk
```

## Usage

```shell
virtbulk FLAGS COMMAND TARGET [TARGET ...]
```

Most useful flags:
  - `-c`, `--uri` to set alternative libvirt URI
  - `-n`, `--dry-run` to show assumed changes and exit
  - `-f`,  `--format` to change output format
  - `-h`, `--help` to show comprehensive options and commans list
  - ...

Most useful commands:
  - `state` shows current states of machines
  - `start` turns machines on
  - `shutdown` sends command to shutdown
  - ...

Some commands provides `STATE_1 -> STATE_2` output format.
  - `->` means a state change
  - `-X` means the requested change can not be commit
  - `-!` means error while applying the change

## TODO

- Unit tests
- `help` command
- man page

## Links

- [virsh](https://www.libvirt.org/manpages/virsh.html)
- [libvirt Python API](https://libvirt.org/python.html)
