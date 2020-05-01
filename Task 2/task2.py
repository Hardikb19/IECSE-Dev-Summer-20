from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'empdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/empdb'

mongo = PyMongo(app)

@app.route('/emply/all', methods=['GET'])
def get_all_details():
  emp = mongo.db.emp_dets
  output = []
  for e in emp.find():
    output.append({'name' : e['name'], 'email' : e['email'], 'phone' : e['phone'], 'address': e['address'], 'department' : e['department']})
  return jsonify({'result' : output})

@app.route('/emply/name/<name>', methods=['GET'])
def get_name(name):
  emp = mongo.db.emp_dets
  e = emp.find_one({'name' : name})
  if e:
    output = {'name' : e['name'], 'email' : e['email'], 'phone' : e['phone'], 'address': e['address'], 'department' : e['department']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/emply/email/<email>', methods=['GET'])
def get_email(email):
  emp = mongo.db.emp_dets
  e = emp.find_one({'email' : email})
  if e:
    output = {'name' : e['name'], 'email' : e['email'], 'phone' : e['phone'], 'address': e['address'], 'department' : e['department']}
  else:
    output = "No such email"
  return jsonify({'result' : output})

@app.route('/emply/addemply', methods=['POST'])
def add_employee():
  emp = mongo.db.emp_dets
  name = request.json['name']
  email = request.json['email']
  phone = request.json['phone']
  address = request.json['address']
  department = request.json['department']
  emp_id = emp.insert({'name' : name, 'email' : email, 'phone' : phone, 'address': address, 'department' : department })
  e = emp.find_one({'_id': emp_id })
  output = {'name' : e['name'], 'email' : e['email'], 'phone' : e['phone'], 'address': e['address'], 'department' : e['department']}
  return jsonify({'result' : output})

@app.route('/emply/editemply/<name>', methods=['PUT'])
def edit_employee(name):
  editquery = { 'name': name }
  
  emp = mongo.db.emp_dets
  name = request.json['name']
  email = request.json['email']
  phone = request.json['phone']
  address = request.json['address']
  department = request.json['department']
  
  e = emp.find_one({'name': name })
  newemp = { "$set": {'name' : name, 'email' : email, 'phone' : phone, 'address': address, 'department' : department } }
  emp.update_many(editquery, newemp)
  output = {'name' : e['name'], 'email' : e['email'], 'phone' : e['phone'], 'address': e['address'], 'department' : e['department']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)