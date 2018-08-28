import pytest

from .node import Node


class Queue(object):
    """ This creates a queue class with methods below
    """
    def __init__(self, potential_iterable=None):
        """ Initializes fn, defines datatype as always a node, = "type annotation"
        """
        self.queue = list()
        self.front = None
        self.back = None
        self._length: int = 0

    def __str__(self):
            """ Returns a string of the top and the length
            """
            return f'{self.front} | {self.back}| Length: {self._length}'

    def __repr__(self):
        """ Returns a formatted string of the top and the length of the queue
        """
        return f'<Queue | front: {self.front} | back: {self.back}| Length : {self._length}>'

    def __len__(self):
        """ Returns the length of the queue
        """
        return self._length

    def enqueue(self, potential_iterable):
        """Takes in an iterable and creates new nodes in the queue's end
        """
        if potential_iterable is iter:
            try:
                for i in potential_iterable:
                    if i not in self.queue:
                        self.queue.insert(0, i)
                        self._length += 1
                        return True
                    else:
                        return False
            except TypeError:
                self.insert(0, potential_iterable)
        else:
                self.queue.insert(0, potential_iterable)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
            self._length -= 1
        return('No items in queue!')







