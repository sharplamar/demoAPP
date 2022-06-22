from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app=app)

@api.route("/conferences/")
def get_all__conferences():
    """
    returns a list of conferences
    """

@api.route("/conferences/", methods=['POST'])
def add_conference():
    """
    Adds a new conference to the list
    """
    
@api.route("/conferences/<int:id>")
def get_conference(id):
    """
    Displays a conference's details
    """
@api.route("/conferences/<int:id>")
def edit_conference(id):
    """
    Edits a selected conference
    """