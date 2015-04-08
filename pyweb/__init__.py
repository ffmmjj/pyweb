from flask import Flask, g, request, session, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from models.user import User

app = Flask(__name__)
app.config.from_object('config')

from pyweb import views

def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        if (user_id):
        	return User(user_id)
        else:
        	return None

init_login()
