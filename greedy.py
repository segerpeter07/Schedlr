from ingester import prepareDataStructure, printGraph


def greedy(graph):
    """
    Takes a graph and colors itself using a greedy algorithmic approach.
    """
    # color_list = list(range(len(graph.nodes)))

    for node in graph.nodes:
        available_colors = list(range(len(graph.nodes)))
        for conflict in node.eventConflicts:
            if conflict.color in available_colors:
                available_colors.remove(conflict.color)
        node.color = available_colors[0]

def print_nodes(graph):
    """
    Prints nodes and their valence.
    """
    for node in graph.nodes:
        print(node.name, node.valence)

def countColors(graph):
    '''
    Takes a Graph obj and counts how many colors are used to color it.
    '''
    colors = []
    for node in graph.nodes:
        if node.color not in colors:
            colors.append(node.color)
    return len(colors)


if __name__ == "__main__":
    # get file name
    # graph = prepareDataStructure('Data/dataset.csv')
    graph = prepareDataStructure('Data/allConflicts.csv')

    print_nodes(graph)
    greedy(graph)
    print("NUMBER OF COLORS: ", countColors(graph))
