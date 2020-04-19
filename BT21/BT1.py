from flask import Flask, request, Response, jsonify
import json
from flask_pymongo import PyMongo
import logging

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydb'

mongo = PyMongo(app)

logging.basicConfig(filename="newfile.log", 
                    format='%(asctime)s %(levelname)s : %(message)s', 
                    filemode='w', level=logging.DEBUG)
#logger=logging.getLogger()

@app.route('/')
def hello():
    app.logger.info('HomePage Request')
    return "<h1>Hello!</h1>"

@app.route('/all', methods=['GET'])
def all_info():
    df_star = mongo.db.stary
    df_planet = mongo.db.planety
    output = []
    for s in df_star.find():
        output.append({'category' : s['category'], 'name' : s['name'], 'distance' : s['distance']})
    for t in df_planet.find():
        output.append({'category' : t['category'], 'name' : t['name'], 'distance' : t['distance']})
    if output==[]:
        app.logger.warning('No data')
        output="No data"
    else:
        app.logger.info('Full database returned')
    return jsonify({'result' : output})

@app.route('/starinfo/<name>', methods=['GET'])
def star_info(name):
    df_star=mongo.db.stary
    s = df_star.find_one({'name' : name})
    app.logger.info('%s star info requested', name)
    if s:
        app.logger.info('Star data returned: "name": %s, "distance": %s, "category": %s', s['name'], s['distance'], s['category'])
        output = {'name' : s['name'], 'distance' : s['distance'], 'category' : s['category']}
    else:
        app.logger.warning('Star not in database')
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/planetinfo/<name>', methods=['GET'])
def planet_info(name):
    df_planet=mongo.db.planety
    s = df_planet.find_one({'name' : name})
    app.logger.info('%s planet info requested', name)
    if s:
        app.logger.info('Planet data returned: "name": %s, "distance": %s, "category": %s', s['name'], s['distance'], s['category'])
        output = {'name' : s['name'], 'distance' : s['distance'], 'category' : s['category']}
    else:
        app.logger.warning('Planet not in database')
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
    df_star = mongo.db.stary
    name = request.json['name']
    category = 'star'
    distance = request.json['distance']
    if not name or not distance:
        app.logger.error('Request in wrong format')
    else:
        app.logger.info('%s star addded',name)
    star_id = df_star.insert({'name': name, 'distance': distance, 'category': category})
    new_star = df_star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance'], 'category' : new_star['category']}
    return jsonify({'result' : output})

@app.route('/planet', methods=['POST'])
def add_planet():
    df_planet = mongo.db.planety
    name = request.json['name']
    distance = request.json['distance']
    category = 'planet'
    if not name or not distance:
        app.logger.error('Request in wrong format')
    else:
        app.logger.info('%s planet added',name)
    star_id = df_planet.insert({'name': name, 'distance': distance, 'category': category})
    new_star = df_planet.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance'], 'category' : new_star['category']}
    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)