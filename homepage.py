from flask import Flask
from threading import Timer
import webbrowser

app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there!"

def open_browser():
    url = "http://127.0.0.1:5000/"
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    Timer(0, open_browser).start()
    app.run(debug=True, use_reloader=False)