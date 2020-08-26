# import threading
# import subprocess
# import logging
# from time import sleep


# log = logging.getLogger('threadHandler_log')


# def play(filename):
#     log.info("Called play")
#     if not validate(filename):
#         log.warning("Invalid filename")
#         return False

#     proc = subprocess.Popen(['ffplay', '-autoexit', '-nodisp', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     # proc = subprocess.Popen(['curl', 'https://www.google.com'], stdout=PIPE, stderr=PIPE)
#     while not proc.poll():
#         sleep(5)

#     return True


# def validate(func):
#     def wrapper(threadID, *args, self=None, **kwargs):
#         if threadID not in self.threads:
#             return False
#         else:
#             func(*args, **kwargs)
#     return wrapper


# class ThreadHandler():
#     threads = {}

#     def __init__(self) -> None:
#         log.info("ThreadHandeler() created")

#     def __repr__(self) -> str:
#         return "\n".join([f"{key}: {value}" for key, value in self.threads.items()])

#     def create(self, filename):
#         # Figure out why it says 60 args are given, how to pass positional arguments to Popen.
#         thread = threading.Thread(
#                                   target=play,
#                                   args=(filename,)
#                                   )
#         self.threads[thread.native_id] = thread
#         self.threads[thread.native_id].start()
#         return thread.native_id

#     # @validate
#     # def start(self, threadID):
#     #     self.threads[threadID].start()
#     #     return True

#     @validate
#     def monitor(self, threadID):
#         # self.threads.signal Need this to be a thing lol.
#         return True

#     @validate
#     def destroy(self, threadID):
#         return False

import logging
import os
from pickle import UnpicklingError
import socket
import subprocess
import pickle
from subprocess import Popen
from typing import Dict, Generator, List, Optional, Union


def uid() -> Generator[int, None, None]:
    """
    Simple function to generate unique id's for each of the
    _item instances which may be generated. Should not be
    imported directly; use the `unique` generator defined
    in this module.
    Example:
        unique_id1 = next(unique)
        unique_id2 = next(unique)
        etc...
    """
    i: int = 0
    while True:
        i += 1
        yield i


unique = uid()


class Message():
    """
    Message class to be sent over a socket, subclassed by an Item if one was present.
    Attributes:
        message(str): The message text to be sent over the socket.
    """
    def __init__(self, message: str) -> None:
        """
        Create a message class which simply holds a message which can be set or read.
        Args:
            message(str): Message to be sent or recieved message
        """
        self._message = message

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        self._message = message


class Item(Message):
    """
    Class to contain the properties of _queue items and manipulate them.
    Attributes:
        caller(int): The id of the User object which has added this _item to the _queue
        file(str): The file path to play
        complete(bool): If True then remove from Queue and avoid playing again
                        (must be readded to the _queue)
    """

    _uid: int
    _caller: int
    _filename: str
    _complete: bool = False

    def __init__(self, caller: int, filename: str, message: str, uid: int = next(unique)) -> None:
        """
        args:
            caller(int): The user ID
            filename(str): The filename to play
        kwargs:
            uid(int): Optionally specify a custom ID (should be unique) else use the
                     generated one.
        """
        super().__init__(message)
        self._uid = uid
        self._complete = False
        self._caller = caller
        self._filename = filename

    def __repr__(self) -> str:
        return ""

    def properties(self) -> Dict[str: Union[str, int, bool]]:
        """Returns the _item attributes following:
                dict{
                    "uid": int
                    "caller": int,
                    "filename": str,
                    "complete": bool
                }
        """
        return {
            "id": self._uid,
            "caller": self._caller,
            "filename": self._filename,
            "complete": self._complete
        }

    @property
    def uid(self) -> int:
        return self._uid

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def caller(self) -> int:
        return self._caller

    @property
    def complete(self) -> bool:
        return self._complete

    @uid.setter
    def uid(self, uid: int) -> None:
        self._uid = uid

    @filename.setter
    def filename(self, filename: str) -> None:
        self._file = filename

    @caller.setter
    def caller(self, caller: int) -> None:
        self._caller = caller

    @complete.setter
    def complete(self, complete: bool) -> None:
        self._complete = compile


