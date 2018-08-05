import xmltodict
import pprint
import json
from io import open
from bson import json_util
from pymongo import MongoClient

@app.route('/import')

client = MongoClient('localhost', 27017)
db = client['relic']
questions = db['questions']

#change hard coded location to user select

with open('C:\\Users\\OG AppleJacks\\Documents\\cisc106rework\\staging-mattsap-quiz-export\\i682d359907261533e3507b8d0b191d73\\i682d359907261533e3507b8d0b191d73.xml', encoding='UTF-8') as fd:
    doc = xmltodict.parse(fd.read())
    jsonDoc = json_util.loads(json.dumps(doc))

#for canvas qti only
    
itemsArray = jsonDoc['questestinterop']['assessment']['section']['section'][0]['item']
for doc in itemsArray:
    questions.insert(doc)

#questions.insert(newDoc)
#client.close()

