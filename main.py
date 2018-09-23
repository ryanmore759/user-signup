from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/user-signup", methods=['POST', 'GET'])
def user_signup():
    return render_template('sign-up.html')