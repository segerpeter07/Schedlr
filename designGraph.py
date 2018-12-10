import networkx as nx
import matplotlib.pyplot as plt
from ingester import prepareDataStructure
from welsh_powell import welshPowell, countColors
from greedy import greedy
from generateSchedule import generateSchedule


def createNxGraph(graph):
    '''
    Creates a networkx graph based off the given Graph object.
    '''
    G = nx.Graph()
    for node in graph.nodes:
        # edges = []
        if node.eventConflicts == []:
            G.add_node(node.name)
        else:
            for edge in node.eventConflicts:
                # edges.append(edge.name)
                G.add_edge(node.name, edge.name)
            # G.add_edge(node.name, edges)
    return G

def buildColorDict(graph):
    '''
    Builds a dictionary of node name:color number based off the given Graph object.
    '''
    res = {}
    for node in graph.nodes:
        res[node.name] = node.color+1
    return res


def drawGraph(graph, colors):
    '''
    Takes a nx.Graph obj and a node name:color dictionary and draws the graph and colors it.
    '''
    pos = nx.spring_layout(graph)
    values = [colors.get(node, 'blue') for node in graph.nodes()]
    nx.draw(graph, pos, with_labels = False, node_color=values, edge_color='black', width=1, alpha=0.7)



if __name__ == "__main__":
    graph = prepareDataStructure('Data/allConflicts.csv')
    # graph = prepareDataStructure('Data/noConflicts.csv')
    # graph = prepareDataStructure('Data/dataset.csv')


    # Run coloring algorithm
    # greedy(graph)
    welshPowell(graph)

    # Count number of colors assigned
    print("Colors required: ", countColors(graph))
    

    # Build node name: color dictionary
    col_val = buildColorDict(graph)

    # print(col_val)

    # Build network
    G = createNxGraph(graph)


    # Draw graph and color it
    drawGraph(G, col_val)
    plt.show()

    # Optionally also generate a print out of the schedule
    generateSchedule(graph)