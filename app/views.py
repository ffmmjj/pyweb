from flask import render_template, redirect
from app import app

def get_current_user():
    return None

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

@app.route('/login')
def login():
    return render_template('login.html',
                            user=None)