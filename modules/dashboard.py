### Candlelight
## A TUI frontend to Canvas because the website sucks
# Dashboard UI module
"""
This module is probably what you'll be looking at all day
at 6AM on a Sunday because you forgot to write a 10 page
essay last week. Anyways, this displays all your courses
in a tabbed list view, with a dedicated tab for missing
work and unread Canvas messages.
"""
import textual
from textual.app import App, ComposeResult
import os
SCRDIR = os.path.abspath(os.path.dirname(__file__))

def Dashboard(App):
    """
    Main UI
    """
    CSS_PATH = f"{SCRDIR}/style.css"
    yield Header()
    
    



if __name__ == "__main__":
    app = Dashboard()
    app.run()