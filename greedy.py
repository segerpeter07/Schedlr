from ingester import prepareDataStructure, printGraph


def greedy(graph):
    """
    Takes a graph and colors itself using a greedy algorithmic approach.
    """
    color_list = list(range(len(graph.nodes)))

    for node in graph.nodes:
        available_colors = color_list
        for conflict in node.eventConflicts:
            if conflict.color in available_colors:
                available_colors.remove(conflict.color)
        node.color = available_colors[0]


def countColors(graph):
    '''
    Takes a Graph obj and counts how many colors are used to color it.
    '''
    colors = []
    for node in graph.nodes:
        for c in node.eventConflicts:
            if c.color not in colors:
                colors.append(c.color)
    return len(colors)


if __name__ == "__main__":
    # get file name
    graph = prepareDataStructure('Data/dataset.csv')

    greedy(graph)
    print("NUMBER OF COLORS: ", countColors(graph))
