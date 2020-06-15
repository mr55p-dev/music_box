from flask import Flask
import subprocess
from multiprocessing import Process

app=Flask(__name__)

def playTheMusic():
    subprocess.call(['ffplay', '-nodisp', '-autoexit','./audio/file.mp3'])

@app.route('/')
def rootPage():
    x = ""
    with open('./web/index.html', 'r') as f:
        x = f.read()
    return x
    # return "This is a page"


@app.route('/play')
def play():
    p = Process(target=playTheMusic)
    p.start()
    return "Playing music"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
