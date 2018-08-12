from flask import render_template, request, jsonify, abort
from run_server import app
from bson.objectid import ObjectId
import my_app.controllers.dataAccess as dataAccess

@app.route("/home")
def mainPage():
    return render_template("searchBar.html")

# add param for different lti i.e. canvas, respondus etc
@app.route("/import")
def importQuestions():
    return dataAccess.importQuestions()

@app.route("/getTagsFromDB", methods = ["POST"])
def getTagsFromDB():
    if not request.json:
        abort(400)
    tag_level =  request.json.get("tag_level","")
    search_text = request.json.get("search_text","")
    tags = dataAccess.getTags(tag_level, search_text)
    return jsonify({'status': "success", "tags": tags})

@app.route("/question")
def testQues():
        result = dataAccess.get_Questions("VPL", "function", 1,[ObjectId('5b7056d29541f93030da381c')])
        print(result)
        for item in result:
                print(item)



def setup_logging(logging_path, level):
    '''Setups logging in app'''
    from logging.handlers import RotatingFileHandler
    from logging import getLogger, getLevelName
    file_handler = RotatingFileHandler(logging_path)
    file_handler.setLevel(getLevelName(level))
    loggers = [app.logger]
    for logger in loggers:
        logger.addHandler(file_handler)
