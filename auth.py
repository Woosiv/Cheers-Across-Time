from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from models import User
from exts import db

auth = Blueprint('auth', __name__)

# Login Page
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Username or password is incorrect')
            return redirect(url_for('auth.login'))
        else:
            login_user(user)
            return redirect(url_for('main.root'))
    else:
        return render_template("login.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cPassword = request.form.get('passwordConfirm')
        firstName = request.form['firstName']
        lastName = request.form['lastName']

        # # Compares password to confirmation of password
        # if password != cPassword:
        #     flash("Password and password confirmation do not match.")

        # user is a User that has that username
        user = User.query.filter_by(username=username).first()

        # If the user already exists, prompt the user with the error
        # and redirect them to signup again.
        if user:
            flash("Username already exists.")
            return redirect(url_for('auth.signup'))
        
        # Hash the password
        hashedPassword = generate_password_hash(password, method='sha256')

        # Create a new user user using the form data.
        new_user = User(firstName = firstName, lastName = lastName, username=username, password=hashedPassword)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.root'))
    else:
        return render_template('signup.html')

@auth.route('/logout')
@login_required
def legout():
    logout_user()
    return redirect(url_for('main.root'))