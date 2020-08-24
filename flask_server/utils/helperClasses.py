import threading
import subprocess
import time


def play(filename):
    proc = subprocess.Popen('ffplay', args=["-autoexit", "-nodisp", filename])
    while not proc.poll():
        time.sleep(1)

    return proc


def validate(func):
    def wrapper(threadID, *args, self=None, **kwargs):
        if threadID not in self.threads:
            return False
        else:
            func(*args, **kwargs)
    return wrapper


class ThreadHandler():
    threads = {}

    def create(self, filename):
        # Figure out why it says 60 args are given, how to pass positional arguments to Popen.
        thread = threading.Thread(
                                  target=subprocess.Popen,
                                  args=('ffplay', args=["-autoexit", "-nodisp", filename])
                                  )
        thread.start()
        self.threads[thread.native_id] = thread
        return thread.native_id

    # @validate
    # def start(self, threadID):
    #     self.threads[threadID].start()
    #     return True

    @validate
    def monitor(self, threadID):
        # self.threads.signal Need this to be a thing lol.
        return True

    @validate
    def destroy(self, threadID):
        return False
