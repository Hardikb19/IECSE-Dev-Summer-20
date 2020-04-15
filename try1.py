from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/food/all', methods=['GET'])
def get_all_details():
  f = mongo.db.foods
  output = []
  for i in f.find():
    output.append({'name' : i['name'], 'taste' : i['taste']})
  return jsonify({'result' : output})

@app.route('/food/name/<name>', methods=['GET'])
def get_foodname(name):
  f = mongo.db.foods
  output=[]
  s = f.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'taste' : s['taste']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/food/taste/<taste>', methods=['GET'])
def get_foodtaste(taste):
  f = mongo.db.foods
  output=[]
  s = f.find_one({'taste' : taste})
  if s:
     output = {'name' : s['name'], 'taste' : s['taste']}
  else:
    output = "No such taste"
  return jsonify({'result' : output})

@app.route('/food/add', methods=['POST'])
def add_food():
  f = mongo.db.foods
  name = request.json['name']
  taste = request.json['taste']
  food_id = f.insert({'name': name, 'taste': taste})
  new_food = f.find_one({'_id': food_id })
  output = {'name' : new_food['name'], 'taste' : new_food['taste']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
