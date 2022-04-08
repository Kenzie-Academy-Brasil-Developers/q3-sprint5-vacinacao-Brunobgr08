from flask import Flask
import os


def init_app(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["JSON_SORT_KEYS"] = False





