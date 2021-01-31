from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from cats import getCat
from quote import getQuote

main = Blueprint('main', __name__)

#Home Page
@main.route('/')
def root():
    print("sending to home")
    return render_template('login.html')

#Activity
@main.route('/Activity')
def activity():
    return render_template('activity.html')

@main.route('/Home')
def home():
    return render_template('home.html')

@main.route('/dashboard/<username>', methods=["GET", "POST"])
@login_required
def dashboard(username=None):
    if (current_user.username != username):
        flash("You don't have access to this page!")
        return redirect(url_for('main.dashboard', username=current_user.username, catImage=getCat(), quote=getQuote()))

    if request.method == "POST":
        # Convert emoji rating to a string form of a number
        number = request.form["name"]
        print(number)
        # if name == "crying":
        #     number = "1"
        # elif name == "sad":
        #     number = "2"
        # elif name == "neutral":
        #     number = "3"
        # elif name == "smiling":
        #     number = "4"
        # elif name == "laughing":
        #     number = "5"
        
        # Modify the database
        print("before", current_user.moodTracker)
        current_user.updateMood()
        print("after", current_user.moodTracker)

    return render_template("dashboard.html", username=current_user.username, catImage=getCat(), quote=getQuote())
