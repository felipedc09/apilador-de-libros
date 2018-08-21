import csv
 
def readFile(fileName):
    elements = []
    with open(fileName) as File:  
        reader = csv.reader(File, delimiter=';')
        for row in reader:
            elements.append(row)
    return elements