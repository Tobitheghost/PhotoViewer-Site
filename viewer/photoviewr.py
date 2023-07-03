from flask import Blueprint, render_template, request, redirect, url_for
from .tools import setup, list_dir

photoviewer = Blueprint('photoviewer', __name__)

@photoviewer.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name, folderDir = setup(request.form["folders"])
        
    else:
        name, folderDir = setup()
    listFiles, vidExtentions = list_dir(name)

    return render_template("index.html", name=name, folder=folderDir, listFiles=listFiles, vidExtentions=vidExtentions)
