#import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
from flasgger import Swagger
import json
from Bussiness import bussiness

app = Flask(__name__)  # Our API url (can of course be a local resource)

swagger = Swagger(app)

@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login/', methods=['POST'])
def login_flow():
    request_data = json.loads(request.data.decode(), strict=False)

    login_status = {"messgage": "User not exist", "status": False}
    
    username = request_data['username'].strip()
    password = request_data['password'].strip()

    if username == "shiva" and password == "test@123":
    #if bussiness._login(username,password):
        login_status = {"messgage": "User exist", "status": True}
    else:
        login_status = {"messgage": "User not exist", "status": False}

    return jsonify(login_status)

if __name__ == '__main__':    
    app.run(debug=True)