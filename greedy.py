from main import prepareDataStructure

# get file name
graph = prepareDataStructure('Data/dataset.csv')

def greedy(graph):
    """
    Takes a graph and colors itself.
    """
    color_list = list(range(len(graph.nodes)))

    for node in graph.nodes:
        available_colors = color_list
        for conflict in node.eventConflicts:
            if conflict.color in available_colors:
                available_colors.remove(conflict.color)
        node.color = available_colors[0]

def printGraph(graph):
    for node in graph.nodes:
        print("CONFLICT --------->", node.name)
        for c in node.eventConflicts:
            print(c.name, c.color)
