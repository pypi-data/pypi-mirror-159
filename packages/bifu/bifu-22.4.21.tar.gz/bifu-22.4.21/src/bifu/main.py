#!/usr/bin/env python3
# Python3 shebang is required to work properly in Windows system - DON'T remove it !!!

import argparse
import logging

from bifu.classes.application import Application  # type: ignore
from bifu.classes.config import PackageConfiguration  # type: ignore


def parse_arguments() -> argparse.ArgumentParser:
    choices = ['pre-commit', 'pre-push']
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--init', action='store_true', required=False, help='Create config file in current directory',
    )
    parser.add_argument(
        '-i', '--install', type=str, choices=choices, action='store', required=False, help='Install selected option',
    )
    parser.add_argument(
        '-n', '--number', type=int, default=0, action='store', required=False, help='Run task number x',
    )
    parser.add_argument(
        '-r', '--run', type=str, choices=choices, action='store', required=False, help='Run selected option',
    )
    parser.add_argument(
        '-u', '--uninstall', type=str, choices=choices, action='store', required=False,
        help='Uninstall selected option',
    )
    return parser


def main() -> None:
    package = PackageConfiguration()

    logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=f'/tmp/{package}.log',
        level=logging.DEBUG,
    )

    logging.info('Started')
    Application(parse_arguments().parse_args())
    logging.info('Finished')


if __name__ == '__main__':
    main()
