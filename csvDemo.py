import csv

with open('utilities/loans.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    #print(list(csvReader))
    names = []
    stats = []
    for row in csvReader:
        #print(row[1])
        names.append(row[0])
        stats.append(row[1])
    print(names)
    print(stats)
    Index = names.index('Sam')
    loanStatus = stats[Index]
    print('Sam loan status is '+loanStatus)

# with open('utilities/loans.csv','a') as wFile:
#     write = csv.writer(wFile)
#     write.writerow(['Bob','rejected'])
