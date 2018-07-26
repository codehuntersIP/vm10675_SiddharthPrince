import sys
len = int(sys.stdin.readline())
numArr = sys.stdin.readline().strip()
numArr = numArr.split(',')

# print(type(len), type(numArr), numArr)
# print(type(numArr[0]))
def b6(val, base):
    res = ''
    while val > 0:
        res = str(val % base) + res
        # val /= base # only valid for Py2
        val //= base  # for getting integer division
    if res: return res
    return '0'

def convB6():

    b6Arr = []
    for num in numArr:
        b6Num = b6(int(num), 6)
        # print(type(binNum))
        b6Arr.append(b6Num)
        print(b6Arr)
    return b6Arr

def digitSum(no):
    suM = 0
    while len(no) != 0:
        suM += no % 10
        no = no // 10
    return suM

def digiSum(b6List):
    b6Sum = []
    for b6Num in b6List:
        # print(b6Num)
        theSum = digitSum(b6Num)
        b6Sum.append(theSum)
    return b6Sum

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

convBase6 = convB6()
sumOfDigits = digiSum(convBase6)
# print(len(onesList))
numberOfInvertions = numOfInv(sumOfDigits)
# print(convBinary)
# print(onesList)
print(numberOfInvertions)