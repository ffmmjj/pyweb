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
from services.nlp_service import NLPService
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
        db = MongoInit().initialize()
        messageService = MessageService(db)
        messages = messageService.getMessagesByUserByPage(user.id, 0, 50)
        return render_template("index.html",
                               title='Home',
                               user=user,
                               messages=messages)

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
    
    payload = { 'fileId': request.json['fileId'], 'data': request.json['data'], 'position': request.json['position'], 'user': get_current_user().id }

    fileService = FileService(db)
    
    file = fileService.processFileChunk(None, payload['fileId'], payload['user'], payload['data'], payload['position'])
    
    return make_response(jsonify({'fileId': file._id, 'position': file.position}), 201)

@app.route('/api/file/process', methods=['POST'])
def process_file():
    if not request.json or not request.json['fileId']:
        requestData = request.json or str(request.form) or request.data
        return make_response('Invalid content: ' + requestData, 400)

    db = MongoInit().initialize()

    payload = { 'fileId': request.json['fileId'], 'user': get_current_user().id }

    fileService = FileService(db)
    messageService = MessageService(db)
    
    chunks = fileService.getChunksByFileId(payload['fileId'])

    messages = []
    if all(c.user == payload['user'] for c in chunks):
        messages = messageService.parseFileChunks(chunks)

    topMessages = []

    for message in messages[:50]:
        topMessages.append({'subject': message.subject, 'sender': message.sender, 'content': message.content, 'date': message.date})

    result = {'fileId': payload['fileId'], 'messages': topMessages}

    return make_response(jsonify(result))

@app.route('/api/messages/<id>', methods=['GET'])
def get_message(id):
    db = MongoInit().initialize()
    
    messageService = MessageService(db)
    
    message = messageService.getMessageById(id)
    
    result = {'subject': message.subject, 'sender': message.sender, 'content': message.content, 'date': message.date}
    
    return make_response(jsonify(result), 200)

@app.route('/api/messages/clusters/<userId>', methods=['GET'])
def get_clusters(userId):
    db = MongoInit().initialize()
    messageService = MessageService(db)
    messages = messageService.getMessagesByUser(userId)

    nlpService = NLPService()
    clusters = nlpService.processMessages(messages)

    result = []

    for key, values in clusters.iteritems():
        clusterId = int(key)
        clusteredMessages = [{'subject': v.subject, 'sender': v.sender, 'content': v.originalContent, 'date': v.date} for v in values[:10]]
        cluster = {'clusterId': clusterId, 'messages': clusteredMessages}
        result.append(cluster)
    
    return make_response(jsonify({'clusters':result}), 200)