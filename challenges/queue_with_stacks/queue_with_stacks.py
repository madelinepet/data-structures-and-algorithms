from typing import Any
import pytest


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
        return f' <Node | Val: {self.val | Next: self._next}>'


class Stack(object):
    """ This creates a stack class with methods below
    """
    def __init__(self, potential_iterable=None):
        """ Initializes fn, defines datatype as always a node, = "type annotation"
        """
        self.top: Node = None
        self._length: int = 0
        if potential_iterable is not None:
            try:
                for i in potential_iterable:
                    self.pop(i)
            except TypeError:
                self.pop(potential_iterable)

    def __str__(self):
            """ Returns a string of the top and the length
            """
            return f'{self.top} | Length: {self._length}'

    def __repr__(self):
        """ Returns a formatted string of the top and the length of the stack
        """
        return f'<Stack | Top: {self.top} | Length : {self._length}>'

    def __len__(self):
        """ Returns the length of the stack
        """
        return self._length

    def push(self, val):
        """ Creates a new node for any item in an iterable and adds the value to the top of the stack
        """
        self.top = Node(val, self.top)
        self._length += 1
        return self.top

    def pop(self):
        """ takes no arguments and removes and returns the Node at the top of the stack. First, set tempoaray to top, set the new top to the temporary's next, set the temporary to have no next now to avoid breaking stack, return the value
        """
        temporary = self.top
        self.top = temporary._next
        temporary._next = None
        self._length -= 1
        return temporary.val

    def peek(self):
        """ Takes no arguments and returns the whole node at the top of the stack without mutating stack
        """
        return self.top


class Queue(object):
    def __init__(self):
        self.top = None
        self.back = None

    def enqueue(self, val):
        stack_one = Stack(val)
        stack_two = Stack(val)
        for i in stack_two:
            stack_one.push(stack_two.pop())
        return stack_one.push(val)

    def dequeue(self):
        stack_one = Stack(self.val)
        stack_two = Stack(self.val)
        for i in stack_one:
            stack_two.push(stack_one.pop())
        return stack_two.pop()





