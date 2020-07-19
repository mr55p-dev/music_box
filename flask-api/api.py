from flask import Flask
import time

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello World"

@app.route("/time")
def timeRoute():
    print("Getting time from the API.")
    print("#ff49a8")
    return {"currentTime": time.time()}
