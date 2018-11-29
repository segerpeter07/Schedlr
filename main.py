import csv
import uuid
import pdb
from collections import OrderedDict



# ----- Objects ----->
class Event:
    def __init__(self, name):
        self.name = name
        self.students = 0
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



if __name__ == "__main__":
    data = importData('Data/dataset.csv')
    users = buildUsers(data[0])
    events = buildEvents(data[1:])

    buildConflicts(data[1:], events, users)
    
    
    eventsKeys = list(events.keys())
    print(eventsKeys[0])
    data = events[eventsKeys[0]]
    conflicts = data.conflicts
    for conflict in conflicts:
        print(conflict)
    print(data.students)