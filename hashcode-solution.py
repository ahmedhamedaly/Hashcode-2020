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

class library:
    def __init__(self, amount, sTime, bShip, bList):
        self.amount = amount
        self.sTime = sTime
        self.bShip = bShip
        self.bList = bList
    
    def sortBooks(self, books):
        return 0
    
    def containsBook(self, bookId):
        if(self.bList.contains(bookId)):
           return bookId
        return -1
    



if __name__ == '__main__':
    main()