import networkx as nx
import matplotlib.pyplot as plt
from main import prepareDataStructure


def createNxGraph(graph):
    G = nx.Graph()
    for node in graph.nodes:
        # edges = []
        for edge in node.eventConflicts:
            # edges.append(edge.name)
            G.add_edge(node.name, edge.name)
        # G.add_edge(node.name, edges)
    return G


def drawGraph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels = False, node_color='blue', edge_color='black', width=1, alpha=0.5)


if __name__ == "__main__":
    graph = prepareDataStructure('Data/dataset.csv')

    # for node in graph.nodes:
    #     print("CONFLICT --------->", node.name)
    #     for c in node.eventConflicts:
    #         print(c.name)

    G = createNxGraph(graph)
    drawGraph(G)
    plt.show()