# -*- coding:utf-8 -*-

import json
import os
import re
import time

from com.dvsnier.config.journal.compat_logging import logging
from com.dvsnier.directory.base_file import BaseFile

EXCLUDE_LIST = [
    '.buildscript',
    '.DS_Store',
    '.gitee',
    '.github',
    '.gradle',
    '.idea',
    '.settings',
    '.tox',
    '.vscode',
    '__tests__',
    '__pycache__',
    'asset',
    'assets',
    'bin',
    'build',
    'conf',
    'config',
    'dist',
    'docs',
    'example',
    'fastlane',
    'gen',
    'gradle',
    'include',
    'lib',
    'library',
    'log',
    'mock',
    'node_modules',
    'out',
    'plugins',
    'Pods',
    'src',
    'script',
    'scripts',
    'test',
    'venv',
    'venv2',
]


def find_git_repository_quickly(destination_directory=None):
    'the quickly find git repository'
    destination_directories = []
    _directory = BaseFile(True)  # protected property
    if isinstance(destination_directory, str):
        destination_directories = [destination_directory]
    elif isinstance(destination_directory, list):
        destination_directories = destination_directory
    else:
        destination_directories = [os.path.dirname(os.getcwd())]
    _directory.set_work_region_space(os.getcwd())
    git_queue = find_git_repository(destination_directories, EXCLUDE_LIST)
    logging.debug('the find git repository list that is {}.'.format(json.dumps(git_queue, ensure_ascii=False,
                                                                               indent=4)))
    return git_queue


def find_git_repository(absolute_dir_list, exclude_list=[]):
    'the find git repository'
    git_repository_queue = []
    find_start = time.time()
    if absolute_dir_list and len(absolute_dir_list) > 0:
        for absolute_dir in absolute_dir_list:
            if absolute_dir and os.path.exists(absolute_dir):
                git_repository_queue.extend(__find_special_directory(absolute_dir, exclude_list))
    find_end = time.time()
    logging.info('the find git repository that total time is {:.3f}s'.format(find_end - find_start))
    return git_repository_queue


def __find_special_directory(dir, exclude_list=[]):
    git_repository_queue = []
    # logging.debug('the current directory or file is {}'.format(dir))
    if os.path.isdir(dir):
        directory = os.listdir(dir)
        directory.sort()
        # logging.debug('the currently retrieved list information is {}'.format(directory))
        for file in directory:
            if exclude_list and len(exclude_list) > 0 and file in exclude_list:
                # logging.warning('the current directory or file is {} and ignore retrieval, skip check for {}'.format(file, file))
                continue
            # logging.info('the current retrieved file or directory that is {}'.format(file))
            if os.path.isdir(os.path.join(os.path.realpath(dir), file)):  # it is directory
                if file == '.git':
                    git_directory = os.path.dirname(os.path.join(os.path.realpath(dir), file))
                    # logging.warning('The current project directory is git project, ready to add {} to the queue.'.forma(git_directory))
                    git_repository_queue.append(git_directory)
                else:  # the recursive execute
                    sub_git_repository_queue = __find_special_directory(os.path.join(dir, file), exclude_list)
                    # logging.warning('Start a recursive call to find the subdirectory {}'.format(os.path.join(dir, file)))
                    if sub_git_repository_queue and len(sub_git_repository_queue) > 0:
                        git_repository_queue.extend(sub_git_repository_queue)
            else:
                # logging.debug('the current file is {} that is maybe skipped.'.format(file))
                continue
    # if git_repository_queue and len(git_repository_queue) > 0:
    #     logging.info('the current list of returned child git items is {}'.format(git_repository_queue))
    return git_repository_queue


def generator_vscode_workspace(absolute_git_repository_list, ws_name):
    '''
        the generator vscode workspace

        Now let's define the workspace concept as follows:

            1. work_sapce_xxx and worksapce and worksapces: the standard worksapce region;
            2. xxx_repository and xxx_repositories: the standard type repository region;
            3. vscode ws is generated in both of the above;

        absolute_git_repository_list: list string type
        ws_name: vscode worksapce name
        flag: 0: the default no merge repository; 1: the merge brother directory repository; the current no support it;
    '''
    if absolute_git_repository_list and len(absolute_git_repository_list) > 0:
        vsc_ws_region = dict()
        vsc_ws_folders = []
        KEY_NAME = 'name'
        KEY_PATH = 'path'
        KEY_FOLDERS = 'folders'
        KEY_SETTINGS = 'settings'
        for index, git_repository_path in enumerate(absolute_git_repository_list):
            vsc_ws_item = dict()
            project_name = os.path.basename(git_repository_path)
            project_directory_path = os.path.dirname(git_repository_path)
            split_list = project_directory_path.split(os.path.sep)
            if split_list and len(split_list) > 0:
                split_list.reverse()
                for split_item in split_list:
                    match = re.search(
                        r'(work_space[\w]*_\w+)|(WorkSpace[\w]*_\w+)|(\w*workspace\w*)|(\w+_repositor\w+)',
                        split_item,
                        flags=re.I)
                    if match:
                        prefix = re.sub(r'(work_space[\w]*_)|(WorkSpace[\w]*_)|(workspace[\w]*)|(_repositor[\w]*)',
                                        '',
                                        match.string,
                                        flags=re.I)
                        pattern = re.compile('{}'.format(prefix), flags=re.I)
                        if prefix and re.match(pattern, project_name):
                            if KEY_NAME not in vsc_ws_item.keys():
                                vsc_ws_item.update({KEY_NAME: project_name})
                        else:
                            if KEY_NAME not in vsc_ws_item.keys():
                                vsc_ws_item.update({KEY_NAME: '{}-{}'.format(prefix, project_name)})
                                # logging.debug('the current project space is replace character that is {} -> {}'.format(
                                #     match.string, prefix))
                    else:
                        if KEY_NAME not in vsc_ws_item.keys():
                            vsc_ws_item.update({KEY_NAME: project_name})
            else:
                vsc_ws_item.update({KEY_NAME: project_name})
            vsc_ws_item.update({KEY_PATH: git_repository_path})
            vsc_ws_folders.append(vsc_ws_item)
        vsc_ws_region.update({KEY_FOLDERS: vsc_ws_folders})
        vsc_ws_settings = dict()
        vsc_ws_region.update({KEY_SETTINGS: vsc_ws_settings})
        if ws_name:
            with open(ws_name, 'w') as file:
                file.write(json.dumps(vsc_ws_region, ensure_ascii=False, indent=4))
        else:
            raise ValueError('the current ws_name is an illegal parameter.')
    else:
        logging.error('the current absolute path is an illegal parameter and then skipping it.')
