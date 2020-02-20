def optLib(libraries,days,bookAmount):
    bestLib = (0,0)
    for lib in libraries:
        runTime  = days - lib.sTime
        optScore = runTime * lib.bShip
        acc = min(optScore, len(lib.bList))
        curVal = 0
        for i in range(acc):
            curVal += lib.bList[i][1]
        score  = curVal * (lib.amount/bookAmount)
        if (score > bestLib[1]):
            bestLib = (libraries.index(lib),score)
    return bestLib




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
        libList = []
        for index, lib in enumerate(data[2:], start=1):
            if index % 2 is 0:
                amount = int(data[index][0])
                sTime = int(data[index][2])
                bShip = int(data[index][4])
                bList = [(int(lib.split()[i]), scoreDict[i]) for i in range(len(lib.split()))]

                print(f"{amount}, {sTime}, {bShip}, {bList}\n")
                libList.append(library(amount, sTime, bShip, bList))
        outList = []
        targetDay = 0
        pendingLibrary = 0
        for i in range(daysForScan):
            if (i == 0):
                libIndex = optLib(libList,daysForScan-i,books)[0]
                pendingLibrary = (libList[libIndex],libIndex)
                targetDay = i + libList[libIndex].sTime
                del libList[libIndex]
            if (i == targetDay):
                libIndex = optLib(libList,daysForScan-i,books)[0]
                outList.append(pendingLibrary)
                pendingLibrary = (libList[libIndex],libIndex)
                targetDay = i + libList[libIndex].sTime
                del libList[libIndex]
            
            for l in outList:
                print(l)
                for k in range(l[0].bShip):
                   temp = l[0].popBest()
                   for l1 in libList:
                       if(l1.containsBooks(temp[0])):
                           l1.bList.removeBook(temp[0])
                l[0].output.append(temp)

        for k1 in outList:
            print(f'{k1.amount}')
                        
            
            
            


    
            

        



def sortBooks(books):
    books.sort(key=lambda tuple: tuple[1], reverse=True)
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
        next((i for i, v in enumerate(self.bList) if v[0] == bookId), bookId)
        return -1

    def removeBook(self, bookId):
        cpyLen = len(self.bList)
        self.bList = [i for i in self.bList if i[0] != bookId]
        if(cpyLen > len(self.bList)):
            self.amount -= 1

    def popBest(self):
        if len(self.bList) == 0:
            return -1
        return self.bList.pop()


def sortLibraries(libraries):
    libraries.sort(key=lambda lib: lib.sTime)


lib1 = library(5, 2, 2, [(0, 1), (1, 2), (2, 3), (4, 5)])
lib2 = library(4, 3, 1, [(3, 6), (2, 3), (5, 4), (0, 1)])
lib3 = library(2, 4, 1, [(3, 6), (2, 3)])
libs = [lib1, lib3, lib2]
sortLibraries(libs)
libs[0].removeBook(1)
for lib in libs:
    print(f'lib: {lib.amount}')
    for tup in lib.bList:
       print(tup)
#lib = optLib(libs, 6, 5)
print(f'tuple {lib}')
main()