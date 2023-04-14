### Candlelight
## A TUI frontend to Canvas because the website sucks
# Main Module

"""
The main module.
It coordinates all the other modules to make candlelight not a library.
What? Were you expecting something else?
"""

VERSION = "0.0.1"
BRANCH = "dev"

import sys # check this before loading everything else so it's quick
if ("--version" in sys.argv):
    print(f"Candlelight {VERSION}-{BRANCH}")
    exit()


from modules import login, api, dashboard, theming, logger
from shutil import copyfile
import textual

from textual.widgets import *
import os
import canvasapi

SCRDIR = os.path.abspath(os.path.dirname(__file__))

if not (os.path.exists(f"{SCRDIR}/user/config/theme")):
    logger.log_warning("/user/config/theme does not exist! Copying default theme /assets/catppuccin-latte.css over it.")
    copyfile(f"{SCRDIR}/assets/stylesheets/catppuccin-latte.css" f"{SCRDIR}/user/config/theme")

currentdisplay = login.LoginChooser()
currentlogin = ""

while True: # login loop
    currentdisplay = login.LoginChooser()
    logger.log("Displayed LoginChooser")
    url = currentdisplay.run() # LoginChooser returns the credfile
    with open(f"{SCRDIR}/user/creds/{url}") as tokenf:
        result = api.validatetoken(url, tokenf.read())
        logger.log("Validating token")
    if (not result):
        if (not ("." in url)): # Protect against path traversal attacks
            os.remove(f"{SCRDIR}/user/creds/")
        logger.log_error("Invalid login!")
        currentdisplay = login.LoginError()
        currentdisplay.run()
    else:
        currentlogin = url
        logger.log("Logged in successfully")
        break
