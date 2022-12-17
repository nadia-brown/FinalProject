Users can clone files 

Users can test Passwordcheck using '{"email" : "foo@bar"}' -X POST http://localhost:9000/check -H "Content-type: application/json"

Users can test Emailcheck using curl -d '{ "password" : "xxxxxxxx" }" -X POST http://localhost:9001/check  -H "Content-type: application/json"

Users can test addRole using curl -d '{ "email" : "user_email", "newRole" : "role_to_add" }' -X POST http://localhost:9003/addrole  -H "Content-type: application/json"

Users can test removeRole using curl -d '{ "email" : "user_email", "remove_role" : "role_to_delete" }' -X POST http://localhost:9003/removerole  -H "Content-type: application/json"

Users can test addUser using curl -d '{ "user" :  "username"}' -X POST http://localhost:9002/adduser -H "Content-type: application/json"

Users can test removeUser curl -d '{"user" : "username", }' -X POST http://localhost:9002/removeuser  -H "Content-type: application/json"

Functional Tests: 
Emailcheck

curl -d ‘{“email”: “nadia@gmail.com"}' -X POST http://localhost:9000/check -H “Content-type: application/json”  

Passwordcheck

curl -d ‘{“password”: “abcdef”}’ -X POST http://localhost:9001/check -H “Content-type: application/json”  

Roles

curl -d ‘{“user” :  “nadiab”}' -X POST http://localhost:9003/adduser -H “Content-type: application/json”

curl -d ‘{“user” : “nadiab”, }' -X POST http://localhost:9003/removeuser  -H “Content-type: application/json”


Authorize 
curl -d '{“user” :  “nadiab”}’ -X POST http://localhost:9002/adduser -H “Content-type: application/json”
