from flask import Flask, request, Response, jsonify
import json
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/')
def hello():
    return "<h1>Hello!</h1>"

@app.route('/all', methods=['GET'])
def all_info():
    df_star = mongo.db.star
    df_planet = mongo.db.planet
    output = []
    for s in df_star.find():
        output.append({'category' : s['category'], 'name' : s['name'], 'distance' : s['distance']})
    for t in df_planet.find():
        output.append({'category' : t['category'], 'name' : t['name'], 'distance' : t['distance']})
    if output==[]:
        output="No data"
    return jsonify({'result' : output})

@app.route('/starinfo/<name>', methods=['GET'])
def star_info(name):
    df_star=mongo.db.star
    s = df_star.find_one({'name' : name})
    if s:
        output = {'name' : s['name'], 'distance' : s['distance'], 'category' : s['category']}
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/planetinfo/<name>', methods=['GET'])
def planet_info(name):
    df_planet=mongo.db.planet
    s = df_planet.find_one({'name' : name})
    if s:
        output = {'name' : s['name'], 'distance' : s['distance'], 'category' : s['category']}
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
    df_star = mongo.db.star
    name = request.json['name']
    category = 'star'
    distance = request.json['distance']
    star_id = df_star.insert({'name': name, 'distance': distance, 'category': category})
    new_star = df_star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance'], 'category' : new_star['category']}
    return jsonify({'result' : output})

@app.route('/planet', methods=['POST'])
def add_planet():
    df_planet = mongo.db.planet
    name = request.json['name']
    distance = request.json['distance']
    category = 'planet'
    star_id = df_planet.insert({'name': name, 'distance': distance, 'category': category})
    new_star = df_planet.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance'], 'category' : new_star['category']}
    return jsonify({'result' : output})

app.run(host='0.0.0.0',port=5000)