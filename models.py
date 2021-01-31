from flask_login import UserMixin
from exts import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    moodTracker = db.Column(db.String(8))
    email = db.Column(db.String(100), unique=True)