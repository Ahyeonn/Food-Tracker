from flask import Blueprint, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from database import*

logger = Blueprint("logger", __name__, static_folder="static", template_folder="templates")

@logger.route('/entries/<entry_id>/loggers')
def loggers_index(entry_id):
    """Show loggers info."""
    entry = entries.find_one({'_id': ObjectId(entry_id)})
    user_loggers = loggers.find({'entry_id': ObjectId(entry_id)})
    return render_template('loggers_index.html', entry=entry, loggers=user_loggers)

@logger.route('/entries/<entry_id>/loggers/new')
def loggers_new(entry_id):
    """Create a logger info."""
    return render_template('loggers_new.html', entry_id=entry_id)

@logger.route('/entries/loggers', methods= ['POST'])
def loggers_submit():
    """Submit a logger info."""
    
    entry_id = request.form.get('entry_id')
    food_name = request.form.get('food_name')
    food_calorie = request.form.get('food_calorie')
    logger = {
        'entry_id': ObjectId(entry_id),
        'food_name': food_name,
        'food_calorie': food_calorie
    }
    loggers.insert_one(logger)
    flash('Food Added!')
    return redirect(url_for('logger.loggers_index', entry_id=entry_id))

@logger.route('/entries/delete/loggers/<logger_id>', methods=['POST'])
def loggers_delete(logger_id):
    """Delete a logger."""
    loggers.delete_one({'_id': ObjectId(logger_id)})
    return redirect(url_for('logger.loggers_index', entry_id=request.form.get('entry_id')))
