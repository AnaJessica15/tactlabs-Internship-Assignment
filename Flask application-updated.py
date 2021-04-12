from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://aj_15:<password>@cluster0.pdcrn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/test')
def test():
    return "App is working perfectly"

db_operations = mongo.db.users

#CRUD Operations
#Create
@app.route('/create')
def create():
    new_user = {'Name' : 'xyz', 'Age' : 20}
    db_operations.insert_one(new_user)
    result = {'result' : 'Created successfully'}
    return result
@app.route('/create-many')
def create_many():
    new_user_1 = {'Name' : 'xyz1', 'Age' : 10}
    new_user_2 = {'Name' : 'xyz2', 'Age' : 20}
    new_user_3 = {'Name' : 'xyz3', 'Age' : 30}
    new_users = [new_user_1, new_user_2, new_user_3]
    db_operations.insert_many(new_users)
    result = {'result' : 'Created successfully'}
    return result

#Read
@app.route('/read')
def read():
    users = db_operations.find()
    output = [{'Name' : user['Name'], 'Age' : user['Age']} for user in users]
    #print(output)
    return jsonify(output)
@app.route('/read-with-filter')
def read_with_filter():
    filt = {'Name' : 'xyz'}
    users = db_operations.find(filt)
    output = [{'Name' : user['Name'], 'Age' : user['Age']} for user in users]
    #print(output)
    return jsonify(output)
@app.route('/read-one')
def read_one():
    filt = {'Name' : 'xyz'}
    user = db_operations.find_one(filt)
    output = {'Name' : user['Name'], 'Age' : user['Age']}
    #print(output)
    return jsonify(output)
   
if __name__ == '__main__':
app.run(debug=True)
