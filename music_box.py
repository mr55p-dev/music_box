from flask import Flask, redirect, url_for, render_template, request
from multiprocessing import Process
from card import cards
import subprocess


app = Flask(__name__)


def playTheMusic(fileName):
    subprocess.run(["ffplay", "-nodisp", "-autoexit", f"./static/audio/{fileName}"])
    # output.check_returncode()
    # return output.returncode
    return


@app.route("/", methods=['GET', 'POST'])
def rootPage():
    return render_template("index.html", cards=cards)


@app.route("/play/<fileName>", methods=['POST'])
def play(fileName):
    playTheMusic(fileName)
    return redirect(url_for("rootPage"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # app.run(ssl_context="adhoc")
    app.run()
