
from flask import Flask, request , Response, json

app = Flask(__name__)

data = {
    "A" : {
        "email" : "A@a.com",
        "contact" : "1234",
        "gender" : "male",
        "DOB" : "10-7-2005",
        "POB" : "Australia"
        },
    "B" : {
        "email" : "B@b.com",
        "contact" : "5678",
        "gender" : "female",
        "DOB" : "13-2-1992",
        "POB" : "earth"
        },
    "C" : {
        "email" : "C@c.net",
        "contact" : "0000",
        "gender" : "other",
        "DOB" : "22-9-2145",
        "POB" : "uranus"
        },
    "D" : {
        "email" : "D@d.org",
        "contact" : "42069",
        "gender" : "unknown",
        "DOB" : "8-11-1439",
        "POB" : "space"
        }
    }

@app.route('/name',methods=['POST','GET'])
def name():
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
        return '<html><head><title>Get Page</title></head><body><h2>This is the get page</h2><p>try putting A, B, C or D as name when posting</p></body></html>'

@app.route('/all',methods=['POST','GET'])
def all():
    content = request.get_json()
    if(request.method == 'POST'):
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["name"] = name
                    ret["email"] = data[name]["email"]
                    ret["contact"] = data[name]["contact"]
                    ret["gender"] = data[name]["gender"]
                    ret["date of birth"] = data[name]["DOB"]
                    ret["place of birth"] = data[name]["POB"]
                    ret["success"] = True
                    return Response( json.dumps(ret) , status = 200 , mimetype='application/json')
                else:
                    return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method == 'GET'):
        return '<html><head><title>Get Page</title></head><body><h2>This is the get page</h2><p>try putting A, B, C or D as name when posting</p></body></html>'


@app.route('/email',methods=['POST','GET'])
def email():
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
        return '<html><head><title>Get Page</title></head><body><h2>This is the get page</h2><p>try putting A, B, C or D as name when posting</p></body></html>'


if __name__ == '__main__':
    app.run(debug=True)
