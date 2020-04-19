from flask import Flask, Response, jsonify, Request, request
import json
from flask_pymongo import PyMongo
import hashlib
import logging,os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restydb'

mongo = PyMongo(app)

logging.basicConfig(filename="users.log", 
                    format='%(asctime)s %(levelname)s : %(message)s', 
                    filemode='w', level=logging.DEBUG)

@app.route('/')
def home():
    app.logger.info('Homepage returned')
    return "<h1>Send authentication details</h1>"

@app.route('/signup', methods=["POST"])
def signup():
    df_pass=mongo.db.sec
    data= request.get_json()
    if "username" in data and "password" in data:
        if data["username"]=="" or data["password"]=="":
            app.logger.error('No data sent')
            return jsonify("Empty field(s)")
        else:
            username=data["username"]
            password=data["password"]
            temp = df_pass.find_one({'username': username})
            if temp:
                app.logger.error('User %s already exists',username)
                return jsonify("Username already taken")
            else:
                salt=os.urandom(32)
                key=hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
                df_pass.insert({'username': username, 'key': key, 'salt':salt})
                app.logger.info('%s user created',username)
                return jsonify({'Success': "User successfully created"})
    else:
        app.logger.warning("Wrong input format")
        return jsonify({'Error': "Send credentials in 'username' and 'password' format"})
    
@app.route('/login', methods=["POST"])
def login():
    df=mongo.db.sec
    datA=request.get_json()
    if "username" and "password" in datA:
        if datA["username"]=="" or datA["password"]=="":
            app.logger.error('No data sent')
            return jsonify("Empty field(s)")
        else:
            username=datA["username"]
            password=datA["password"]
            temp = df.find_one({'username': username})
            if temp:
                salt=temp["salt"]
                key=temp["key"]
                new_key=hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
                if new_key==key:
                    app.logger.info('User authentication successful')
                    out="True"
                else:
                    app.logger.info('Incorrect credentials')
                    out="False"
                return jsonify(out)
            else:
                app.logger.error('No such user')
                return jsonify("Username does not exist")
    else:
        app.logger.warning("Wrong input format")
        return jsonify("Send credentials in \"username\" and \"password\" format")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)