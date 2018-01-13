from flask import Flask
from luis_sdk import LUISClient
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"