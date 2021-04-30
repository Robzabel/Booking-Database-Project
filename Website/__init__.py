from flask import Flask
from config import Config


#Method to create an instance of the application
def create_app():
    #Initialise the app with the environment variables from the config file
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.testing = Config.TESTING 
    app.debug = Config.DEBUG
    return app

  



