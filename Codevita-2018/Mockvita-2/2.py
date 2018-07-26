import sys
len = int(sys.stdin.readline())
numArr = sys.stdin.readline().strip()
numArr = numArr.split(',')

# print(type(len), type(numArr), numArr)
# print(type(numArr[0]))
def convBin():

    binArr = []
    for num in numArr:
        binNum = bin(int(num))
        # print(type(binNum))
        binArr.append(binNum[2:])
    return binArr

def count1s(binList):
    binCount = []
    for binNum in binList:
        binCount.append(binNum.count('1'))
    return binCount

def numOfInv(derivedList):
    # print(len(derivedList))
    # initNum = derivedList[0]
    inversionCount, i = 0, 0
    while i < len:
        j = i + 1
        while j < len:
            if derivedList[i] > derivedList[j]:
                inversionCount += 1
            j += 1
        i += 1
    return inversionCount

convBinary = convBin()
onesList = count1s(convBinary)
# print(len(onesList))
numberOfInvertions = numOfInv(onesList)
print(convBinary)
print(onesList)
print(numberOfInvertions)