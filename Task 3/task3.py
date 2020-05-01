import wikipedia
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import redis
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'wikidb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/wikidb'

mongo = PyMongo(app)

redis_host = "localhost"
redis_port = 6379
redis_password = ""

r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/wiki/addInfo', methods=['POST'])
def Add_Info():
    wiki = mongo.db.wiki_dets
    name = request.json['name']    
    
    if(r.get(name)!=None):
        output = {'name' : name, 'info' : r.get(name)}
        return jsonify({'result' : output})

    else:
        info = ''
        try:
            info = wikipedia.WikipediaPage(title=name).summary
        except:
            info = ''

        w_test = wiki.find_one({'name' : name})
    
        if(w_test == None):
            wiki_id = wiki.insert({'name' : name, 'info' : info})
            w = wiki.find_one({'_id' : wiki_id}) 
            output = {'name' : w['name'], 'info' : w['info']}
            r.set(name, info)
        else:
            r.set(name, info)
            output = {'name' : w_test['name'], 'info' : w_test['info']}
        return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)