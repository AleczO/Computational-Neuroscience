import networkx as nx
import matplotlib.pyplot as plt
import random

Graph = nx.complete_graph(3, nx.DiGraph)

for node in Graph.nodes():
    Graph.add_edge(node, node)

for (u, v) in Graph.edges():
    Graph.edges[u, v]['weight'] = 1

print(Graph.edges.data('weight'))

nx.draw(Graph)

plt.show()