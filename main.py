from flask import Blueprint, render_template, request, flash
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

@main.route('/Home')
def home():
    return render_template('home.html')

@main.route('/Home2')
def home2():
    return render_template('home2.html')

@main.route('/dashboard/<username>', methods=["GET", "POST"])
@login_required
def dashboard(username=None):
    # Obtain moodTracker and convert to list of int
    phrase = current_user.getMood()
    data = []
    for num in phrase:
        data.append(int(num))


    if (current_user.username != username):
        flash("You don't have access to this page!")
        return redirect(url_for('main.dashboard', username=current_user.username, catImage=getCat(), quote=getQuote(), item=data))

    if request.method == "POST":
        # Convert emoji rating to a string form of a number
        number = request.form["name"]

        # Modify the database
        current_user.updateMood(number)

        # Update data list
        data.append(int(current_user.getMood()[-1]))
        if len(data > 7):
            data.pop(0)

    return render_template("dashboard.html", username=current_user.username, catImage=getCat(), quote=getQuote(), item=data)
