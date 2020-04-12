from flask import Flask, request, Response, jsonify
import json


app = Flask(__name__)

data = {
    "chakshu" : {
        "email" : "chakshusaraswat@gmail.com",
        "contact": 9934127828,
        "branch" : "CSE",
        "block":15,
        "roll no" : 1
    },
    "jeet" : {
        "email":"jeetsmehta13@gmail.com",
        "contact" : 7990644046,
        "branch" : "CSE",
        "block":14,
        "roll no" : 2
    },
    "nitigya" : {
        "email" : "kapoornitigya@gmail.com",
        "contact" : 9999259584,
        "branch" : "CSE",
        "block":15,
        "roll no" : 3
    },
    "hardik" : {
        "email" : "hardikbharunt@gmail.com",
        "contact": 8777089724,
        "branch" : "CSE",
        "block":15,
        "roll no" : 4
    }
}

#Home Page
@app.route('/')
def home_page():
    return '<html><h2>Check the routes: <h2><b>/all /name /email<b></html>'



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
                    ret["block"]=data[name]["block"]
                    ret["roll no"]=data[name]["roll no"]

                    return Response(json.dumps(ret), status=200, mimetype='application/json')
                else:
                    return Response("Name not found", status=200, mimetype='application/json')
            except:
                return Response(status = 400, mimetype='application/json' )
        return Response(status = 404, mimetype='application/json' )
    elif (request.method=="GET"):
        return '<html><h1>Details</h1><body>This is a GET request. Send a POST request.</body></html>'



@app.route("/name", methods=["GET","POST"])
def name():
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
        return '<html><h1>Name and Email details</h1><body>This is a GET request. Send a POST request.</body></html>'



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
        return '<html><h1>Email details</h1><body>This is a GET request. Send a POST request.</body></html>'




if __name__ == '__main__':
    app.run(debug=True)