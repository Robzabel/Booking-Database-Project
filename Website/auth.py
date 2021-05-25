from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

"""
Create views that require authenitication
"""
#Create a blueprint for the authentication view
auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    #Fetch submitted form data
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #Query the DB for the email address
        user = User.query.filter_by(email=email).first()
        #if the user exists check the password
        if user:
            if check_password_hash(user.password, password):
                flash("You have logged in Successfully", category='success')
                login_user(user, remember=True)# create a session token for the user
                return redirect(url_for('views.home'))
            else:
                flash("The password is incorrect!", category='error')
        else:
            flash("User does not exist, Please Register", category='error')
            return redirect(url_for('auth.register'))
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out successfully!", category='success')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    #Fetch submitted form data
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #check if the user already exists on the DB
        user = User.query.filter_by(email=email).first()
        if user:
            flash("This address already exists, Please enter a different one!", category='error')
        elif '@' and '.' not in email:
            flash('Email address not valid.', category='error')
        elif len(first_name) < 1:
            flash('Please enter a first name.', category='error')
        elif len(last_name) < 1:
            flash('Please enter a last name.', category='error')
        elif password1 != password2:
            flash('The passwords do not match.', category='error')
        elif len(password1) < 6:
            flash('Your password must be at least 6 characters long.', category='error')
        else: #Create a new user object, hash the password and commit it to the database
            new_user = User(email=email, firstName=first_name, lastName=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user) #log the new user in once their details are corrrect
            flash('You are now registered.', category='success')
            return redirect(url_for('views.home'))#redirects the user to the home route of the view blueprint

    return render_template('register.html', user=current_user)