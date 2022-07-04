import graph
from depth_first_search import shortest_path
from depth_first_search import print_path 

sample_graph = graph.Graph()
long_node_path = [graph.Node("A"), graph.Node("B"), graph.Node("C"), graph.Node("D"), graph.Node("E")]
short_node_path = [graph.Node("BL"), graph.Node("CL")]
edges = [ graph.Edge(long_node_path[0], long_node_path[1]), graph.Edge(long_node_path[1], long_node_path[2]), 
          graph.Edge(long_node_path[2], long_node_path[3]), graph.Edge(long_node_path[3], long_node_path[4]), 
          graph.Edge(long_node_path[0], short_node_path[0]), 
          graph.Edge(short_node_path[0], short_node_path[1]),
          graph.Edge(short_node_path[1], long_node_path[4])
        ]

for node in long_node_path:
    sample_graph.add_node(node)
for node in short_node_path:
    sample_graph.add_node(node)

for edge in edges:
    sample_graph.add_edge(edge)

print("Shortest path is: " + print_path(shortest_path(sample_graph, long_node_path[0], long_node_path[4], True)))

