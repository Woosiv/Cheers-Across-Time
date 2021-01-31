from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from cats import getCat
from quote import getQuote

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
    if current_user.username != username:
        flash("You can't access someone else's dashboard")
        return redirect(url_for('main.dashboard', username=current_user.username, catImage=getCat(), quote=getQuote()))
    if request.method == "POST":
        print(request.form)
        print(request.form["name"])
    return render_template("dashboard.html", username=current_user.username, catImage=getCat(), quote=getQuote())

