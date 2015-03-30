import sqlite3
from flask import render_template, redirect, g, request, session, url_for, flash
from app import app

def get_current_user():
    return session.get('logged_in')

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
    error = None
    users_query = g.db.execute('select id, username, password from users')
    users = [dict(id=row[0], username=row[1], password=row[2]) for row in users_query.fetchall()]

    if request.method == 'POST':
        if request.form['username'] not in [user['username'] for user in users]:
            error = 'Invalid username or password'
        elif request.form['password'] != [user['password'] for user in users if user['username'] == request.form['username']][0]:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            session['user_nickname'] = request.form['username']
            user = dict(nickname=session.get('user_nickname'))
            return render_template('index.html', user=user)

    return render_template('login.html', error=error)
