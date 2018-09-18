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


class Graph:
    def __init__(self):
        """ Initializes the graph class as an empty dict
        """
        self.graph = {}

    def __repr__(self):
        """ Returns a technical representation of the graph's details
        """
        return(f'Graph: {self.graph}')

    def __str__(self):
        """ Returns a string representation of the graph's details
        """
        return f'{self.graph}'

    def __len__(self):
        """ Returns the length of the graph
        """
        return len(self.graph)

    def add_vert(self, val):
        """ add vertice to self.graph, check to see if the vert already exists:
        if so raise exception create a helper method
        """
        if self.has_vert(val):
            raise LookupError
        self.graph[val] = {}

    def has_vert(self, val):
        """ checks for a key in the graph
        """
        if val in self.graph:
            return True
        else:
            return False

    def add_edge(self, v1, v2, weight):
        """ add a relationship and weight between two verts, don't forget to validate
        """
        if self.has_vert(v1) and self.has_vert(v2):
            try:
                if self.graph[v1][v2]:
                    raise LookupError
            except KeyError:
                self.graph[v1][v2] = weight

    def get_neighbors(self, val):
        """ Given a val (key), return all all adjacent verts, return empty
        list if no neighbors
        """
        if self.has_vert(val):
            return self.graph[val].keys()
        else:
            return([])

    def breadth_first_traversal(self, root=None):
        """ Accepts a starting node and returns a collection of nodes in the
        order they were visited.
        """
        try:
            if root is None:
                return []
            queue = Queue()
            visited = {root: True}
            output = []
            queue.enqueue(root)
            while len(queue) > 0:
                value = queue.dequeue()
                output.append(value)
                for node in self.graph[value]:
                    try:
                        visited[node]
                    except KeyError:
                        queue.enqueue(node)
                        visited[node] = True
            return output
        except KeyError:
            return []
