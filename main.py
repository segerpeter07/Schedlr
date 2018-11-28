import csv
import uuid
import pdb
from collections import OrderedDict


class Event:
    def __init__(self, name):
        self.name = name
        self.conflicts = []
    
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


def importData(name):
    '''
    importData takes a CSV filename and parses it into a list of rows
    '''
    csv_file = open(name, mode='r')
    csv_reader = csv.reader(csv_file)
    ans = []
    for line in csv_reader:
        ans.append(line)

    return ans

def buildUsers(usersRaw):
    '''
    Does some stuff
    '''
    users = OrderedDict()
    for u in usersRaw:
        users[u] = User(u)
    del users[""]
    return users


def buildEvents(data):
    events = {}
    for line in data:
        events[line[0]] = Event(line[0])
    return events


def buildConflicts(data, events, users):
    populatedEvents = []
    userKeys = list(users.keys())
    for row in data:
        event = events[row[0]]
        for i,col in enumerate(row[1:]):
            if 



if __name__ == "__main__":
    # classes, anonUsers, usersDict = importData('Data/generatedData.csv')
    data = importData('Data/dataset.csv')
    users = buildUsers(data[0])
    events = buildEvents(data[1:])
    # for user in  users:
    #     print(user)
    buildConflicts(data[1:], events, users)