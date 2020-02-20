import re
import random


class library:
    def __init__(self, amount, sTime, bShip, bList):
        self.amount = amount
        self.sTime = sTime
        self.bList = sortBooks(self, bList)
        self.bShip = bShip
    def sortBooks(self, books):
        self.bList.sort(key = lambda tuple : tuple[1])

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
