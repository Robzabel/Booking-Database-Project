from flask import Blueprint, render_template, request, flash, session


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
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('home.html')


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    #Fetch submitted form data
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if '@' and '.' not in email:
            flash('Email address not valid.', category='error')
        elif len(first_name) < 1:
            flash('Please enter a first name.', category='error')
        elif len(last_name) < 1:
            flash('Please enter a last name.', category='error')
        elif password1 != password2:
            flash('The passwords do not match.', category='error')
        elif len(password1) < 6:
            flash('Your password must be at least 6 characters long.', category='error')
        else: 
            #add user to the database
            flash('You are now registered.', category='success')

    return render_template('register.html')