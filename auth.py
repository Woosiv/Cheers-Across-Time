from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

# Login Page
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if verifyLogin(user, password):
            print('correct user login')
            return redirect(url_for('main.root', username = user))
        else:
            print('failed login')
            return redirect(url_for('auth.login'))
    else:
        return render_template("login.html")

# Verifies the login with the database
def verifyLogin(username, password):
    return username != 'fail'

@auth.route('/signup')
def signup():
    pass


