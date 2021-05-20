from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
"""
Create the App Factory 
"""
#Initialise the objects
db = SQLAlchemy()

#Method to create an instance of the application
def create_app():

    #Initialise the app 
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.testing = Config.TESTING 
    app.debug = Config.DEBUG

    #Initialise the Databade 
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_STRING
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

  
    #Initialise the blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #Return the app to the calling function
    return app

  



