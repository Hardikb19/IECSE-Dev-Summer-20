from flask import Flask, request , Response, jsonify
import json

app = Flask(__name__)

data = {
    "name1" : {
        "email" : "name1@gmail.com",
        "contact" : "1111111111",
        "city" : "Manipal",
        "college" : "MIT",
        "age" : "18",
        "course" : "CSE"
    },
    "name2" : {
        "email" : "name2@gmail.com",
        "contact" : "2222222222",
        "city" : "Manipal",
        "college" : "MIT",
        "age" : "19",
        "course" : "IT"
    },
    "name3" : {
        "email" : "name3@gmail.com",
        "contact" : "3333333333",
        "city" : "Chennai",
        "college" : "IIT",
        "age" : "19",
        "course" : "CSE"
    },
    "name4" : {
        "email" : "name4@gmail.com",
        "contact" : "4444444444",
        "city" : "Mumbai",
        "college" : "IIT",
        "age" : "19",
        "course" : "CSE"
    }
}

@app.route('/all',methods=['POST','GET'])
def test_allRoute():
    content = request.get_json()#holds the request body
    if(request.method == 'POST'): #checks if its a POST request
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["name"] = name
                    ret["email"] = data[name]["email"]
                    ret["contact"] = data[name]["contact"]
                    ret["age"] = data[name]["age"]
                    ret["college"] = data[name]["college"]
                    ret["course"] = data[name]["course"]
                    ret["success"] = True
                    return Response( json.dumps(ret) , status = 200 , mimetype='application/json')
                else:
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method == 'GET'): # Checks if it is a get request
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1></body></html>' 
#returns an html doc to render

@app.route('/name',methods=['POST','GET'])
def test_nameRoute():
    content = request.get_json()#holds the request body
    if(request.method == 'POST'): #checks if its a POST request
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["name"] = name
                    ret["email"] = data[name]["email"]
                    ret["success"] = True
                    return Response( json.dumps(ret) , status = 200 , mimetype='application/json')
                else:
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method == 'GET'): # Checks if it is a get request
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1></body></html>' 
#returns an html doc to render

@app.route('/email',methods=['POST','GET'])
def test_emailRoute():
    content = request.get_json()#holds the request body
    if(request.method == 'POST'): #checks if its a POST request
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["email"] = data[name]["email"]
                    ret["success"] = True
                    return Response( json.dumps(ret) , status = 200 , mimetype='application/json')
                else:
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method == 'GET'): # Checks if it is a get request
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1></body></html>' 
#returns an html doc to render

if __name__ == '__main__':
    app.run(debug=True)