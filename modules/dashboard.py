### Candlelight
## A TUI frontend to Canvas because the website sucks
# Dashboard UI module
import textual
from textual.app import App, ComposeResult
import os
SCRDIR = os.path.abspath(os.path.dirname(__file__))

class Dashboard(App):
    """
    Main UI
    """
    CSS_PATH = f"{SCRDIR}/style.css"
    yield Header()
    



if __name__ == "__main__":
    app = Dashboard()
    app.run()