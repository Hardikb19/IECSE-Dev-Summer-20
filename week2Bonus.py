from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import os
import hashlib
import logging

logging.basicConfig(filename="week2.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

print(mongo.db.list_collection_names())


@app.route('/')
def index():
    return ' Hello world, ask me about the stars. '

@app.route('/star/get', methods=['GET'])
def get_all_stars():
  try:
    star = mongo.db.stars
    output = []
    for s in star.find():
      output.append({'name' : s['name'], 'distance' : s['distance']})
    logger.info({'result': output})
    return jsonify({'result' : output})
  except:
    logger.error("Client is maybe not available.")
    return jsonify({'result' : None})

@app.route('/star/names', methods=['GET'])
def get_all_names():
  try:
    star = mongo.db.stars
    output = []
    for s in star.find():
      output.append({'name' : s['name']})
    logger.info({'result': output})
    return jsonify({'result' : output})
  except:
    logger.error("Client is maybe not available.")
    return jsonify({'result' : None})

@app.route('/star/distances', methods=['GET'])
def get_all_distances():
  try:
    star = mongo.db.stars
    output = []
    for s in star.find():
      output.append({'distance' : s['distance']})
    logger.info({'result':output})
    return jsonify({'result' : output})
  except:
    logger.error("Client is maybe not available.")
    return jsonify({'result' : None})

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

@app.route('/star/post', methods=['POST'])
def add_star():
  try:
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance']}
    logger.info({'result': output})
    return jsonify({'result' : output})
  except:
    logger.error("Client is maybe not available")
    return jsonify({'result': None})

@app.route('/star/update', methods=['POST'])
def update_star():
  try:
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
      logger.info({'result': output})
      return jsonify({'result' : output})

    myquery = { "name":name,"distance": new_star['distance'] }
    newvalues = { "$set": {"name":name, "distance": distance } }
    #new_star['distance']=distance
    star.update_one(myquery, newvalues)
    output = {'name' : name, 'distance' : distance}
    logger.info({'result': output})
    return jsonify({'result' : output})
  except:
    logger.error("Client is maybe not available")
    return jsonify({'result': None})

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
  try:
    star=mongo.db.stars
    distance=request.json['distance']
    new_star = star.find_one({'distance': distance })
    if not new_star:
      logger.error("Wrong distance input")
      return jsonify({'result':'Not found. Use /star/distances and GET method to know distance data'})
    output = {'name' : new_star['name'], 'distance' : distance}
    logger.info({'result': output})
    return jsonify({'result' : output})
  except:
    logger.error("Client is maybe not available")
    return jsonify({'result': None})

@app.route('/star/userdata',methods=['POST'])
def user_login():
  try:
    user=mongo.db.users
    username= request.json['username']
    password= request.json['password']
    new_user = user.find_one({'username':username})
    if new_user:
      logger.error("User already exists. Shouldn't have tried to access again")
      return jsonify({"Username already exists ":username})
    salt = os.urandom(32) # A new salt for this user
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    user_id=user.insert({'username':username, 'salt':salt , 'key':key})
    logger.info("Entered data of "+ username)
    return jsonify({'Data entered of ':username})
  except:
    logger.error("Error in data collection")
    return jsonify({'result':None})

@app.route('/star/usercheck',methods=['POST'])
def user_check():
  try:
    user = mongo.db.users
    username= request.json['username']
    password= request.json['password']
    new_user= user.find_one({'username': username})
    if not new_user:
      logger.error("Username doesn't exist")
      return jsonify({'result':"Username doesn't exist"})
    usalt = new_user['salt']
    ukey = new_user['key']
    keyn = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), usalt, 100000)
    if keyn == ukey:
      logger.info({"Login by user":username})
      return jsonify({'result':True})
    else:
      logger.info({"Illegal login for user":username})
      return jsonify({'result':False})
  except:
    logger.error("Client may not be available")
    return jsonify({'result': None})


if __name__ == '__main__':
    port1 = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0' , port=port1)
