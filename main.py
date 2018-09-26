from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def display_username():
    return render_template('sign_up.html')

@app.route('/validate-username',methods=['POST'])
def validate_username():
    username= request.form['user-name']
    


         
    return redirect('/valid-username?username={}'.format(username))
 

@app.route('/valid-username')
def valid_username():
    username = request.args.get('username')
    return '<h1>g {0} </h1>'.format(username)




app.run()