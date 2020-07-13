from flask import Flask, redirect, url_for, render_template, request
from multiprocessing import Process
from card import cards
import subprocess

app = Flask(__name__)


def playTheMusic(fileName):
    try:
        subprocess.run(["ffplay", "-nodisp", "-autoexit", f"./static/audio/{fileName}"])
        # output.check_returncode()
        # return output.returncode
        return ("", 200)
    except Exception:
        return ("Failed to play file on server.", 202)

@app.route("/", methods=['GET', 'POST'])
def rootPage():
    return render_template("index.html", cards=cards)


@app.route("/play/<filename>", methods=['POST'])
def play():
    status = playTheMusic(fileName)
    return status


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # app.run(ssl_context="adhoc")
    app.run()
