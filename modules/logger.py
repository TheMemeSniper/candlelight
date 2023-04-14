### Candlelight
## A TUI frontend to Canvas because the website sucks
# Dashboard UI module

"""
This module is called by main and other functions to
provide a verbose log in /logs for debugging. It
writes to a file with the current date and time when
the module is imported.
"""

import inspect
import os
from datetime import datetime

curtime = datetime.today().strftime('%Y-%m-%d')
SCRDIR = os.path.abspath(os.path.dirname(__file__))

def get_calling_module_name():
    """
    Only for use internally by
    the logger module! If you
    need to use this outside of
    logger, think again!

    Returns name of module calling the function
    """
    frm = inspect.stack()[2]
    mod = inspect.getmodule(frm[0])
    return mod.__name__


def writelog(text):
    """
    Only for use internally by
    the logger module! If you
    need to use this outside of
    logger, think again!

    Writes to today's log file
    """
    with open(f"{SCRDIR}/../logs/{curtime}", "a") as log:
        log.write(text)

def log_error(text):
    """
    Log an error in /logs.
    """
    writelog(f"[(!!!) {get_calling_module_name()} ERROR]: {text}\n")

def log_warning(text):
    """
    Log a warning in /logs.
    """
    writelog(f"[(!) {get_calling_module_name()} WARNING]: {text}\n")

def log(text):
    """
    Log in /logs.
    """
    writelog(f"[(i) {get_calling_module_name()} DEBUG]: {text}\n")