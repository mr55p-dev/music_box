from flask import Flask, redirect, url_for, render_template
import subprocess
from multiprocessing import Process

app=Flask(__name__)

def playTheMusic():
    output = subprocess.run(['ffplay', '-nodisp', '-autoexit','./audio/file.mp3'])
    output.check_returncode()
    return output.returncode

@app.route('/')
def rootPage():
    return(render_template('index.html'))
    # return "This is a page"


@app.route('/play')
def play():
    p = Process(target=playTheMusic)
    return redirect(url_for('rootPage'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port='80', debug=True)
