from flask import Blueprint, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from database import*

page = Blueprint("page", __name__, static_folder="static", template_folder="templates")

@page.route('/home')
def home_index():
    return render_template('home_index.html')

@page.route('/about_us')
def about_us_index():
    return render_template('about_us_index.html')

@page.route('/daily_calorie')
def daily_calorie_index():
    return render_template('daily_calorie_index.html')