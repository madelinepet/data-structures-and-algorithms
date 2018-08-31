from typing import Any


class Node:
    def __init__(self, val: Any, _next=None):
        """ Initializes the class with value, and a next that can be a
        """
        self.val = val
        self._next = _next

    def __str__(self):
        """ Returns a string
        """
        return f'{self.val}'

    def __repr__(self):
        """ Returns a more highly formatted string
        """
        return f' <Node | Val: {self.val} | Next: {self._next}>'


class Animal(object):
    def __init__(self, type=None, _next=None):
        self.type = type
        self._next = _next


class AnimalShelter(object):
    """ This creates a queue class with methods below, used for animals in an
    animal shelter
    """
    def __init__(self, potential_iterable=None):
        """ Initializes fn, defines datatype as always a node, = "type annotation"
        """
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

    def enqueue(self, type):
        """Takes in an animal and creates new nodes in the queue's end, if
        there is no front, animal being added becomes the front
        """
        to_add = Animal(type)
        if not self.front:
            self.front = to_add
        else:
            iter_animal = self.front
            while iter_animal._next is not None:
                iter_animal = iter_animal._next
            iter_animal._next = to_add
            self.back = iter_animal
        self._length += 1

    def dequeue(self, preferred_animal=None):
        """ Dequeues animal of owner's preference
        """
        if self._length < 1:
            return('No items in queue!')
        if preferred_animal == 'dog' or preferred_animal == 'cat':
            iter_animal = self.front
            while iter_animal._next.type is not None:
                if iter_animal._next.type == preferred_animal:
                    self._length -= 1
                    return_node = iter_animal._next.type
                    iter_animal._next = iter_animal._next._next
                    return return_node
                else:
                    iter_animal = iter_animal._next
        elif self.front.type == preferred_animal or preferred_animal is None:
            temp = self.front
            self.front = temp._next
            self._length -= 1
