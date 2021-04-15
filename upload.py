from flask import Flask,render_template,request
import os

app = Flask(__name__)

app.config["UPLOAD_PATH"] ='mongodb+srv://aj_15:6385715202@cluster0.pdcrn.mongodb.net/aj?retryWrites=true&w=majority'

@app.route("/upload_file",methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            f.save(os.path.join(app.config['UPLOAD_PATH'],f.file_name))
        return render_template("upload-file.html",msg="File has been uploaded successfully")
    return render_template("upload-file.html",msg="Please choose a file")
if __name__ == '_main_':
    app.run(debug=True,host='0.0.0.0')
