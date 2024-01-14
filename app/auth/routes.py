from . import auth
from flask import render_template

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('auth/signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')