# -*- coding:utf-8 -*-

import argparse
import datetime
import json
import os
import sys
from time import sleep

from com.dvsnier.config.journal.compat_logging import logging
from com.dvsnier.directory.base_file import BaseFile
from com.dvsnier.tool import DEBUGGER, VERSIONS
from com.dvsnier.tool.util.dvs_logging import LOGGING
from com.dvsnier.tool.util.vscode_ws import EXCLUDE_LIST, find_git_repository_quickly, generator_vscode_workspace


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
        prog='dvs-vsws',
        description="""
    this is a dvs android execution program.
        """,
        epilog='the copyright belongs to DovSnier that reserve the right of final interpretation.\n',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-V', '--version', action='version', version=VERSIONS, help='the show version and exit.')
    parser.add_argument(
        'destination_directory',
        action='store',
        nargs='*',
        default=os.getcwd(),
        type=str,
        metavar='destination-directory',
        # dest='destination_directory',
        help='the current destination directories to be searched.')
    parser.add_argument('-el',
                        '--exclude-list',
                        action='store',
                        nargs='*',
                        default=EXCLUDE_LIST,
                        type=str,
                        metavar='exclude-list',
                        dest='exclude_list',
                        help='the collection of paths excluded by the current search index.')
    # parser.add_argument('-gw',
    #                     '--generate-workspace',
    #                     action='store',
    #                     nargs=1,
    #                     default=None,
    #                     type=str,
    #                     metavar='generate-workspace',
    #                     dest='generate_workspace',
    #                     help='the generate workspace that is absolute path xxx.code-workspace name.')
    args = parser.parse_args(args)
    run(args)


def run(args):
    ''' the run script command '''
    LOGGING.set_logging()
    if args:
        if args.destination_directory:
            if args.exclude_list and len(args.exclude_list) > 0:
                for exclude in args.exclude_list:
                    if exclude not in EXCLUDE_LIST:
                        EXCLUDE_LIST.append(exclude)
                        logging.debug('the current name({}) added to ignore file.'.format(exclude))
                args.exclude_list = EXCLUDE_LIST
                logging.debug('the current list of ignored files is {}.'.format(
                    json.dumps(args.exclude_list, ensure_ascii=False, indent=4)))
            _directory = BaseFile(True)
            _directory.set_work_region_space(os.getcwd())
            if args.destination_directory and isinstance(args.destination_directory, list):
                for absolute_workspace_or_repository in args.destination_directory:
                    git_queue = find_git_repository_quickly(absolute_workspace_or_repository)  # item queue
                    ws_name = _directory.generate_file_name(
                        'code-workspace',
                        'workspace_{}.ws.code-workspace'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')))
                    logging.warning('this current file is that generate ws region name is {}'.format(ws_name))
                    generator_vscode_workspace(git_queue, ws_name)
                    sleep(1)
            else:
                git_queue = find_git_repository_quickly(args.destination_directory)
                ws_name = _directory.generate_file_name(
                    'code-workspace',
                    'workspace_{}.ws.code-workspace'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')))
                logging.warning('this current file is that generate ws region name is {}'.format(ws_name))
                generator_vscode_workspace(git_queue, ws_name)
        else:
            logging.error('the current parameter is illegal and invalid, then parsing return.')
    if DEBUGGER:
        # print('vars(args): {}'.format(vars(args)))
        logging.warning('the current config(args): {}'.format(json.dumps(vars(args), indent=4)))


if __name__ == "__main__":
    '''the main function entry'''
    execute()
