from flask import Flask, request , Response, jsonify
import os
import json
app = Flask(__name__)

data = {
    "chakshu" : {
        "email" : "chakshusaraswat@gmail.com",
        "contact": 9934127828,
        "id":7777,
        "block":15,
        "college":"MIT"
    },
    "jeet" : {
        "email":"jeetsmehta13@gmail.com",
        "contact" : 7990644046,
        "id":7778,
        "block":14,
        "college":"MSAP"
    },
    "nitigya" : {
        "email" : "kapoornitigya@gmail.com",
        "contact" : 9999259584,
        "id":7779,
        "block":15,
        "college":"MCOPS"
    },
    "hardik" : {
        "email" : "hardikbharunt@gmail.com",
        "contact": 8777089724,
        "id":7780,
        "block":14,
        "college":"KMC"
    }
}
@app.route('/')
def index():
    return ' Hello world '


@app.route('/check',methods=['POST','GET'])
def test():
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
                    print("else")
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                print("Except")
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        else:
            print("outermost else")

            return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif (request.method == 'GET'): # Checks if it is a get request
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1></body></html>'
#returns an html doc to render

@app.route('/all',methods=['POST','GET'])
def alldetails():
    content1 = request.get_json()
    if(request.method == 'POST'):
        if "name" in content1:
            try:
                name = content1["name"]
                if name in data:
                    ret={}
                    ret["name"] = name
                    ret["email"] = data[name]["email"]
                    ret["contact"] = data[name]["contact"]
                    ret["id"] = data[name]["id"]
                    ret["College"] = data[name]["college"]
                    ret["Block"] = data[name]["block"]
                    ret["success"] = True
                    return Response(json.dumps(ret) , status = 200 , mimetype='application/json')
                else:
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method == 'GET'): # Checks if it is a get request
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1><p>Use POST request with a specific name to get all data</p></body></html>'


@app.route('/name',methods=['POST','GET'])
def nameget():
    content2 = request.get_json()
    if(request.method == 'POST'):
        if "name" in content2:
            try:
                name = content2["name"]
                if name in data:
                    ret={}
                    ret["name"] = name
                    #ret["email"] = data[name]["email"]
                    ret["success"] = True
                    return Response(json.dumps(ret) , status = 200 , mimetype='application/json')
                else:
                    #print("Fail1")
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                #print("Fail2")
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        #print("Fail")
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method == 'GET'): # Checks if it is a get request
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1><p>Use POST request with a specific name to get name data</p></body></html>'

@app.route('/email',methods = ['POST','GET'])
def names():
    content3 = request.get_json()
    if(request.method == 'POST'):
        if "name" in content3:
            try:
                name = content3["name"]
                if name in data:
                    ret={}
                    ret["email"] = data[name]["email"]
                    ret["success"] = True
                    return Response(json.dumps(ret), status = 200, mimetype='application/json')
                else:
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json')
    elif(request.method == 'GET'): # Checks if it is a get request
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1><p>Use POST request with a specific name to get email data</p></body></html>'

if __name__ == '__main__':
    port1 = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0' , port=port1)
