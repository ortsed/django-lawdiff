#!/usr/bin/env python
import site, sys, os
sys.path.insert(0, '/www/lawdiff/')
sys.path.insert(0, '/www/lawdiff/lawdiff/')
site.addsitedir("/www/lawdiff/lib/python" + sys.version[0:3] + "/site-packages")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lawdiff.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
