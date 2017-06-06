#!/usr/bin/env python
<<<<<<< HEAD
"""
Command-line utility for administrative tasks.
"""

=======
>>>>>>> bd90123510bc5894ca7541d6577fcc23e9bc150d
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "ApproApp.settings"
    )
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
>>>>>>> bd90123510bc5894ca7541d6577fcc23e9bc150d

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
