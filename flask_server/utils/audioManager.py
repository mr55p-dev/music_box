from subprocess import PIPE
from time import sleep
import subprocess
import threading
import logging


mp_log = logging.getLogger('multiprocessing_log')
mp_log.info(f"Loaded audioManager module from {__name__}")


def validate(filename: str):
    # path, dirs, files = os.walk(current_app.config["UPLOAD_FOLDER"])
    # if filename.split('/')[-1] in:
    #     return True
    # else:
    #     return False
    return True


def test(callback, callback_args, fn):
    mp_log.info("function test called")

    with subprocess.Popen(['echo', 'https://www.google.com'], stdout=PIPE, stderr=PIPE) as proc:
        mp_log.info(proc.stdout.readlines())
        # mp_log(f"Exited with code {proc.poll()}")

    returned = callback(callback_args)
    mp_log.info("post-callback")
    return returned


def playFile(callback, callback_args, filename):
    mp_log.info("function playFile called")
    if not validate(filename):
        return False

    proc = subprocess.Popen(['ffplay', '-autoexit', '-nodisp', filename], stdout=PIPE, stderr=PIPE)
    # proc = subprocess.Popen(['curl', 'https://www.google.com'], stdout=PIPE, stderr=PIPE)
    while not proc.poll():
        mp_log.info("Running...")
        sleep(5)
    mp_log(f"Exited with code {proc.returncode}")
    callback(callback_args)
    mp_log.info("post-callback")
    return


# @trace
def openInThread(callback, callbackargs, filename):
    """
    Allows the music to play in an asychronous way using ffplay,
    with a callback to execute when the song is done.
    """
    mp_log.info("Called openInThread")
    thread = threading.Thread(target=playFile, args=(callback, callbackargs, filename))
    mp_log.info("Starting thread")
    thread.start()
    mp_log.info("Returning...")
    return thread
