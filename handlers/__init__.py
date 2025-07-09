from flask import Blueprint
from .reviews import bp as reviews_bp


def register_handlers(app):
    app.register_blueprint(reviews_bp)
