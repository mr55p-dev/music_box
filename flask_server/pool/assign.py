from flask_server.pool.worker import play
from flask import current_app
import logging


application_log = logging.getLogger('application_log')


def add_to_queue(filePath):
    job = current_app.queue.enqueue(play, filePath)
    application_log.info(f"Created worker with id: {job.id}")
    if not job:
        application_log.warning("Worker failed.")
        return None
    else:
        application_log.info("Worker exitedited with code 0.")
        return True
