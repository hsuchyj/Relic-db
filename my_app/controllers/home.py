
import json
from ..config import settings
from os.path import join
from ..scripts import scripts

import xmltodict
import pprint
from io import open
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
from tkinter import filedialog
from tkinter import *
from flask import render_template, request, jsonify
from run_server import app
import sys


@app.route("/home")
def mainPage():
    return render_template("searchBar.html")


# add param for different lti i.e. canvas, respondus etc
@app.route("/import")
def importQuestions():
    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']
    # user selects file from gui
    #root = Tk()
    #root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    xmlLoc = "C:\\Users\\OG AppleJacks\\Documents\\cisc106rework\\staging-mattsap-quiz-export\\i682d359907261533e3507b8d0b191d73\\i682d359907261533e3507b8d0b191d73.xml"
    with open(xmlLoc, encoding='UTF-8') as fd:
        doc = xmltodict.parse(fd.read())
        jsonDoc = json_util.loads(json.dumps(doc))
    # for canvas qti only
    itemsArray = jsonDoc['questestinterop']['assessment']['section']['section'][0]['item']
    for doc in itemsArray:
        questions.insert(doc)

        # questions.insert(newDoc)
    client.close()
    print("imported stuff")

@app.route("/getTagsFromDB", methods = ["GET"])
def getTagsFromDB():
    client = MongoClient('localhost', 27017)
    db = client['relic']
    tags = db['tags']
    select = request.args.get('tagFilter')
    #have to change 'function' to whatever the first entry for that tag is
    tagData = tags.find({select:{'$exists':True}})
    for items in tagData:
        tagList = items[select]
    return jsonify(result = tagList)


def setup_logging(logging_path, level):
    '''Setups logging in app'''
    from logging.handlers import RotatingFileHandler
    from logging import getLogger, getLevelName
    file_handler = RotatingFileHandler(logging_path)
    file_handler.setLevel(getLevelName(level))
    loggers = [app.logger]
    for logger in loggers:
        logger.addHandler(file_handler)
