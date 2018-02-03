import csv
import os
import time

if(not os.path.exists('Data.txt')): 
    print('Data doesn\'t exist!')
    exit()

filePath = 'Results\\' + time.strftime('%Y-%m-%d %H-%M-%S') + '.csv' #This gives the time in YYYY-MM-DD HH-MM-SS, example: 2018-2-2 18-30-17

open(filePath, 'a').close()


data = open('Data.txt', 'r')
outputFile = open(filePath, 'w', newline='')

outputWriter = csv.writer(outputFile)

linesPerRow = int(data.readline())

print('Lines per row ' + str(linesPerRow))



linesRead = 0
thingToWrite = []

timesThroughLoop = 1

for line in data:
    print(timesThroughLoop)
    timesThroughLoop += 1
    thingToWrite += [line[:-1]]

    linesRead += 1


    if linesRead == linesPerRow:
        linesRead = 0

        outputWriter.writerow(thingToWrite)

        print('Wrote ' + str(thingToWrite))

        thingToWrite = []

        

data.close()
outputFile.close()