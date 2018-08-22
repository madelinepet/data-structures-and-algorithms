import pytest

from .node import Node
from typing import Any


class LinkedList(object):
    """ This creates a linked list class with methods below
    """
    def __init__(self, potential_iterable=None):
        """ Initializes fn, defines datatype as always a node, = "type annotation"
        """
        self.head: Node = None
        self._length: int = 0
        if potential_iterable is not None:
            try:
                for i in potential_iterable:
                    self.insert(i)
            except TypeError:
                self.insert(potential_iterable)

    def __str__(self):
        """ Returns a string of the head and the length
        """
        return f'{self.head} | Length: {self._length}'

    def __repr__(self):
        """ Returns a formatted string of the head and the length of the linked list
        """
        return f'<Linked List | Head: {self.head} | Length : {self._length}>'

    def __len__(self):
        """ Returns the length of the ll
        """
        return self._length

    def __iter__(self):
        """ Iterates over the ll
        """
        pass

    def __next__(self):
        """ Iterates to the next item.
        """
        pass

    def insert(self, val: Any) -> Any:
        """ Insert something into the linked list. Any data type can be inserted (denoted by val: datatype), returns any datatype as output
        """
        new_node = Node(val, self.head)
        self.head = new_node
        self._length += 1
        return

    def includes(self, val: Any) -> bool:
        """ Checks to see if something in the list
        """
        current_node = self.head
        while current_node is not None:
            if current_node.val == val:
                return True
            current_node = current_node._next
        return False

    def append(self, val):
        """
        Similar to insert, but appends to end of LL
        """
        current = self.head
        while current._next is not None:
            current = current._next

        new_node = Node(val, _next=None)
        current._next = new_node

    def insert_before(self, val, target):
        """
        Inserts before a given value
        """
        if self.head.val == target:
            self.head = Node(val, self.head)
            return self.head
        else:
            current = self.head
            while current._next.val != target:
                current = current._next
            current._next = Node(val, current._next)
            return current._next

    def insert_after(self, val, target):
        """
        Inserts after a given value
        """
        current = self.head
        while current.val != target:
            current = current._next
        current._next = Node(val, current)
        return current._next
