### Candlelight
## A TUI frontend to Canvas because the website sucks
# Main Module

VERSION = "0.0.1"
BRANCH = "dev"

import sys # check this before loading everything else so it's quick
if ("--version" in sys.argv):
    print(f"Candlelight {VERSION}-{BRANCH}")
    exit()


from modules import login, api, dashboard
import textual

from textual.widgets import *
import os
import canvasapi

SCRDIR = os.path.abspath(os.path.dirname(__file__))
currentdisplay = login.LoginChooser()
currentlogin = ""

while True: # login loop
    currentdisplay = login.LoginChooser()
    url = currentdisplay.run()
    with open(f"{SCRDIR}/user/creds/{url}") as tokenf:
        result = api.validatetoken(url, tokenf.read())
    if (not result):
        if (not ("." in url)): # Protect against path traversal attacks
            os.remove(f"{SCRDIR}/user/creds/")
        currentdisplay = login.LoginError()
        currentdisplay.run()
    else:
        currentlogin = url
        break
