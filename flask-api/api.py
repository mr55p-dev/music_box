from flask import Flask
import time

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello World"

@app.route("/time")
def timeRoute():
    return {"time": time.time()}
