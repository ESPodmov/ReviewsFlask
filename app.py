from flask import Flask
from handlers import register_handlers


def create_app():
    flask_app = Flask(__name__)
    register_handlers(flask_app)
    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
