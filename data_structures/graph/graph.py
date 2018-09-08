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
        """ add vertice to self.graph, check to see if the vert already exists: if so raise exception create a helper method
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
