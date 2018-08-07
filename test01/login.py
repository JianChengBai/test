from flask import Flask


def hello():
    print("Hello World")


app = Flask(__name__)


@app.route('/')
def index():
    return "this is a new project"


@app.route('/login')
def login():
    return "login page"
