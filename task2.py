from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

# People


@app.route('/people', methods=['GET'])
def get_all_people():
    people = mongo.db.people
    output = []
    for x in people.find():
        output.append({'name': x['name'], 'email_id': x['email_id'], 'contact_no': x['contact_no']})
    return jsonify({'result': output})


@app.route('/people/', methods=['GET'])
def get_one_person(name):
    people = mongo.db.people
    x = people.find_one({'name': name})
    if x:
        output = {'name': x['name'], 'email_id': x['email_id'], 'contact_no': x['contact_no']}
    else:
        output = "No such name"
    return jsonify({'result': output})


@app.route('/people', methods=['POST'])
def add_star():
    people = mongo.db.people
    name = request.json['name']
    email_id = request.json['email_id']
    contact_no = request.json['contact_no']
    id = people.insert({'name': name, 'email_id': email_id, 'contact_no': contact_no})
    new = people.find_one({'_id': id})
    output = {'name': new['name'], 'email_id': new['email_id'], 'contact_no': new['contact_no']}
    return jsonify({'result': output})

# Groups


@app.route('/groups', methods=['GET'])
def get_all_groups():
    groups = mongo.db.groups
    output = []
    for x in groups.find():
        output.append({'name': x['name'], 'no_of_members': x['no_of_members']})
    return jsonify({'result': output})


@app.route('/groups/', methods=['GET'])
def get_one_group(name):
    groups = mongo.db.groups
    x = groups.find_one({'name': name})
    if x:
        output = {'name': x['name'], 'no_of_members': x['no_of_members']}
    else:
        output = "No such name"
    return jsonify({'result': output})


@app.route('/groups', methods=['POST'])
def add_star():
    groups = mongo.db.groups
    name = request.json['name']
    no_of_members = request.json['no_of_members']
    id = groups.insert({'name': name, 'no_of_members': no_of_members})
    new = groups.find_one({'_id': id})
    output = {'name': new['name'], 'no_of_members': new['no_of_members']}
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)
