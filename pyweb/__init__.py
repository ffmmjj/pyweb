from flask import Flask, g, request, session, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from flask.ext.mongoengine import MongoEngine
from models.user import User
from services.user_service import UserService

app = Flask(__name__)
app.config.from_object('config.Config')

#db = MongoEngine(app)

from pyweb import views

def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)
    UserService.initialize_users()

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        if (user_id):
        	return User(user_id)
        else:
        	return None

init_login()
