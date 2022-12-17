from flask import request, Flask
import json, socket

import sys
sys.path.insert(0,"..")

import my_imports.top

app = Flask(__name__)

authorized_users = {}

#
# curl http://localhost:9002
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)


#
# curl -d "{ \"user\" :  "username" }" -X POST http://localhost:9002/check -H "Content-type: application/json"
#
# @app.route("/username", methods=["POST"])
# def verify():
#     hostName = socket.gethostname()

#     username = request.json['user']

#     returnDictionary = {'Nadia': "Granted", 'WonderPhil':"Granted", "Foo": "Denied"}
#     returnDictionary["username"] = username
    

#     if username in returnDictionary:
#     #     returnDictionary["success"] = True
#     # else:
#     #     returnDictionary["success"] = False 
#         if key in returnDictionary.keys():
#             returnDictionary["success"] = True
#         else:
#             returnDictionary["success"] = False
    
#     return json.dumps(returnDictionary)


#
# curl -d '{ "user" :  "username"}' -X POST http://localhost:9002/adduser -H "Content-type: application/json"
# curl -d '{ "user" :  "nadiab"}' -X POST http://localhost:9002/adduser -H "Content-type: application/json"
#

@app.route("/adduser", methods=["POST"])
def addUser():
   
    user_name = request.json['user']

    if user_name not in authorized_users:
        authorized_users[user_name] = user_name
    else:
        usr_already_authorized = authorized_users[user_name]
        if user_name not in usr_already_authorized:
            usr_already_authorized += [user_name]
    
    return json.dumps(authorized_users)


# curl -d '{"user" : "username", }' -X POST http://localhost:9002/removeuser  -H "Content-type: application/json"
#
@app.route("/removeuser", methods=["POST"])
def removeUser():
    user_name = request.json["user"]

    if user_name in authorized_users:
            authorized_users[user_name].remove(user_name)

    return json.dumps(authorized_users)

 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)