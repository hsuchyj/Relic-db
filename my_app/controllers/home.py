from flask import Blueprint, render_template, redirect, request, make_response 
from ..app import add_blueprint
import json
from ..config import settings
from os.path import join
from ..scripts import scripts

import xmltodict
import pprint
from io import open
from bson import json_util
from pymongo import MongoClient
from tkinter import filedialog
from tkinter import *

bp = Blueprint('home', __name__)

@bp.route("/home")
def mainPage():
    return render_template("searchBar.html")

@bp.route("/import")
def importQuestions():
    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']

    #user selects
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
    xmlLoc = root.filename
    with open(xmlLoc, encoding='UTF-8') as fd:
        doc = xmltodict.parse(fd.read())
        jsonDoc = json_util.loads(json.dumps(doc))

    #for canvas qti only
    
    itemsArray = jsonDoc['questestinterop']['assessment']['section']['section'][0]['item']
    for doc in itemsArray:
        questions.insert(doc)

    #questions.insert(newDoc)
    #client.close()
        
add_blueprint(bp)
