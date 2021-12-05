from flask import Flask, render_template

app = Flask(__name__)

users = [
    { 'name': 'Ahyeon', 'profile': 'picture'},
    { 'name': 'Ahyeon2', 'profile': 'picture2'}
]

@app.route('/')
def user_index():
    """Show all users"""
    return render_template('user_index.html', users = users)

if __name__ == '__main__':
    app.run(debug=True)