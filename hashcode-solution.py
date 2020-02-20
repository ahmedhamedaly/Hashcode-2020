import re
import random


class library:
    def __init__(self, amount, sTime, bShip, bList):
        self.amount = amount
        self.sTime = sTime
        self.bShip = bShip
        self.bList = bList
    
    def sortBooks(self, books):
        self.bList.sort(key = lambda tuple : tuple[1])
    
    def containsBook(self, bookId):
        if(bList.contains(bookId)):
           return bookId
        return -1
    

#file1 = open('a_example.in', "r")

print("hey")
