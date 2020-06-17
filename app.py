from flask import Flask, redirect, url_for, render_template
import subprocess
from multiprocessing import Process
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)

def playTheMusic():
    subprocess.run(['ffplay', '-nodisp', '-autoexit','./audio/file.mp3'])
    # output.check_returncode()
    # return output.returncode
    return

@app.route('/')
def rootPage():
    return(render_template('index.html', cardTitle=["Lizst - Hungarian Rhapsody no. 12"], cardBody=["Music box style excerpt from our piece."]))
    # return "This is a page"


@app.route('/play/')
def play():
    playTheMusic()
    return redirect(url_for('rootPage'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port='80', debug=True)
    # app.run()
