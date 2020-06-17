from flask import Flask, redirect, url_for, render_template
import subprocess
from multiprocessing import Process
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


cardTitle = ([],)
cardBody = []
cards = [
    [
        "Lizst - Hungarian Rhapsody no. 12",
        "Music box style excerpt from our piece.",
        "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.ien.com%2Ffiles%2Fbase%2Findm%2Fien%2Fimage%2F2018%2F05%2F640w%2Fpiano_keys.5aec75c0e81fa.jpg&f=1&nofb=1",
    ],
]


def playTheMusic():
    subprocess.run(["ffplay", "-nodisp", "-autoexit", "./static/audio/file.mp3"])
    # output.check_returncode()
    # return output.returncode
    return


@app.route("/")
def rootPage():
    return render_template("index.html", pageTitle="Music Box Home", cards=cards)
    # return "This is a page"


@app.route("/play/")
def play():
    playTheMusic()
    return redirect(url_for("rootPage"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True)
    # app.run()
