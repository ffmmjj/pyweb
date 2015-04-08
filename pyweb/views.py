from flask import render_template, redirect, g, request, session, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from pyweb import app
from forms.login_form import LoginForm
from models.user import User

def get_current_user():
    if (current_user.is_authenticated()):
        return current_user
    else:
        return None

def set_current_user(user):
    current_user = user

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
        
        users = [{'username':'valid_user', 'password':'valid_password'}]

        if request.method == 'POST':
            if request.form['login'] not in [user['username'] for user in users]:
                error = 'Invalid username or password'
            elif request.form['password'] != [user['password'] for user in users if user['username'] == request.form['login']][0]:
                error = 'Invalid username or password'
            else:
                user = User(request.form['login'])
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
