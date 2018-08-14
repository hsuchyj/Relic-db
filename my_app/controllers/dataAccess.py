
import json
from ..config import settings
from os.path import join
from ..scripts import scripts
from flask import render_template
import xmltodict
import pprint
from io import open
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
import sys
from tkinter import filedialog
from tkinter import *

def importQuestions():
    raise Exception("TODO Not fully implemented")
    """
    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']
    # user selects file from gui
    # root = Tk()
    # root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    xmlLoc = ""
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
    """

def getTags(tag_level, search_text):
   #tag_level is either units, unit_slos, skills, skill_slos
   #search_text is the user's response (e.g. "the") Need to return all units/sklls/etc with "the" inside.
    """
    client = MongoClient('localhost', 27017)
    db = client['relic']
    tags = db['tags']
    select = request.args.get('tagFilter')
    # have to change 'function' to whatever the first entry for that tag is
    tagData = tags.find({select :{'$exists' :True}})
    for items in tagData:
        tagList = items[select]
    return jsonify(result = tagList)
    """
    #replace with call from db
    data =  {"units":[{"unit_name":"Simple Python Data","unit_SLO":"Write a script/program that asks a user for input values from the keyboard, performs a mathematical computation and displays the result to the screen.","topics":["operators","variables"],"skills":[{"skill_name":"algorithms","skill_slos":["write algorithm for solving simple mathematical problems","understand the difference between an algorithm and a program"]},{"skill_name":"operators","skill_slos":["evaluate expressions containing these operators","understand the difference between floating point and integer division","convert a mathematical formula into a Python expression"]}]}]}
    if tag_level == "units":
       results = [unit.get("unit_name","") for unit in data.get("units", []) ]
    elif tag_level == "unit_slos":
       results= [unit.get("unit_SLO", "") for unit in data.get("units", [])]
    elif tag_level == "skills":
       results= [skill.get("skill_name", "") for unit in data.get("units", []) for skill in unit.get("skills", {})]
    elif tag_level == "skill_slos":
       results = []
       for unit in data.get("units", []):
          for skill in unit.get("skills", []):
             for skill_slo in skill.get("skill_slos", []):
                results.append(skill_slo)
    else:
       results = ["Error"]
    return list(filter(lambda text: search_text.lower() in text.lower(), results))

def get_Questions(type, tag, difficulty, excludeIDs):
    #type  = VPL or quiz
    #tag = list
    #difficulty = number
    #list of excluded ids
    client = MongoClient('localhost', 27017)
    db = client['relic']
    tags = db['tags']
    questions = db['questions']
    print("connected to db")
    #query for one tag
    results = questions.find({'$and':[{'type':type}, {'tags':tag}, {'difficulty':difficulty}, {'_id':{'$nin':excludeIDs}}]})
    return results

def tag_and_insert_q():
    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']
    #change this to user input
    root = Tk()
    #root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    #xmlLoc = root.filename
    xmlLoc = "C:\\Users\\OG AppleJacks\\Documents\\cisc106rework\\thisIsQti\\vpl.xml"
    #add script to parse mbz and load xml
    with open(xmlLoc, encoding='UTF-8') as fd:
        doc = xmltodict.parse(fd.read())

    title = doc['activity']['vpl']['name']
    description = doc['activity']['vpl']['intro']

    res = render_template('questionsDisplay.html',
                          t=title,
                          d=description)
    questions.insert_one(doc)
    print("question inserted into db")



