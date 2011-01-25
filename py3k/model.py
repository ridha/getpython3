from .application import db

from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    pw_hash = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    def __init__(self, username, password, email, first_name='', middle_name='', last_name=''):
        self.username = username
        self.set_password(password)
        self.email = email
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)