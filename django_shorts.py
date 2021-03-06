#!/usr/bin/env python

import os
import sys
from subprocess import call

ALIASES = {
    # Django
    'c'  : 'collectstatic',
    'r'  : 'runserver',
    'sd' : 'syncdb',
    'sp' : 'startproject',
    'sa' : 'startapp',
    't'  : 'test',

    # Shell
    'd'  : 'dbshell',
    's'  : 'shell',

    # Auth
    'csu': 'createsuperuser',
    'cpw': 'changepassword',

    # South
    'm'  : 'migrate',
    'mkm' : 'makemigrations',

    # session
    'cs' : 'clearsessions',

#     # Haystack
#     'ix' : 'update_index',
#     'rix': 'rebuild_index',

#     # Django Extensions
#     'sk' : 'generate_secret_key',
#     'rdb': 'reset_db',
#     'rp' : 'runserver_plus',
#     'shp': 'shell_plus',
#     'url': 'show_urls',
#     'gm' : 'graph_models',
#     'rs' : 'runscript'
}


def run(command=None, *arguments):
    """
    Run the given command.
    Parameters:
    :param command: A string describing a command.
    :param arguments: A list of strings describing arguments to the command.
    """

    if command is None:
        sys.exit('django-shorts: No argument was supplied, please specify one.')

    if command in ALIASES:
        command = ALIASES[command]

    if command == 'startproject':
        return call('django-admin.py startproject {}'.format(' '.join(arguments)), shell=True)

    script_path = os.getcwd()
    while not os.path.exists(os.path.join(script_path, 'manage.py')):
        base_dir = os.path.dirname(script_path)
        if base_dir != script_path:
            script_path = base_dir
        else:
            sys.exit('django-shorts: No \'manage.py\' script found in this directory or its parents.')

    a = {
        'python': sys.executable,
        'script_path': os.path.join(script_path, 'manage.py'),
        'command': command or '',
        'arguments': ' '.join(arguments)
    }
    return call('{python} {script_path} {command} {arguments}'.format(**a), shell=True)


def main():
    """Entry-point function."""
    try:
        sys.exit(run(*sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
