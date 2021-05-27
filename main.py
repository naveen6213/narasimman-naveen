#import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import json
from Bussiness import bussiness
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
#setting the upload folder in local
UPLOAD_FOLDER = "uploads"
#allowed extensions for the file upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

#check for the allowed file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_flow():
    #request_data = json.loads(request.data.decode(), strict=False)

    username=request.form['username']
    password=request.form['password']

    login_status = {"messgage": "User not exist", "status": False}
    
    # username = request_data['username'].strip()
    # password = request_data['password'].strip()

    if username == "shiva" and password == "test@123":
    #if bussiness._login(username,password):
        #login_status = {"messgage": "User exist", "status": True}
        return render_template('home.html',name=username)
    else:
        #login_status = {"messgage": "User not exist", "status": False}
        return render_template('login.html',info='Invalid Data')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload_status.html',status='No file part')
            
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('upload_status.html',status='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return render_template('upload_status.html',status='File uploaded successfully')

if __name__ == '__main__':    
    app.run(debug=True)