class PlayQueue():
    """
    Class to handle the requests to play music sent to the box
    from the Flask web server. Should be able to handle queueing,
    popping, play/pause, skipping, stopping.

    Attributes:
            item(dict): {"caller": int, "file": None, "complete": bool}
            queue(list(item)): A list of items which represent the order and attributes
                               of the next songs in the queue
    """
    _queue = List[Optional[Item]]

    def __init__(self) -> None:
        """Initalise the Queue class"""
        return None

    def __repr__(self) -> str:
        """Return the current queued files as a list."""
        return [i["file"] for i in self._queue]

    def _clean(self) -> None:
        self.queue = [i for i in self.queue if not i.complete]

    @property
    def queue(self) -> List[Item]:
        return self._queue

    @queue.setter
    def queue(self, queue: Optional[List[Item]]) -> None:
        self._queue = queue

    @property
    def current(self) -> Optional[Item]:
        """Get the current item to be played"""
        self._clean()
        if not self.queue:
            return None
        else:
            return self.queue[0]

    @current.setter
    def current(self, item: Item) -> None:
        if item.uid in self.queue:
            self.queue[0] = item

    def update(self, item: Item) -> None:
        """Updates the property of a given item with the passed item if that item exists in the queue"""
        self._queue = [item if i.uid == item.uid else i for i in self._queue]
        return None

    def append(self, item: Item) -> None:
        """Appends an item to the internal queue"""
        self._queue.append(item)
        return None

    def enqueue(self, item: Item) -> List[Item]:
        """Append a new object Item to the end of the current queue"""
        self.append(item)
        return self.queue

    def pop(self, uid: Optional[int] = None) -> Optional[Item]:
        """Remove either a specific item from the queue via uid or pop the last item added"""
        self._clean()
        if uid:
            self._queue = [i for i in self._queue if i.uid != uid]
        else:
            try:
                self._queue.pop()
            finally:
                return None

        """Remove any items which have been played"""
        if not self._queue:
            return None
        self._queue = [i for i in self._queue if not i.complete]
        return None

    def skip(self) -> Optional[Item]:
        """Mark the current song as complete and push self.current"""
        current = self.current
        current.complete = True
        self.update(current)
        self._clean()

        return self.current

    def clear(self) -> None:
        self.queue = []


def play(path: str) -> Popen:
    """Open a process which calls `ffplay` on the path provided"""
    proc = subprocess.Popen(
                            ['ffplay', '-autoexit', '-nodisp', path],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                            )
    return proc


if __name__ == "__main__":
    # Create a unix socket
    soc = socket.socket('AF_UNIX', 'SOCK_STREAM', 0)
    soc.bind(os.path.join(os.getcwd(), 'socket/socket.s'))
    soc.listen()

    # Set up vars
    qh = PlayQueue()
    playing = Optional[subprocess.Popen]
    logging.basicConfig("logs/listener.log")
    log = logging.getLogger('listener')

    while True:
        # Update current song.
        current_song = qh.current
        if current_song and not playing:
            # If there is something to play, play it (potentially use playing.poll())
            playing = play(current_song)

        # As long as there isnt, accept incoming requests.
        # Figure out a good message size. Load the recieved object.
        conn, address = soc.accept()
        data, sender = soc.recvmsg(4096)
        try:
            recv = pickle.loads(data)
        except UnpicklingError:
            log.error("Could not unpickle response, check that data has been created correctly.")
            recv = None

        # Now validate if the recieved object is of the correct type
        if isinstance(recv, Item):
            message = recv.message

            # Logic for if a song to be played has been sent
        elif isinstance(recv, Message):
            message = recv.message
            # Logic for play/pause
        else:
            log.error(f"Recieved a response of type {type(recv)} which is not valid.")
            log.error("Only types Message and Item can be sent.")
            pass


def messageLogic(message: str, qh: Optional[PlayQueue] = None, item: Optional[Item] = None):
    if message == 'play':
        qh.append(item)
        return 'play'
    elif message == 'stop':

        return 'stop'
    elif message == 'pause':
        return 'pause'
    elif message == 'fetch':
        return 'fetch'
    else:
        log.info(f"Invalid message: {message}")
        return None


"""
Need to find a way to set a fixed sensible message size
Create a standard response object which can handle
all the different scaenarios in the main program.
Maybe put things into functions
"""


"""
if __name__ == "__main__":
    qh = PlayQueue()
    playing = None
    while True:
        # Emulates listening on a socket for incoming requests
        current_song = qh.current
        if current_song and not playing:
            # If there is a song to play and it hasnt been started, start it
            playing = play(current_song.filename)

        elif conn.recieve.str == 'play':
            # If the play request is recieved, then play
            item: Item = conn.recieve.data
            qh.enqueue(item)

        elif conn.recieve.str == 'stop':
            # If the stop request is recieved, then stop
            if current_song or playing:
                try:
                    playing.communicate(stop)
                    current_song.complete = True
                    qh.update(current_song)
                except NotListeningError:
                    playing.kill()
                finally:
                    qh.clear()

        elif conn.recieve.str == 'pause':
            if playing:
                playing.communicate('p')

        elif conn.recieve.str == 'fetch_queue':
            conn.communicate(qh.queue)

        elif playing:
            # If there is a current play job then wait for it to complete
            if not playing.poll():
                sleep(0.25)
            else:
                # When the task ends, mark the current song as complete and then
                # let the queue handler update it and remove it from the list.
                current_song.complete = True
                qh.update(current_song)





    # listen:
    #     start playing:
    #         music = play(qh.current)
    #     stop playing:
    #         if music:
    #             music.stop()
    #     queue song:
    #         qh.enqueue(song)
    #     music.finished:
    #         qh.finished(song)
    #         if qh.current:
    #             play(qh.current)
    """
