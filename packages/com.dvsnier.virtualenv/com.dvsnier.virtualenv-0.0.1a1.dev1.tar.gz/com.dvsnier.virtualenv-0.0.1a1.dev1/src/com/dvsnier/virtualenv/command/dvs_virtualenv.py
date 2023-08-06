# -*- coding:utf-8 -*-

import argparse
import json
import sys

from com.dvsnier.config.journal.compat_logging import logging
from com.dvsnier.virtualenv import DEBUGGER, VERSIONS
from com.dvsnier.virtualenv.util.dvs_logging import LOGGING


def execute(args=None):
    '''
        the execute command

        it is that reference link:

            1. https://docs.python.org/zh-cn/3/library/argparse.html
            2. https://docs.python.org/zh-cn/2/library/argparse.html
    '''
    if args is None:
        args = sys.argv[1:]
    # LOGGING.set_logging()
    parser = argparse.ArgumentParser(
        prog='dvs-virtualenv',
        description="""
    this is a dvs virtualenv execution program.
        """,
        epilog='the copyright belongs to DovSnier that reserve the right of final interpretation.\n',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-V', '--version', action='version', version=VERSIONS, help='the show version and exit.')
    parser.add_argument(
        'commands',
        action='store',
        nargs='*',
        default=None,
        type=str,
        metavar='commands',
        # dest='commands',
        help='the commands property.')
    # parser.add_argument('-dvs-api',
    #                     '--dvs-api',
    #                     action='store',
    #                     nargs='?',
    #                     default=None,
    #                     type=str,
    #                     metavar='dvs-api',
    #                     dest='dvs_api',
    #                     help='the dvs api property.')
    args = parser.parse_args(args)
    run(args)


def run(args):
    ''' the run script command '''
    LOGGING.set_logging()
    if args:
        if args.commands and len(args.commands) > 0:
            from com.dvsnier.process.execute import execute as execute_commands
            result = execute_commands(args.commands, quiet=False)
            logging.debug(result)
        else:
            logging.error('the current parameter is illegal and invalid, then parsing return.')
    if DEBUGGER:
        # print('vars(args): {}'.format(vars(args)))
        logging.warning('the current config(args): {}'.format(json.dumps(vars(args), indent=4)))


if __name__ == "__main__":
    '''the main function entry'''
    execute()
