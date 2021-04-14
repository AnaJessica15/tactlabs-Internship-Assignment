#Saving a file

from flask import Flask,request,url_for
from flask_pymongo import PyMongo

app = flask.Flask(_name_)
app.config['MONGO_URI'] = 'mongodb+srv://aj_15:**********@cluster0.pdcrn.mongodb.net/aj?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def index():
    return '''
        <h1>Save file</h1>
        <form method="POST" action="/save-file" enctype="multipart/form-data">
            <label for="name">Name</label>
            <input type="text" name="name" id="name">
            <input type="file" name="new_file"><br><br>
            <input type="submit">
        </form>
    '''
@app.route('/save-file', methods=['POST'])
def save_file():
    if 'new_file' in request.files:
        new_file = request.files['new_file']
        mongo.save_file(new_file.filename, new_file)
        data = {'Name' : request.values.get('name'), 'File Name' : new_file.filename}
        db_operations.insert(data)
        return redirect('/')
