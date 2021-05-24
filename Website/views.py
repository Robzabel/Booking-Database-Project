from flask import Blueprint, render_template
from flask_login import login_required, current_user


"""
Create views that dont require authentication
"""

#create the object of blueprint that defines the site views, call it the same as the filename for clarity
views = Blueprint('views', __name__) 

@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/manage')
@login_required
def booking():
    return render_template("manage.html", user=current_user)