from flask import Flask
import subprocess
app=Flask(__name__)

@app.route('/')
def rootPage(self):
    # self.x = ""
    # with open('./web/index.html', 'r') as self.f:
    #     self.x = self.f.read()
    # return self.x
    return "This is a page"


@app.route('/play')
def play(self):
    subprocess.call(['ffplay', '-nodisp','./audio/file.mp3'])
    return "Playing music"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
