from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']=True

sign_up="""
<!doctype html>
    <html>
        <body>
        <form action='/sign-up' method = 'POST'>
            <label>Username: 
                <input id= "user-name" name="user-name" type = "text" value ='{{username}}'/>
            </label>
            <input type="submit"/>
        </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return sign_up

@app.route("/sign-up", methods=['POST'])
def user_signup():
    username= request.form['user-name']
    hello = "hello, {}".format(username)
    return "hhhdhd"






app.run()