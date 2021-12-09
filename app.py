from flask import Flask, render_template
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
    """Show all users"""
    return render_template('users_index.html', users = users.find())

if __name__ == '__main__':
    app.run(debug=True)