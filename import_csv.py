import csv

with open('MSFT.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    mylist = list(readCSV)
    print(mylist)

import csv

with open('MSFT.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0], row[1], row[2], )
        import csv
