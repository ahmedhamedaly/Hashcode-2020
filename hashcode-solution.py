import re
import random


def main():
    dataFile = "a_example.txt"
    with open(dataFile) as file:
        dataLines = file.readlines()

        data = [line.strip() for line in dataLines]

        bkLibScan = [int(i) for i in data[0].split()]

        books = bkLibScan[0]
        libraries = bkLibScan[1]
        daysForScan = bkLibScan[2]

        scores = [int(i) for i in data[1].split()]

        scoreDict = {}
        for index in range(len(scores)):
            scoreDict[index] = scores[index]

        scoreList = [(scoreDict[score], score) for score in scoreDict]

        for index, lib in enumerate(data[2:], start=1):
            if index % 2 is 0:
                amount = int(data[index][0])
                sTime = int(data[index][2])
                bShip = int(data[index][4])
                bList = [(int(lib.split()[i]), scoreDict[i]) for i in range(len(lib.split()))]

                print(f"{amount}, {sTime}, {bShip}, {bList}\n")
                library(amount, sTime, bShip, bList)


class library:
    def __init__(self, amount, sTime, bShip, bList):
        self.amount = amount
        self.sTime = sTime
        self.bList = sortBooks(self, bList)
        self.bShip = bShip
        self.bList = bList

    def sortBooks(self, books):
        self.bList.sort(key=lambda tuple: tuple[1])

    def containsBook(self, bookId):
        if (self.bList.contains(bookId)):
            return bookId
        return -1

    def removeBook(self, bookId):
        self.bList = [i for i in self.bList if i[0] != bookId]


def sortLibraries(libraries):
    libraries.sort(key=lambda lib: lib.sTime)


# file1 = open('a_example.in', "r")

print("hey")

if __name__ == '__main__':
    main()