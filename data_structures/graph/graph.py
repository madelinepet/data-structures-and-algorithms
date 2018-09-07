class Vertice:
    def __init__(self, value):
        self.value = value
        # self.vertices is essentially neighbors
        self.vertices = {}

    def __repr__(self):
        pass

    def __str__(self):
        pass


class Graph():
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def add_vert(self, val):
        """ Use val to create a new vertice, add that vertice to the graph,
        check if to see if the vert already exists, if so, raise an exception in a helper method
        """

    def has_vert_already(self, val):
        """ Helper method that checks for a key in the graph
        """
        pass

    def add_edge(self, vert1, vert2, weight):
        """ Adds a new edge connecting vert1 and vert 2 with weight, check if
        the edge already exists
        """
        pass

    def get_neighbors(self, val):
        """ Given a key, return all the adjacent verts
        """
        pass

