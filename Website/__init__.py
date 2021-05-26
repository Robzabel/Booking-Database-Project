from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

"""
Create the App Factory 
"""
#Initialise the db object
db = SQLAlchemy()

#Method to create an instance of the application
def create_app():

    #Initialise the app 
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.testing = Config.TESTING 
    app.debug = Config.DEBUG


    #Initialise the Database object peramaters 
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_STRING
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True #used for testing to see the SQL commands being run
    db.init_app(app)
    

    #Initialise the databse models
    from .models import create_database, User
    create_database(app)


    #Initialise the blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    #Initialise the Login Manager & define the user_loader
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    #Query the DB for user details based on the ID so the user doenst need to
    @login_manager.user_loader
    def load_user(id):
	    return User.query.get(int(id))

    #Return the app to the calling function
    return app





