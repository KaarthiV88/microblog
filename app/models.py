from werkzeug.security import generate_password_hash, check_password_hash  
from flask_login import UserMixin
from datetime import datetime
from app import login
from app import db


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    projects = db.relationship('Project', backref='manager', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    cost = db.Column(db.Numeric)
    completion = db.Column(db.Numeric)
    image_filepath = db.Column(db.String)
    hyperlinks = db.Column(db.String)
    description = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Project {}>'.format(self.description)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))