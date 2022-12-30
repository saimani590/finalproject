
from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/post',methods=['POST','GET'])
def index():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("app_data.db")
        cursor = connection.cursor()

#Html form
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        confirmpassword=request.form['confirmpassword']

        print(name,username,email,password,confirmpassword)
    return render_template('index.html')
