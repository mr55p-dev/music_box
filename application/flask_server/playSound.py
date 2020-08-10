import subprocess

def play(fileName):
    try:
        subprocess.run(["ffplay", f"{fileName}.mp3"])
    except:
        return None