from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_mysql_connector import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from chat import get_response

from config import config

# Models
from models.ModelUser import ModelUser

# Entities
from models.entities.User import User

app=Flask('__name__')

# csrf=CSRFProtect()
db=MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/')
def index():
    session['username']=None
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html',var='home')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user!= None:
            if logged_user.password:
                login_user(logged_user)
                session['username']=request.form['username']
                return redirect(url_for('home'))
            else:
                flash("Invaloid password ...")
                return render_template('sign.html',var='sign')
        else:
            flash("User not found")
            return render_template('sign.html',var='sign')
    else:
        return render_template('sign.html',var='sign')
    
@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    session['username']=None
    return redirect(url_for('home'))

@app.route('/sign', methods=['GET','POST'])
def sign():
    if request.method=='POST':
        if request.form['username_sign']=='' or request.form['password_sign']=='' or request.form['fullname_sign']=='':
            return render_template('sign.html',var='sign')
        user=User(None,request.form['username_sign'],request.form['password_sign'],request.form["fullname_sign"])
        check=ModelUser.check_exist(db,user)
        if check:
            logged_user=ModelUser.sign(db,user)
            if logged_user:
                flash("INSERT added successfully!")
                return render_template('sign.html',var='sign')
            else:
                flash("An error occurred while committing to the database:")
                return render_template('sign.html',var='sign')
        else:
            flash("Username aleredy exist")
            return render_template('sign.html',var='sign')
    else:
        return render_template('sign.html',var='sign')
   

@app.route('/chat')
def chat():
    # if session['username']==None:
    #     return render_template('sign.html',var='sign')
    return render_template('chat.html',var='chat')

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()
