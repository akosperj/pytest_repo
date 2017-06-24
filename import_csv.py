import csv

with open('MSFT.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    mylist = list(readCSV)
    print(mylist)
