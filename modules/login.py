### Candlelight
## A TUI frontend to Canvas because the website sucks
# Login UI module

"""
This module handles Canvas API authentication. It requests
the user to input their domain and token, and performs
response validation on it. If it is invalid, it will tell
the user that what they have input is invalid. When the
user inputs a valid domain and token, it will return the
domain name input, which will be used by main to find the
token file and log in.
"""
import textual
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import *
import os
import logger
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
    loginlist = ListView(id="loginlist") # return a ListView with the links if there's anything there
    for file in os.listdir(f"{SCRDIR}/../user/creds/"):
        loginlist.append(LabelItem(f"https://{file}.instructure.com"))
    if not loginlist:
        return None
    else:
        return loginlist


class LoginChooser(App):
    """
    Prompt user to pick a login from 
    /user/creds/
    """
    CSS_PATH = theming.findtheme()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Stored logins //", id="title")
        if not (getprexistinglogins() == None): # If some logins already exist, display them
            yield Container(
                    getprexistinglogins()
                    )
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
        self.exit(event.item.label.split("https://")[1].split(".instructure.com")[0]) # reaaaallly bad way of returning the filename
                                                                                      # so programming this is easier

    def on_button_pressed(self, event: Button.Pressed):
        urlinput = self.query_one("#url",Input).value
        tokeninput = self.query_one("#token",Input).value
        errorlabel = self.query_one("#error2",Label)
        urlname = urlinput.split("https://")[1].split(".instructure.com")[0]
        if (urlinput == "" or tokeninput == ""): # input validation
            errorlabel.update(f"{urlinput} {tokeninput}")
            return
        if ("https://" not in urlinput and ".instructure.com" not in urlinput):
            errorlabel.update("Not a valid URL")
            return
        if ("." in urlname): # Protect against path traversal attacks
            errorlabel.update("Subdomain cannot contain periods")
            return
        with open(f"{SCRDIR}/../user/creds/{urlname}", "w+") as file:
            file.write(tokeninput)
        self.exit(urlname)

class LoginError(App):
    """
    Tell the user they're
    annoying and I don't
    want to put up with
    their bad tokens
    (bad login error)
    """
    CSS_PATH = theming.findtheme()

    def compose(self):
        yield Header()
        yield Container(
            Label("Invalid login!"),
            Button.error("sorry :3"),
            id="error"
        )
    def on_button_pressed(self, event: Button.Pressed):
        self.exit()

if __name__ == "__main__":
    app = LoginChooser()
    app.run()
