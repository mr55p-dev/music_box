from . import app
from .playSound import play
import os

cp = os.getcwd()

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_name(name):
    # print(f"Name: {name}.")
    return f"Hello, {name}"

@app.route("/play/<fileName>")
def playFile(fileName):
    if play(f"static/audio/{fileName}"):
        return "Good"
    else:
        return "Bad"