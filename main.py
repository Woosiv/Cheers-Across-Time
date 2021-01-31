from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from cats import getCat

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

@main.route('/dashboard/<username>', methods=["GET", "POST"])
@login_required
def dashboard(username=None):
    if request.method == "POST":
        print(request.form)
        print(request.form["name"])
    print(getCat())
    return render_template('dashboard.html', username=username, catImage=getCat())

