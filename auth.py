from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

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

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cPassword = request.form.get('passwordConfirm')
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        # user is a User that has that username
        user = User.query.filter_by(username=username).first()

        # If the user already exists, prompt the user with the error
        # and redirect them to signup again.
        if user:
            flash("Username already exists")
            return redirect(url_for('auth.signup'))
        
        # Hash the password
        hashedPassword = generate_password_hash(password, method='sha256')

        # Create a new user user using the form data.
        new_user = User(username=username, password=hashedPassword)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.root'))
    
    return render_template('signup.html')
