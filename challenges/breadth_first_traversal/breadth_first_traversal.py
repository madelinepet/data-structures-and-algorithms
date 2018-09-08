
class Node(object):
    def __init__(self, value, data=None, left=None, right=None):
        """ Instantiates the first Node
        """
        self.value = value
        self.data = data
        self.left = left
        self.right = right
        self._next = None

    def __str__(self):
        """ Returns a string
        """
        return f'{self.value}'

    def __repr__(self):
        """ Returns a more highly formatted string
        """
        return f' <Node | Value: {self.value} | Data: {self.data} | Left: {self.left} | Right: {self.right} | Next: {self._next}>'


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
        return f'{self.value}'

    def __repr__(self):
        """ Technical representation of the BinaryTree
        """
        return f' <Node | Value: {self.root.value} | Root : {self.root}>'

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
            if val < current.value:
                if current.left is None:
                    current.left = new_node
                    return False
                else:
                    current = current.left
            if val > current.value:
                if current.right is None:
                    current.right = new_node
                    return False
                else:
                    current = current.right

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
        self.front = None
        self.back = None
        self._length = 0

        if isinstance(potential_iterable, (list, tuple)):
            for x in potential_iterable:
                self.enqueue(x)

    def __str__(self):
            """ Returns a string of the top and the length
            """
            return f'{self.front} | {self.back}| {self._length}'

    def __repr__(self):
        """ Returns a formatted string of the top and the length of the queue
        """
        return f'<Queue | Front: {self.front} | Back: {self.back}| Length : {self._length}>'

    def __len__(self):
        """ Returns the length of the queue
        """
        return self._length

    def enqueue(self, input):
        """Takes in an iterable and creates new nodes in the queue's end
        """
        new_node = Node(input)
        if not self.front:
            self._length += 1
            self.front = new_node
            self.back = new_node
        else:
            self._length += 1
            temp = self.back
            self.back = new_node
            temp._next = self.back

    def dequeue(self):
        if self.front:
            self._length -= 1
            temp = self.front
            self.front = temp._next
            temp._next = None
            return temp.value
        return('No items in queue!')


def traverse_breadth_first(bt):
    """ Return all the nodes on each level of a binary tree
    """
    queue = Queue()
    output = []
    queue.enqueue(bt.root)
    if queue.front is None:
        return('Your bt was empty!')
    while len(queue) > 0:
        if queue.front.value.left is not None:
            queue.enqueue(queue.front.value.left)
        if queue.front.value.right is not None:
            queue.enqueue(queue.front.value.right)
        output.append(queue.dequeue().value)
    return output
