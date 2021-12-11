from flask import Blueprint, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from database import*

entry = Blueprint("entry", __name__, static_folder="static", template_folder="templates")

@entry.route('/users/<user_id>/entries/new')
def entries_new(user_id):
    """Create an entry."""
    return render_template('entries_new.html', user_id=user_id)

@entry.route('/users/entries', methods= ['POST'])
def entries_submit():
    """Submit an entry info."""
    user_id = request.form.get('user_id')
    date = request.form.get('date')
    if entries.find_one({'date': date, 'user_id': ObjectId(user_id)}):
        flash('The date already exists')
        return redirect(url_for('user.users_show', user_id=user_id))
    entry = {
        'user_id': ObjectId(user_id),
        'date': date,
    }
    entries.insert_one(entry)
    return redirect(url_for('user.users_show', user_id=user_id))

@entry.route('/users/entries/<entry_id>/delete', methods=['POST'])
def entries_delete(entry_id):
    """Delete an entry."""
    entries.delete_one({'_id': ObjectId(entry_id)})
    loggers.delete_many({'entry_id': entry_id})
    return redirect(url_for('user.users_show', user_id=request.form.get('user_id')))