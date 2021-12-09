from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.FoodTracker
users = db.users

# users = [
#     { 'name': 'Ahyeon', 'profile': 'picture'},
#     { 'name': 'Ahyeon2', 'profile': 'picture2'}
# ]

@app.route('/')
def users_index():
    """Show all users."""
    return render_template('users_index.html', users = users.find())

@app.route('/users/new')
def users_new():
    """Create user."""
    return render_template('users_new.html')

@app.route('/users', methods= ['POST'])
def users_submit():
    """Submit a user info."""
    user = {
        'name': request.form.get('name'),
        'gender': request.form.get('gender'),
        'state': request.form.get('state')
    }
    users.insert_one(user)
    return redirect(url_for('users_index'))    

if __name__ == '__main__':
    app.run(debug=True)