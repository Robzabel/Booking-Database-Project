from flask import Flask
from config import Config


#Method to create an instance of the application
def create_app():
    #Initialise the app with the environment variables from the config file
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.testing = Config.TESTING 
    app.debug = Config.DEBUG

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

  



