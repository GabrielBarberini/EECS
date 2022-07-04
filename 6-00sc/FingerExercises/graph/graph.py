class Node(object):
    """ assumes name is a string """
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def __str__(self):
        return self._name

class Edge(object):
    """ assumes src and dest are nodes """
    def __init__(self, src, dest):
        self._src = src
        self._dest = dest
    def get_source(self):
        return self._src
    def get_destination(self):
        return self._dest
    def __str__(self):
        return self._src.get_name() + '->' + self._dest.get_name()

class Digraph(object):
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph') 
        self._edges[src].append(dest)

    def children_of(self, node):
        return self._edges[node]

    def has_node(self, node):
        return node in self._nodes

class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)
