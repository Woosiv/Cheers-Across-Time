from flask import Blueprint, render_template

main = Blueprint('main', __name__)

#Home Page
@main.route('/')
def root():
    print("sending to home")
    return render_template('home.html')

#Activity
@main.route('/Activity')
def activity():
    return render_template('activity.html')

