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
            scoreDict[scores[index]] = index

        scoreList = [(scoreDict[score], score) for score in scoreDict]

        for index, lib in enumerate(data[2:], start=1):
            print(f"{lib} and {index}")
            if index % 2 is 1:
                print("hello")

def sortBooks(books):
     books.sort(key = lambda tuple : tuple[1], reverse = True)
class library:
    def __init__(self, amount, sTime, bShip, bList):
        sortBooks(bList)
        self.amount = amount
        self.sTime = sTime
        self.bList = bList
        self.bShip = bShip

    def containsBook(self, bookId):
        if(bList.contains(bookId)):
           return bookId
        return -1
    def removeBook(self, bookId):
        self.bList = [i for i in self.bList if i[0] != bookId]
    
def sortLibraries(libraries):
    libraries.sort(key=lambda lib: lib.sTime)

#file1 = open('a_example.in', "r")

print("hey")
