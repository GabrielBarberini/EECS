def print_path(path):
    """ Assumes path is a list of nodes """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, to_print = False):
    path = path + [start]
    if to_print:
        print('Current DFS path: ', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path
    return shortest

def shortest_path(graph, start, end, to_print = False):
    return DFS(graph, start, end, [], None, to_print)
