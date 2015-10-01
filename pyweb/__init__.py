from flask import Flask, g, request, session, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from models.user import User
from services.user_service import UserService
from mongo_init import MongoInit
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_object('config.Config')

db = MongoInit().initialize()

from pyweb import views

def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)
    user_service = UserService(db)
    user_service.initialize_users()

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        if (user_id):
        	return User(user_id)
        else:
        	return None

def init_logger():
    handler = RotatingFileHandler('yummybox.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

init_login()
init_logger()