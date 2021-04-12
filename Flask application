pip install flask
pip install flask-pymongo
pip install dnspython

from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "<mongodb+srv://aj_15:6385715202@cluster()-jtpxd.mongodb.net/admin>"
mongo = PyMongo(app)

@app.route('/test')
def test():
    return "App is working perfectly"
    
if __name__ == '__main__':
app.run(debug=True)
