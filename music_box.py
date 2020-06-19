from flask import Flask, redirect, url_for, render_template
import subprocess
from multiprocessing import Process
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


cards = [
    [
        "Lizst - Hungarian Rhapsody no 12",
        "lizst.mp3",
        "Music box style excerpt from our piece.",
        "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.ien.com%2Ffiles%2Fbase%2Findm%2Fien%2Fimage%2F2018%2F05%2F640w%2Fpiano_keys.5aec75c0e81fa.jpg&f=1&nofb=1",
    ],
    [
        "Chopin - Raindrop Prelude",
        "raindrop.mp3",
        "Excerpt from the song I learned for you.",
        "http://typotic.com/uploads/posts/5593/raindrops.jpg",
    ],
    [
        "Bach - Prelude in C Major",
        "prelude.mp3",
        "First piece I learned to read only from the music",
        "https://i.ytimg.com/vi/B-rgOYwjRk0/hqdefault.jpg",
    ],
]
# titleFilenameDict = {
#     cards[0][0]: "lizst.mp3",
#     cards[1][0]: "raindrop.mp3",
#     # cards[2][0]: ""
#     # cards[3][0]: ""
#     # cards[4][0]: ""
# }


def playTheMusic(fileName):
    subprocess.run(["ffplay", "-nodisp", "-autoexit", f"./static/audio/{fileName}"])
    # output.check_returncode()
    # return output.returncode
    return


@app.route("/")
def rootPage():
    return render_template("index.html", cards=cards)
    # return "This is a page"


@app.route("/play/<fileName>")
def play(fileName):
    playTheMusic(fileName)
    return redirect(url_for("rootPage"))


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
    # app.run()
