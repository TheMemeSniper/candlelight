### Candlelight
## A TUI frontend to Canvas because the website sucks
# Login UI module

import textual
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import *
import os
SCRDIR = os.path.abspath(os.path.dirname(__file__))

class LabelItem(ListItem): # For some inconcievable reason, Textual
                           # can't just return the content of a ListItem,
                           # so we have to do it ourselves.
    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = label

    def compose( self ) -> ComposeResult:
        yield Label(self.label)

def getprexistinglogins(): # List everything in /user/creds and
    loginlist = ListView() # return a ListView with the links if there's anything there
    for file in os.listdir(f"{SCRDIR}/../user/creds/"):
        loginlist.append(LabelItem(f"https://{file}.instructure.com"))
    if not loginlist:
        return None
    else:
        return loginlist


class LoginChooser(App):
    CSS_PATH = f"{SCRDIR}/../assets/style.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Stored logins //", id="title")
        if not (getprexistinglogins() == None): # If some logins already exist, display them
            yield getprexistinglogins()
        else:
            yield Container(
                Label("No logins found!"), # If not, display an error
                id="error"
            )
        yield Label("New login //", id="title2")
        yield Container(
            Label("URL"),
            Input(placeholder="https://yourschool.instructure.com", id="url"),
            Label("Canvas Token"),
            Input(placeholder="12345~donotshareyourtokenalsohi:3", password=True, id="token"),
            Button("Go!", variant="primary",),
            id="login"
        )
        yield Label("", id="error2")
        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected):
        self.exit(event.item.label.split("https://")[1].split(".instructure.com")[0]) # reaaaallly bad way of returning the filenaem
                                                                                      # so programming this is easier

    def on_button_pressed(self, event: Button.Pressed):
        urlinput = self.query_one("#url",Input).value
        tokeninput = self.query_one("#token",Input).value
        errorlabel = self.query_one("#error2",Label)
        if (urlinput or tokeninput == ""): # input validation
            errorlabel.update("Empty input")
            return
        if ("https://" and ".instructure.com" not in urlinput):
            errorlabel.update("Not a valid URL")
            return
        urlname = urlinput.split("https://")[1].split(".instructure.com")[0]
        with open(f"{SCRDIR}/../user/creds/{urlname}", "w+") as file:
            file.write(tokeninput)
        self.exit(urlname)

if __name__ == "__main__":
    app = LoginChooser()
    app.run()