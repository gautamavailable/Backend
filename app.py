from flask import Flask
app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return 'This is homepage!'

if __name__ == '__main__':
    app.run(debug=True)

# Importing after the route definitions
from controller import *
