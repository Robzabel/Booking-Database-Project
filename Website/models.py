from enum import unique
from . import db
from flask_login import UserMixin

"""
Create the tables for the database with SQLAlchemy models
"""

#Create the Users model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    
    def __repr__(self):
        return f"<User {self.first_name}>"

#Create the booking model
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    restaurant_id = db.Column(db.Integer, db.ForeighKey('resteraunts.id'))
    booking_date = db.Column(db.Date)
    booking_time = db.Column(db.Time)
    number_of_guests = db.Column(db.Integer, nullable=False)
    dietary_requirements = db.Column(db.String(150))

    def __repr__(self):
        return f"<Booking {self.id}"

#Create the restaurant model
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colums(db.String(50))
    location = db.Colums(db.String(50))

    def __repr__(self):
        return f"<Restaurant {self.name}"