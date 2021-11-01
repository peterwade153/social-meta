#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def read_env_file(file_name):
    try:
        with open(os.path.join('environments/', file_name), 'r') as f:
            lines = [line.rstrip('/n').split('=', 1) for line in f]
            for line in lines:
                if line[0] not in os.environ:
                    print(f'Setting env var {line[0]} to {line[1]}')
                    os.environ.setdefault(line[0], line[1])
    except FileNotFoundError:
        print(f'Env file {file_name} not found')


def main():
    """Run administrative tasks."""
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    if 'ENV_VAR_FILE' in os.environ:
        file_name = os.getenv('ENV_VAR_FILE')
        read_env_file(file_name)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
