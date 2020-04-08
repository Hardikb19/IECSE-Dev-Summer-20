from flask import Flask, request , Response, jsonify, json

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

                    #print(ret)

                    # return jsonify(json.dumps(ret))
                    return Response(json.dumps(ret) ,
                    status = 200 , mimetype='application/json')
                else:
                    return Response( "{\"success\":\"false\"}" ,
                        status = 200 , mimetype='application/json' )
            except:
                return Response( "{\"success\":\"false\"}" ,
                    status = 200 , mimetype='application/json' )
        return Response( "{\"success\":\"false\"}" , status = 200 ,
            mimetype='application/json' )
    elif(request.method == 'GET'): # Checks if it is a get request
        return 
        '<html><head><title>Get Request</title></head><body></body></html>' 
#returns an html doc to render



if __name__ == '__main__':
    app.run(debug=True)