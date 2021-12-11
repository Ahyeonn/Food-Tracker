from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from entry import entry
from logger import logger
from user import user
from page import page
from database import*

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(page, url_prefix="/")
app.register_blueprint(user, url_prefix="/")
app.register_blueprint(entry, url_prefix="/")
app.register_blueprint(logger, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)