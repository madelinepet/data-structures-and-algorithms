class Node:
    def __init__(self, val, _next=None):
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


class Stack(object):
    """ This creates a stack class with methods below
    """
    def __init__(self, potential_iterable=None):
        """ Initializes fn, defines datatype as always a node, = "type annotation"
        """
        self.top: Node = None
        self._length: int = 0
        if potential_iterable is iter:
            try:
                for i in potential_iterable:
                    self.pop(i)
            except TypeError:
                self.pop()

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
        """ Creates a new node for any item in an iterable and adds the value
        to the top of the stack
        """
        self.top = Node(val, self.top)
        self._length += 1
        return self.top

    def pop(self):
        """ takes no arguments and removes and returns the Node at the top of
        the stack. First, set tempoaray to top, set the new top to the
        temporary's next, set the temporary to have no next now to avoid
        breaking stack, return the value
        """
        temporary = self.top
        self.top = temporary._next
        temporary._next = None
        self._length -= 1
        return temporary.val

    def peek(self):
        """ Takes no arguments and returns the whole node at the top of the
        stack without mutating stack
        """
        return self.top


class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return(f'Graph: {self.graph}')

    def __str__(self):
        return f'{self.graph}'

    def __len__(self):
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

    def depth_first_graph(self, start, x=lambda x: print(x)):
        """ Visit, go left until you can't any more, and then go right
        """
        explored = []
        output = []
        explored.append(start)
        stack = Stack()
        stack.push(start)
        while stack._length:
            output.append(stack.pop())
            for neighbor in self.graph[output[-1]].keys():
                if neighbor not in explored:
                    stack.push(neighbor)
                    explored.append(neighbor)
        return output
