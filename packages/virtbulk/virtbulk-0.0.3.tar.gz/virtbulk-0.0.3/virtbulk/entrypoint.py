'''
Entrypoint for CLI

Author: 2022 A. Karmanov
'''

import argparse
import inspect
import sys

from typing import Dict
from typing import List

from virtbulk import command
from virtbulk import formatter


def _get_args(commands: List[str], formats: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='VirtBulk...')
    parser.add_argument(
        '-c', '--uri',
        required=False,
        type=str,
        help='libvirt connection URI',
        default='qemu:///system')
    parser.add_argument(
        '-f', '--format',
        type=str,
        choices=formats,
        required=False,
        help='output format',
        default='grid')
    parser.add_argument(
        '-n', '--dry-run',
        required=False,
        action='store_true',
        help='do not act, only print')
    parser.add_argument(
        'command',
        type=str,
        choices=commands,
        nargs=1,
        help='operation to perform')
    parser.add_argument(
        '-i', '--ignore-case',
        required=False,
        action='store_true',
        help='case-insenetive glob matching')
    # TODO Implement
    parser.add_argument(
        '-v', '--verbose',
        required=False,
        action='store_true',
        help='print more messages')
    parser.add_argument(
        'target',
        type=str,
        metavar='TARGET',
        nargs='+',
        help='glob to march virtual domains')
    return parser.parse_args()


def run_cli() -> None:
    ''' Entrypoint for CLI '''
    command_mapping: Dict[str, type] = {}
    for _, member in inspect.getmembers(command):
        if (
                inspect.isclass(member)
                and issubclass(member, command.CommandBase)
                and not inspect.isabstract(member)):
            command_mapping[member.name] = member

    formatter_mapping: Dict[str, type] = {}
    for _, member in inspect.getmembers(formatter):
        if (
                inspect.isclass(member)
                and issubclass(member, formatter.FormatterBase)
                and not inspect.isabstract(member)):
            formatter_mapping[member.name] = member

    args = _get_args(
        commands=sorted(command_mapping.keys()),
        formats=sorted(formatter_mapping.keys()))

    if args.verbose:
        print('"--verbose" flag is not implemented yet, please be patient')

    command_str = args.command.pop()
    command_type = command_mapping.get(command_str)
    if command_type is None:
        print(f'Unknown command "{command_str}"', file=sys.stderr)
        sys.exit(1)

    formatter_str = args.format
    formatter_type = formatter_mapping.get(formatter_str)
    if formatter_type is None:
        print(f'Unknown formatter "{formatter_str}"', file=sys.stderr)
        sys.exit(1)

    command_obj = command_type(
        uri=args.uri,
        targets=args.target,
        formatter=formatter_type(),
        ignore_case=args.ignore_case,
    )
    command_obj.commit(dry_run=args.dry_run)
