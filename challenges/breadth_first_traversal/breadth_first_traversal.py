
class Node(object):
    def __init__(self, value, data=None, left=None, right=None):
        """ Instantiates the first Node
        """
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """ String representation of the Node
        """
        pass

    def __repr__(self):
        """ Technical representation of the Node
        """
        pass


class BinaryTree:
    def __init__(self, iterable=None):
        """ Instatiates the first BinaryTree
        """
        self.root = None
        if iterable:
            for i in iterable:
                self.insert(i)

    def __str__(self):
        """ String representation of the BinaryTree
        """
        pass

    def __repr__(self):
        """ Technical representation of the BinaryTree
        """
        pass

    def insert(self, val):
        """ Given root node, go left or right, get to child, go left, right or
        insert? Does not need to be self balancing.
        """
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if val == current.value:
                raise ValueError('Value is already in the tree')
            if val > current.value:
                if current.right is None:
                    current.right = new_node
                    return False
                else:
                    current = current.right
            if val < current.value:
                if current.left is None:
                    current.left = new_node
                    return False
                else:
                    current = current.left

    def in_order(self, callable=lambda node: print(node)):
        """ Go left, visit, go right.
        """
        def _walk(node=None):
            """ recursion! Function calls itself. The recursion needs to know
            when to stop. The return here acts at the base case when the node
            is None
            """
            if node is None:
                return

            # go left
            if node.left is not None:
                _walk(node.left)

            # visit, runs lambda and prints the node
            callable(node)

            # go right
            if node.right is not None:
                _walk(node.right)

        # call walk for the first time and pass in the root
        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """ Visit, go left, go right
        """
        def _walk(node=None):
            """ recursion! Function calls itself. The recursion needs to know
            when to stop. The return here acts at the base case when the node
            is None
            """
            if node is None:
                return
            # visit, runs lambda and prints the node
            callable(node)

            # go left
            if node.left is not None:
                _walk(node.left)

            # go right
            if node.right is not None:
                _walk(node.right)

        # call walk for the first time and pass in the root
        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
            """ Go left, go right, visit
            """
            def _walk(node=None):
                """ recursion! Function calls itself. The recursion needs to know
                when to stop. The return here acts at the base case when the
                node is None
                """
                if node is None:
                    return
                # go left
                if node.left is not None:
                    _walk(node.left)

                # go right
                if node.right is not None:
                    _walk(node.right)
                # visit, runs lambda and prints the node
                callable(node)

            # call walk for the first time and pass in the root
            _walk(self.root)

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


def traverse_breadth_first(Node, root):
    """ Return all the nodes on each level of a binary tree
    """

    breadth = Queue()
    breadth.enqueue(root)

    while breadth.head is not None:
        front = breadth.dequeue()
        print(front.Value)
        if (front.left is not None):
            breadth.enqueue(front.left)
        if (front.right is not None):
            breadth.enqueue(front.right)


