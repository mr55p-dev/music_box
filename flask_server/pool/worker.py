import logging
import subprocess


PIPE = subprocess.PIPE
worker_log = logging.getLogger("worker_log")


def play(filePath):
    print(f"Starting play job: {filePath}")
    worker_log.info(f"Starting play job: {filePath}")
    proc = subprocess.Popen(['ffplay', '-autoexit', '-nodisp', filePath], stdout=PIPE, stderr=PIPE)
    with proc.stderr:
        out, err = proc.communicate()
        print(f"output: {out}\nerror: {err}")
    # worker_log.info("Opening subprocess.")
    # worker_log.info(proc.stderr)
    return 1
