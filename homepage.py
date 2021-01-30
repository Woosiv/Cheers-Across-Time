from flask import Flask, render_template
from threading import Timer
import time
import webbrowser

app = Flask(__name__)
#HomePage
@app.route('/')
def home():
    return render_template('home.html')

# Login Page
@app.route('/login')
def login():
    return "Log in"

# About
@app.route('/#')
def about():
    return render_template('about.html')

def open_browser():
    url = "http://127.0.0.1:5000/"
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    Timer(0, open_browser).start()
    app.run(debug=True, use_reloader=False)
