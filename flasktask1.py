from flask import Flask, request, response, jsonify
app = Flask(__name__)
data ={
    "ram":{
        "email":"ram2000@gmail.com",
        "contact":9845645419,
        "home":"chandigarh",
        "age":14,
        "eyecolor":"blue"
        },
    "shyam":{
        "email":"shyamlal2345@gmail.com",
        "contact":8956443210,
        "home":"nepal",
        "age":17,
        "eyecolor":"brown"
    },
    "tani":{
        "email":"tani3001@gmail.com",
        "contact":7884294013,
        "home":"mumbai",
        "age":19,
        "eyecolor":"hazel"
    }
}
@app.route('/all',methods=['POST','GET'])
def alltest():
    content=request.get_json()
    if(request.method == 'POST'):
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["name"] = name
                    ret["email"] = data[name]["email"]
                    ret["contact"] = data[name]["contact"]
                    ret["home"] = data[name]["home"]
                    ret["age"] = data[name]["age"]
                    ret["eyecolor"] = data[name]["eyecolor"]
                    ret["success"] = True
                    return Response( json.dumps(ret), status=200, mimetype='application/json')
                else:
                    return Response("{\"success\":\"false\"}", status=200, mimetype='application/json')
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method =='GET'):
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request...</h1></body></html>'

@app.route('/name', methods=['POST','GET'])
def nametest():
    content=request.get_json()
    if(request.method == 'POST'):
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["name"] = name
                    ret["email"] = data[name]["email"]
                    ret["success"] = True
                    return Response( json.dumps(ret), status=200, mimetype='application/json')
                else:
                    return Response("{\"success\":\"false\"}", status=200, mimetype='application/json')
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method =='GET'):
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request...</h1></body></html>'
@app.route('/email', methods=['POST','GET'])
def emailtest():
    content=request.get_json()
    if(request.method == 'POST'):
        if "name" in content:
            try:
                name = content["name"]
                if name in data:
                    ret = {}
                    ret["name"] = name
                    ret["success"] = True
                    return Response( json.dumps(ret), status=200, mimetype='application/json')
                else:
                    return Response("{\"success\":\"false\"}", status=200, mimetype='application/json')
            except:
                return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 , mimetype='application/json' )
    elif(request.method =='GET'):
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request...</h1></body></html>'
if __name__=='__main__':
    app.run(debug=True)
