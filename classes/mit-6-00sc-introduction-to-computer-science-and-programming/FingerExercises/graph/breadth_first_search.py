import graph
from depth_first_search import print_path

def BFS(graph, start, end, to_print = False):
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)
        if to_print:
            print('Current BFS path:', print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None
    
