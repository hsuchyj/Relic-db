
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
from flask import render_template
from run_server import app

@app.route("/home")
def mainPage():
    return render_template("searchBar.html")


# add param for different lti i.e. canvas, respondus etc
@app.route("/import")
def importQuestions():
    client = MongoClient('localhost', 27017)

    # user selects file from gui

    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    xmlLoc = root.filename
    with open(xmlLoc, encoding='UTF-8') as fd:
        doc = xmltodict.parse(fd.read())
        jsonDoc = json_util.loads(json.dumps(doc))

    # for canvas qti only

    itemsArray = jsonDoc['questestinterop']['assessment']['section']['section'][0]['item']
    for doc in itemsArray:
        questions.insert(doc)

        # questions.insert(newDoc)
        # client.close()
    print("imported stuff")

def setup_logging(logging_path, level):
    '''Setups logging in app'''
    from logging.handlers import RotatingFileHandler
    from logging import getLogger, getLevelName
    file_handler = RotatingFileHandler(logging_path)
    file_handler.setLevel(getLevelName(level))
    loggers = [app.logger]
    for logger in loggers:
        logger.addHandler(file_handler)
