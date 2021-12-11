from flask import Blueprint, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from database import*

user = Blueprint("user", __name__, static_folder="static", template_folder="templates")

@user.route('')
def users_index():
    """Show all users."""
    return render_template('users_index.html', users = users.find())

@user.route('/users/new')
def users_new():
    """Create user."""
    return render_template('users_new.html', user={}, title= 'New User')

@user.route('/users', methods= ['POST'])
def users_submit():
    """Submit a user info."""
    user = {
        'name': request.form.get('name'),
        'gender': request.form.get('gender'),
        'state': request.form.get('state')
    }
    users.insert_one(user)
    return redirect(url_for('user.users_show', user_id=user['_id']))    

@user.route('/users/<user_id>')
def users_show(user_id):
    """Show users & entries info."""
    user = users.find_one({'_id': ObjectId(user_id)})
    user_entries = entries.find({'user_id': ObjectId(user_id)})
    return render_template('users_show.html', user=user, entries=user_entries)

@user.route('/users/<user_id>/edit')
def users_edit(user_id):
    """Edit a user."""
    user = users.find_one({'_id': ObjectId(user_id)})
    return render_template('users_edit.html', user=user, title= 'Edit User')

@user.route('/users/<user_id>', methods=['POST'])
def users_update(user_id):
    """Submit an edited user profile."""
    updated_user = {
        'name': request.form.get('name'),
        'gender': request.form.get('gender'),
        'state': request.form.get('state')
    }
    users.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': updated_user})
    return redirect(url_for('user.users_index', user_id=user_id))

@user.route('/users/<user_id>/delete', methods=['POST'])
def users_delete(user_id):
    """Delete one user."""
    users.delete_one({'_id': ObjectId(user_id)})
    entries.delete_many({'user_id': user_id})
    loggers.delete_many({'user_id': user_id})
    return redirect(url_for('user.users_index'))