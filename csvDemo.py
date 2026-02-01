import csv

with open('utilities/loans.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])
    print(names)
    print(stats)
    Index = names.index('Sam')
    loanStatus = stats[Index]
    print('Sam loan status is '+loanStatus)
