from flask import flask 

app = flask(__name__)

@ap.route("/conferences")
def get_all_conferences():
    """
    returns a list of conferences
    """

@app.route("/conferences/",methods=['post'])
def add_conference():
    """
    adds a new conference to the list
    """

@app.route("/conferences/<int:id>")
def get_conference(id):
    """
    Displays a conference`s details

    """

@app.route("/conferences/<int:id>")
def edit_conference(id):
    """
    Edits a selected conference
    """