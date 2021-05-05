from flask import Blueprint

#create the object of blueprint that defines the site views, call it the same as the filename for clarity
views = Blueprint('views', __name__) 

@views.route('/')
def home():
    return "<h1>Hello</h1>"
