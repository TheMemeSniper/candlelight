### Candlelight
## A TUI frontend to Canvas because the website sucks
# Dashboard UI module
import textual
from textual.app import App, ComposeResult
import os
SCRDIR = os.path.abspath(os.path.dirname(__file__))

class Dashboard(App):
    CSS_PATH = f"{SCRDIR}/style.css"

    