from enum import unique
from . import db
from flask_login import UserMixin

"""
Create the tables for the database with SQLAlchemy models
"""
class User(db.Model, UserMixin):
    User_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
