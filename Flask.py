# Flask.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello, World!'

# Command Prompt
# set FLASK_APP=Flask.py
# python -m flask run

# enable debugging
# set FLASK_ENV=development
