from flask import Flask,request,render_template
import os
import uuid

''' aplication modules '''
from Bussiness import bussiness

app = Flask(__name__)


@app.route('/',methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/logout',methods=['GET'])
def logout_page():
    return render_template('login.html')

@app.route('/home-page',methods=['POST'])
def home_page():

    userName = request.form['username']
    password = request.form['password']

    if bussiness._login(userName= userName,password=password):
        return render_template('home.html')
    else:
        return render_template('login.html',info='Invalid Data')

@app.route('/file-upload',methods= ['POST'])
def file_upload():
    name = request.files['file'].filename
    file = request.files['file']

    guid = str(uuid.uuid4())

    path = os.getcwd()+"/files/"+ guid+"/"

    if not os.path.exists(path):
        os.makedirs(path)
        file.save(path+"/"+name)
    else:
        file.save(path+"/"+name)

    if bussiness.fileupload(guid,path,name) != "":
        ''' success html'''
        return render_template('upload.html',status='File successfully uploaded',guids = guid)
    else:
        return render_template('uploadFail.html',status='Upload failed')

@app.route('/result',methods=['GET'])
def result():
    #guid = request.form['guid']
    guid = request.args.get('guids')

    image_path = bussiness.process_check(guid)
    if image_path == "":
       return render_template('upload.html',status='File successfully uploaded',guids = guid)
    else:
        return render_template('results.html',source_image_path=image_path)

if __name__ == '__main__':
    app.run()
