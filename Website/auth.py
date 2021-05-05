from flask import Blueprint

#Create a blueprint for the authentication view
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/register')
def register():
    return "<p>Register</p>"