from flask import Flask, request , Response, jsonify
import json

app = Flask(__name__)

data = {
    "nishika" : {
        "email" : "nishika991@gmail.com",
        "contact" : "9910517874",
        "city" : "gurgaon",
        "Age" : "18",
        "course" : "IT"

    },

    "pragnya" : {
        "email" : "pragnya.deshpande@gmail.com",
        "contact" : "7032637335",
        "city" : "hyderabad",
        "Age" : "19",
        "course" : "IT"

    },

    "angad" : {
        "email" : "angad.sandhu@gmail.com",
        "contact" : "7011324657",
        "city" : "gurgaon",
        "Age" : "19",
        "course" : "CSE"

    }
    
}
@app.route('/all',methods=['POST','GET'])
def test1():
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
                    ret["city"] = data[name]["city"]
                    ret["Age"] = data[name]["Age"]
                    ret["course"] = data[name]["course"]
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
def test2():
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
def test3():
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
    app.run(debug=True)

