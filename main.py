from Website import create_app
from config import Config


app = create_app()


if __name__ == "__main__":
    app.run(host=Config.SERVER_NAME)
    