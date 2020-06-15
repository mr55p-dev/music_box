from flask import Flask
import subprocess
app=Flask(__name__)

@app.route('/')
def rootPage(self):
    with open('./web/index.html', 'r') as f:
        return f.read()

@app.route('/play')
def play(self):
    subprocess.call(['ffplay', '-nodisp','./audio/file.mp3'])
    return "Playing music"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
