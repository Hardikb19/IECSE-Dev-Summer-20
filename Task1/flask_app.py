
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

data = {
    "chakshu" : {
        "email" : "chakshusaraswat@gmail.com",
        "contact": 9934127828,
        "branch" : "CCE",
        "gpa" : 8.91,
        "roll no" : 85
    },
    "jeet" : {
        "email":"jeetsmehta13@gmail.com",
        "contact" : 7990644046,
        "branch" : "CSE",
        "gpa" : 8.5,
        "roll no" : 45
    },
    "nitigya" : {
        "email" : "kapoornitigya@gmail.com",
        "contact" : 9999259584,
        "branch" : "ECE",
        "gpa" : 9.09,
        "roll no" : 96
    },
    "hardik" : {
        "email" : "hardikbharunt@gmail.com",
        "contact": 8777089724,
        "branch" : "IT",
        "gpa" : 9.3,
        "roll no" : 27
    }
}

@app.route('/')
def hello_world():
    return '<html>Available routes: <b>/all /name /email<b></html>'

@app.route('/all', methods=["GET","POST"])
def all_details():
    content= request.get_json()
    if (request.method=="POST"):
        if "name" in content:
            try:
                name=content["name"]
                if name in data:
                    ret = {}
                    ret["name"]=name
                    ret["email"]=data[name]["email"]
                    ret["contact"]=data[name]["contact"]
                    ret["branch"]=data[name]["branch"]
                    ret["gpa"]=data[name]["gpa"]
                    ret["roll no"]=data[name]["roll no"]
                    return Response(json.dumps(ret), status=200, mimetype='application/json')
                else:
                    return Response("Name not found", status=200, mimetype='application/json')
            except:
                return Response(status = 400, mimetype='application/json' )
        return Response(status = 404, mimetype='application/json' )
    elif (request.method=="GET"):
        return '<html><h1>All details</h1><body>Send a POST request</body></html>'

@app.route("/name", methods=["GET","POST"])
def two():
    content= request.get_json()
    if (request.method=="POST"):
        if "name" in content:
            try:
                name=content["name"]
                if name in data:
                    ret = {}
                    ret["name"]=name
                    ret["email"]=data[name]["email"]
                    return Response(json.dumps(ret), status=200, mimetype='application/json')
                else:
                    return Response("Name not found", status=200, mimetype='application/json')
            except:
                return Response( "{\"success\":\"false\"}" , status = 200, mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200, mimetype='application/json' )
    elif (request.method=="GET"):
        return '<html><h1>Name and Email details</h1><body>Send a POST request</body></html>'

@app.route("/email", methods=["GET","POST"])
def email():
    content= request.get_json()
    if (request.method=="POST"):
        if "name" in content:
            try:
                name=content["name"]
                if name in data:
                    ret = {}
                    ret["email"]=data[name]["email"]
                    return Response(json.dumps(ret), status=200, mimetype='application/json')
                else:
                    return Response("Name not found", status=200, mimetype='application/json')
            except:
                return Response( "{\"success\":\"false\"}" , status = 200, mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200, mimetype='application/json' )
    elif (request.method=="GET"):
        return '<html><h1>Email details</h1><body>Send a POST request</body></html>'

if __name__ == '__main__':
    app.run()