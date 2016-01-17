from flask import render_template, redirect, g, request, session, url_for, flash, request, abort, make_response, jsonify
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from pyweb import app
from forms.login_form import LoginForm
from models.user import User
from models.message import Message
from models.fileChunk import FileChunk
from services.user_service import UserService
from services.message_service import MessageService
from services.file_service import FileService
from mongo_init import MongoInit
import logging


def get_current_user():
    if (current_user.is_authenticated()):
        return current_user
    else:
        return None

def set_current_user(user):
    current_user = user

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/')
@app.route('/index')
def index():
    user = get_current_user()
    if user == None:
        return redirect('/login',302)
    else:
        return render_template("index.html",
                               title='Home',
                               user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if get_current_user() is None:
        error = None

        db = MongoInit().initialize()
        
        if request.method == 'POST':            
            user = UserService(db).load_user_by_login(request.form['login'])
            
            if user is None:
                error = 'Invalid username or password'
            elif user.password != request.form['password']:
                error = 'Invalid username or password'
            else:
                login_user(user)
                set_current_user(user)
                return redirect(url_for('index'))

        
        return render_template('login.html', error=error, form=form)

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/api/file', methods=['POST'])
def create_file():
    if not request.json or not request.json['data']:
        requestData = request.json or str(request.form) or request.data
        return make_response('Invalid content: ' + requestData, 400)

    db = MongoInit().initialize()
    
    payload = { 'fileId': request.json['fileId'], 'data': request.json['data'], 'user': get_current_user().id }

    fileService = FileService(db)
    
    file = fileService.processFileChunk(None, payload['fileId'], payload['data'], payload['user'])
    
    return make_response(jsonify({'fileId': file._id, 'data': file.data}), 201)
