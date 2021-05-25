from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Restaurant, Booking
from . import db
from datetime import date

"""
Create views that dont require authentication
"""

#create the object of blueprint that defines the site views, call it the same as the filename for clarity
views = Blueprint('views', __name__) 

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    restaurants = Restaurant.query.all()
    user = current_user
    
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
        
        new_booking = Booking(userId=user_id, restaurantId=restaurant_id, bookingDate=booking_date, bookingTime=booking_time, numberOfGuests=num_of_guests, dietaryRequirements=comment )
        db.session.add(new_booking)
        db.session.commit()
        return redirect(url_for('views.booking'))  

    return render_template("home.html", user=current_user, restaurants=restaurants)


    


@views.route('/manage')
@login_required
def booking():
    return render_template("manage.html", user=current_user)