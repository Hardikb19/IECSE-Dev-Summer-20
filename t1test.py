from flask import Flask, request , Response, jsonify
import json

app = Flask(__name__)

data = {
    "prabhat" : {
        "email" : "prabhat@gmail.com",
        "Contact" : "9987540623",
        "City" : "Mumbai",
        "Age" : "18",
        "Course" : "CSE"

    },

    "raj" : {
        "email" : "raj@gmail.com",
        "Contact" : "9163040623",
        "City" : "Chittor",
        "Age" : "19",
        "Course" : "Civil"

    },

    "rekha" : {
        "email" : "rekha@gmail.com",
        "Contact" : "9987590077",
        "City" : "Bhilwara",
        "Age" : "19",
        "Course" : "Chemical"

    }

}
@app.route('/all',methods=['POST','GET'])
def testall():
    content = request.get_json()
    if(request.method == 'POST'):
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["name"] = name
                    ret["email"] = data[name]["email"]
                    ret["Contact"] = data[name]["Contact"]
                    ret["City"] = data[name]["City"]
                    ret["Age"] = data[name]["Age"]
                    ret["Course"] = data[name]["Course"]
                    ret["success"] = True
                    return Response( json.dumps(ret) , status = 200 , mimetype='application/json')
                else:
                    return Response( "{\"success\":\"name not in data\"}" , status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"try failed\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"name in content\"}" , status = 200 , mimetype='application/json' )
    elif(request.method == 'GET'):
        return '<html><head><title>Get Request</title></head><body><h1>GET Request</h1></body></html>'



@app.route('/name',methods=['POST','GET'])
def testnc():
    content = request.get_json()
    if(request.method == 'POST'):
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
    elif(request.method == 'GET'):
        return '<html><head><title>Get Request</title></head><body><h1>GET Request</h1></body></html>'


@app.route('/email',methods=['POST','GET'])
def testemail():
    content = request.get_json()
    if(request.method == 'POST'):
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
    elif(request.method == 'GET'):
        return '<html><head><title>Get Request</title></head><body><h1>GET Request</h1></body></html>'




if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)
