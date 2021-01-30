from flask import Flask, render_template, request
from threading import Timer
import time
import webbrowser
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__, static_url_path='', static_folder='static')

# Configure app
app.config.from_object('config.Config')

db.init_app(app)

#HomePage
@app.route('/')
def root():
    print("sending to home")
    return app.send_static_file('home.html')

def open_browser():
    url = "http://127.0.0.1:5000/"
    webbrowser.open_new_tab(url)

# Login Page
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("reached here")
        print(request.form['username'])
        print(request.form['password'])
        return app.send_static_file('home.html')
    else:
        return app.send_static_file('login.html')

if __name__ == '__main__':
    #Timer(0, open_browser).start()
    app.run(debug=True, use_reloader=False)
