from Website import create_app
from config import Config

"""
Create an object of the app and run it
"""
app = create_app()


if __name__ == "__main__":
    app.run(host=Config.SERVER_NAME)
    