from flask import Flask, request , Response, jsonify

app = Flask(__name__)

data = {
    "chakshu" : {
        "email" : "chakshusaraswat@gmail.com",
        "contact": 9934127828
    },
    "jeet" : {
        "email":"jeetsmehta13@gmail.com",
        "contact" : 7990644046
    },
    "nitigya" : {
        "email" : "kapoornitigya@gmail.com",
        "contact" : 9999259584
    },
    "hardik" : {
        "email" : "hardikbharunt@gmail.com",
        "contact": 8777089724
    }
}

@app.route('/check',methods=['POST','GET'])
def test():
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
        return '<html><head><title>Get Request</title></head><body><h1>I got a GET Request</h1></body></html>' 




if __name__ == '__main__':
    app.run(debug=True)
