from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/')
def index():
    return ' Hello world, ask me about the stars. '

@app.route('/star', methods=['GET'])
def get_all_stars():
  star = mongo.db.stars
  output = []
  for s in star.find():
    output.append({'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})

@app.route('/star/names', methods=['GET'])
def get_all_names():
  star = mongo.db.stars
  output = []
  for s in star.find():
    output.append({'name' : s['name']})
  return jsonify({'result' : output})

@app.route('/star/distances', methods=['GET'])
def get_all_distances():
  star = mongo.db.stars
  output = []
  for s in star.find():
    output.append({'distance' : s['distance']})
  return jsonify({'result' : output})
#@app.route('/star/:name', methods=['GET'])
#def get_one_star(name):
  #return name
  #star = mongo.db.stars
  #s = star.find_one({'name' : name})
  #if s:
    #output = {'name' : s['name'], 'distance' : s['distance']}
  #else:
    #output = "No such name"
  #return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

@app.route('/star/update', methods=['POST'])
def update_star():
    star=mongo.db.stars
    name = request.json['name']
    distance=request.json['distance']
    new_star = star.find_one({'name': name })
    if not new_star:
        star = mongo.db.stars
        name = request.json['name']
        distance = request.json['distance']
        star_id = star.insert({'name': name, 'distance': distance})
        new_star = star.find_one({'_id': star_id })
        output = {'name' : new_star['name'], 'distance' : new_star['distance']}
        return jsonify({'result' : output})

    myquery = { "name":name,"distance": new_star['distance'] }
    newvalues = { "$set": {"name":name, "distance": distance } }
    #new_star['distance']=distance
    star.update_one(myquery, newvalues)
    output = {'name' : name, 'distance' : distance}
    return jsonify({'result' : output})

#@app.route('/star/distanceless', methods=['POST'])
#def get_all_distance_name():
    #star=mongo.db.stars
    #distance=request.json['distance']
    #myquery = { "distance": { "$lte": distance } }
    #for x in star.find(myquery):
        #output.append( {'name' : x['name']} )
    #return jsonify({'result' : output})

@app.route('/star/distance', methods=['POST'])
def get_name():
    star=mongo.db.stars
    distance=request.json['distance']
    new_star = star.find_one({'distance': distance })
    if not new_star:
        return jsonify({'result':'Not found. Use /star/distances and GET method to know distance data'})
    output = {'name' : new_star['name'], 'distance' : distance}
    return jsonify({'result' : output})


if __name__ == '__main__':
    port1 = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0' , port=port1)
