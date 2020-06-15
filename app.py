from flask import Flask
import subprocess
app=Flask(__name__)

@app.route('/')
def rootPage():
    x = ""
    with open('./web/index.html', 'r') as f:
        x = f.read()
    return x
    # return "This is a page"


@app.route('/play')
def play():
    subprocess.call(['ffplay', '-nodisp','./audio/file.mp3'])
    return "Playing music"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
