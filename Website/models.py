from . import db
from flask_login import UserMixin

"""
Create the tables for the database with SQLAlchemy models
"""

#Create the Users model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    booking = db.relationship('Booking')

    
    def __repr__(self):
        return f"<User {self.first_name}>"


#Create the booking model
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    restaurantId = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    bookingDate = db.Column(db.Date)
    bookingDime = db.Column(db.Time)
    numberOfGuests = db.Column(db.Integer, nullable=False)
    dietaryRequirements = db.Column(db.String(150))

    def __repr__(self):
        return f"<Booking {self.id}>"


#Create the restaurant model
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    booking = db.relationship('Booking')

    def __repr__(self):
        return f"<Restaurant {self.name}>"

#define a function that can be imported to create the database 
def create_database(app):
    #db.drop_all(app=app)
    db.create_all(app=app)
    print("created Database")