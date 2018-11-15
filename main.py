import csv
import uuid
import pdb


def anonymizeUser(anonUsers, user):
    '''
    This function takes a list of users with potentially repeated repeated names and creates
    a dictionary which mapps a UUID to a common name
    '''
    uuidKey = str(uuid.uuid4())
    anonUsers[uuidKey] = user
    return uuidKey, anonUsers


def importData(name):
    '''
    importData takes a CSV filename and parses it into a list of classes, a dictionary of anonymized userId:course selection,
    and a dictionary of anonymized userId:user name
    '''
    csv_file = open(name, mode='r')
    csv_reader = csv.reader(csv_file)
    ans = []
    for line in csv_reader:
        ans.append(line)
    
    classes = ans[0][1::]
    usersList = ans[1::]
    usersDict = {}
    
    anonUsers = {}
    for user in usersList:
        id, anonUsers = anonymizeUser(anonUsers, user[0])
        usersDict[id] = user[1::]

    return classes, anonUsers, usersDict


def buildClassMatrix(users):
    '''
    buildClassMatrix takes a dictionary of users and class selections and builds a matrix of them
    '''
    mtx = []
    for user in users:
        mtx.append(users[user])

    return mtx


if __name__ == "__main__":
    classes, anonUsers, usersDict = importData('Data/generatedData.csv')
    print(classes)
    id = list(anonUsers)
    # print(anonUsers[id[0]])
    # print(usersDict[id[0]])
    classMtx = buildClassMatrix(usersDict)
    print(classMtx)