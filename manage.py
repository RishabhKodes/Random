#!/usr/bin/env python3
import os
import sys

#Django settings module
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed &"
            "available on your PYTHONPATH environment variable? Don't "
            "forget to activate a virtual environment in the path?"
        ) from exc
    execute_from_command_line(sys.argv)
