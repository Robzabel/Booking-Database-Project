from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Restaurant, Booking
from . import db


"""
Create views that dont require authentication
"""

#create the object of blueprint that defines the site views, call it the same as the filename for clarity
views = Blueprint('views', __name__) 

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    #SQLAlchemy queries to make objects for the homepage cards
    r1_card = Restaurant.query.filter_by(id="1").first()
    r2_card = Restaurant.query.filter_by(id="2").first()
    r3_card = Restaurant.query.filter_by(id="3").first()
    
    #Initialise the restaurant and user objects
    restaurants = Restaurant.query.all()
    user = current_user
    
    #Fetch the information about the booking
    if request.method == 'POST':
        #Get the user ID from the current_user 
        user_id = user.id
        #get the rest ID, this messy and can be improved with switch case statement
        if request.form.get('select_rest') == 'Restaurant 1':
            restaurant_id = 1
        elif request.form.get('select_rest') == 'Restaurant 2':
            restaurant_id = 2
        elif request.form.get('select_rest') == 'Restaurant 3':
            restaurant_id = 3
        booking_date = request.form.get('booking_date')
        booking_time = request.form.get('booking_time')
        num_of_guests = request.form.get('number_of_guests')
        comment = request.form.get('comment')
        
        #Input the information into the database
        new_booking = Booking(userId=user_id, restaurantId=restaurant_id, bookingDate=booking_date, bookingTime=booking_time, numberOfGuests=num_of_guests, dietaryRequirements=comment )
        db.session.add(new_booking)
        db.session.commit()

        #Flash a success message and takethe user to their manage bookings page
        flash("You booking was successfully created!")
        return redirect(url_for('views.booking'))  

    return render_template("home.html", user=current_user, restaurants=restaurants, r1_card=r1_card, r2_card=r2_card, r3_card=r3_card)


    


@views.route('/manage', methods=['GET', 'POST'])
@login_required
def booking():

    user = current_user
    user_bookings = Booking.query.filter_by(userId=user.id).all()
    if request.method == 'POST':
        booking_id = request.form.get('cancel_booking')
        booking_to_cancel = Booking.query.get(booking_id)
        if booking_to_cancel:
            db.session.delete(booking_to_cancel)
            db.session.commit()
            return redirect(url_for('views.booking'))

  
    return render_template("manage.html", user=current_user, user_bookings=user_bookings)
    