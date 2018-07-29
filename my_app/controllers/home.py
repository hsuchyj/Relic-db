from flask import Blueprint, render_template, redirect, request, make_response 
from ..app import add_blueprint
import json
from ..config import settings
from os.path import join
from ..scripts import scripts

bp = Blueprint('home', __name__)

@bp.route("/home")
def mainPage():
    return render_template("searchBar.html")
 
add_blueprint(bp)
