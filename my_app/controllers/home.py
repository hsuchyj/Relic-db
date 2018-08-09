from flask import render_template, request, jsonify
from run_server import app
import my_app.controllers.dataAccess as dataAccess

@app.route("/home")
def mainPage():
    return render_template("searchBar.html")

# add param for different lti i.e. canvas, respondus etc
@app.route("/import")
def importQuestions():
    return dataAccess.importQuestions()

@app.route("/getTagsFromDB", methods = ["GET"])
def getTagsFromDB():
    return dataAccess.getTags()



def setup_logging(logging_path, level):
    '''Setups logging in app'''
    from logging.handlers import RotatingFileHandler
    from logging import getLogger, getLevelName
    file_handler = RotatingFileHandler(logging_path)
    file_handler.setLevel(getLevelName(level))
    loggers = [app.logger]
    for logger in loggers:
        logger.addHandler(file_handler)
