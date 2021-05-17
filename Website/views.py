from flask import Blueprint, render_template

#create the object of blueprint that defines the site views, call it the same as the filename for clarity
views = Blueprint('views', __name__) 

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/manage')
def booking():
    return render_template("manage.html")