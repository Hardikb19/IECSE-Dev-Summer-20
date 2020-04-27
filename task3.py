from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import os
import redis
import logging
import wikipedia


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/thirdtask'

mongo = PyMongo(app)

logging.basicConfig(filename="week3.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

redis_host = "localhost"
redis_port = 6379
redis_password = ""

try:
    red = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
except Exception as e:
    print(e)


@app.route('/')
def index():
    return 'send a Post request on with question in data /wiki/'

@app.route('/wiki', methods=['GET'])
def wiki1():
    return "Append any name after /wiki/ to get it's wikipedia summary!!!"

@app.route('/wiki/<name>', methods=['GET'])
def wikfunc(name):
    wikidata=mongo.db.wikidata
    #name= request.json['name']
    result= red.get("result:"+name)
    if result:
        return result
    new_data = wikidata.find_one({'name': name })
    if new_data:
        output= {'data':new_data['data']}
        return output
    try:
        result = wikipedia.WikipediaPage(title=name).summary
        result1=str(result)
        red.set("result:"+name,result1)
        wikidata_id = wikidata.insert({'name': name, 'data': result1})
    except:
        result = 'No data found on wikipedia'
    return result




if __name__ == '__main__':
    port1 = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0' , port=port1)
