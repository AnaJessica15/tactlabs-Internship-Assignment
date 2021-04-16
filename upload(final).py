#Importing necessary packages
from flask import Flask,render_template,request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os

#Connecting MongoDB to native drive Python
app = Flask(__name__)
app.config["MONGO_URI"] ='mongodb+srv://aj_15:*********@cluster0.pdcrn.mongodb.net/aj?retryWrites=true&w=majority'
mongo = PyMongo(app)

#Locating the database and the collection in MongoDB to upload the files
cluster = MongoClient("mongodb+srv://aj_15:**********@cluster0.pdcrn.mongodb.net/aj?retryWrites=true&w=majority")
db = cluster["TactInternship"]
collection = db["TactInternship"]

#Uploading files via html
@app.route("/upload_file",methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            f.save(os.path.join(app.config['MONGO_URI'],f.filename))
        return render_template("upload-file.html", msg="File has been uploaded successfully")
    return render_template("upload-file.html", msg="Please choose a file")
if __name__ == '__main__':
    app.run(debug=True)
