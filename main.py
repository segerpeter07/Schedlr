import csv


def importData(name):
    csv_file = open(name, mode='r')
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)


if __name__ == "__main__":
    importData('Data/generatedData.csv')