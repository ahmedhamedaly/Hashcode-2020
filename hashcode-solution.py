import re
import random

def sortBooks(books):
     books.sort(key = lambda tuple : tuple[1], reverse = True)
     return books
class library:

    def __init__(self, amount, sTime, bShip, bList):
        sortBooks(bList)
        self.amount = amount
        self.sTime = sTime
        self.bList = sortBooks(bList)
        self.bShip = bShip
        self.output = []

    def addToOutput(self, bookId):
        self.output.append(bookId)
        
    def containsBook(self, bookId):
        if(self.bList.contains(bookId)):
           return bookId
        return -1
    def removeBook(self, bookId):
        self.bList = [i for i in self.bList if i[0] != bookId]

def sortLibraries(libraries):
    libraries.sort(key=lambda lib: lib.sTime)


lib1 = library(5,2,2, [(0, 1), (1, 2), (2, 3), (3, 6), (4, 5)])
lib2 = library(4,3,1, [(3, 6), (2, 3), (5, 4), (0, 1)])
lib3 = library(2,4,1, [(3, 6), (2, 3)])
libs = [lib1, lib3, lib2]
sortLibraries(libs)
libs[0].removeBook(1)
for lib in libs:
    print(f'lib: {lib.amount}')
    for tup in lib.bList:
        print(tup)
#file1 = open('a_example.in', "r")
