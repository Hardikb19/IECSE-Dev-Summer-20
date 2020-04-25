from flask import Flask, Response, jsonify, Request, request
#import json
from flask_pymongo import PyMongo
import wikipedia
import redis
#import logging

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'task3db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/task3db'

mongo = PyMongo(app)

@app.route('/request', methods=['POST'])
def query():
    df_app=mongo.db.wiki
    r=redis.StrictRedis(decode_responses=True)
    data_raw=request.get_json()
    if data_raw:
        data=data_raw['find']
        out=r.get(data)
        if out:
            return jsonify(out)
        else:
            out=df_app.find_one({'key': data})
            if out:
                r.set(data,out,86400)
                return jsonify(out)
            else:
                out=wikipedia.WikipediaPage(title=data).summary
                if out:
                    r.set(data,out,86400)
                    df_app.insert({'key': data, 'value': out})
                    return jsonify(out)
                else:
                    return jsonify("No info available")
    else:
        return jsonify("Send data")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)