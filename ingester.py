import csv
import uuid
import pdb
from collections import OrderedDict



# ----- Objects ----->
class Event:
    def __init__(self, name):
        self.name = name
        self.color = None       # will be changed by the coloring algorithm
        self.students = 0
        self.valence = 0
        self.conflicts = []
        self.eventConflicts = []

    def __str__(self):
        ans = self.name
        for c in self.conflicts:
            ans = ans + " " + c
        return ans


class User:
    def __init__(self, name):
        self.name = name
        self.conflicts = []

    def __str__(self):
        ans = self.name
        for c in self.conflicts:
            ans = ans + " " + c
        return ans


class Graph:
    def __init__(self, firstNode):
        self.nodes = [firstNode]

    def addEvent(self, newEvent):
        '''
        Takes an event and adds all conflicts to the graph if they haven't already been accounted for.
        '''
        for event in self.nodes:
            for person in newEvent.conflicts:
                if person in event.conflicts:   # check if a person (conflict) appears in both
                    # add conflict to both
                    if event not in newEvent.eventConflicts:
                        newEvent.eventConflicts.append(event)
                        newEvent.valence += 1
                    if newEvent not in event.eventConflicts:
                        event.eventConflicts.append(newEvent)
                        event.valence += 1
        self.nodes.append(newEvent)



# ----- Methods ----->
def importData(name):
    '''
    importData takes a CSV filename and parses it into a list of rows.
    '''
    csv_file = open(name, mode='r')
    csv_reader = csv.reader(csv_file)
    ans = []
    for line in csv_reader:
        ans.append(line)

    return ans

def buildUsers(usersRaw):
    '''
    Generates user objects based off the dataset given.
    '''
    users = OrderedDict()
    for u in usersRaw:
        users[u] = User(u)
    del users[""]
    return users


def buildEvents(data):
    '''
    Generates events objects based off the dataset given.
    '''
    events = OrderedDict()
    for line in data:
        events[line[0]] = Event(line[0])
    return events


def buildConflicts(data, events, users):
    '''
    Reads the conflict matrix and populates each event with conflicts in the form of a list of Users that conflict.
    Also appends information about how many students are required for the event.
    '''
    userKeys = list(users.keys())
    for row in data:
        event = events[row[0]]
        for i,col in enumerate(row[1:]):
            if i == 0:
                event.students = col
            if col == '1':
                event.conflicts.append(users[userKeys[i]])
    return


def buildGraph(events):
    '''
    Builds an undirected graph datastructure with events as nodes and edges as conflicts.
    '''
    keys = list(events.keys())
    g = Graph(events[keys[0]])
    for event in events:
        g.addEvent(events[event])
    return g


def printGraph(graph):
    '''
    Pretty printer function to display graph.
    '''
    for node in graph.nodes:
        print("CONFLICT --------->", node.name)
        for c in node.eventConflicts:
            print(c.name, c.color, c.valence)


def prepareDataStructure(file):
    '''
    Builds the data structure.
    '''
    data = importData(file)
    users = buildUsers(data[0])
    events = buildEvents(data[1:])

    buildConflicts(data[1:], events, users)

    graph = buildGraph(events)
    return graph


if __name__ == "__main__":
    graph = prepareDataStructure('Data/dataset.csv')
    printGraph(graph)
