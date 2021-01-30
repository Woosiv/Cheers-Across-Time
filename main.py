from flask import Blueprint, render_template

main = Blueprint('main', __name__)

#Home Page
@main.route('/')
def root():
    print("sending to home")
    return render_template('home.html')

# About
@main.route('/#')
def about():
    return render_template('about.html')