#Importing necessary packages
from flask import Flask,render_template,request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo
import os

#Connecting MongoDB to native drive Python
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#Locating the database and the collection in MongoDB to upload the files
MONGO_URI='mongodb://127.0.0.1:5000'
client = pymongo.MongoClient(MONGO_URI)
DB = client['TactInternship']
images = DB.images

#Uploading files via html
@app.route("/upload_file",methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            f.save(os.path.join(APP_ROOT['MONGO_URI'],f.filename))
        return render_template("upload-file.html", msg="File has been uploaded successfully")
    return render_template("upload-file.html", msg="Please choose a file")
if __name__ == '__main__':
    app.run(debug=True)
