### Candlelight
## A TUI frontend to Canvas because the website sucks
# Main Module

from modules import login, api, dashboard
import textual

from textual.widgets import *
import os
import canvasapi

SCRDIR = os.path.abspath(os.path.dirname(__file__))

currentdisplay = login.LoginChooser()
print(currentdisplay.run())