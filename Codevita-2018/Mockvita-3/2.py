import sys
from collections import Counter

numArr = sys.stdin.readline().strip()
numArrInt = map(int, numArr.split(','))

time = ""
data = dict(Counter(numArrInt)) # https://stackoverflow.com/questions/2600191/how-to-count-the-occurrences-of-a-list-item

def filler():
    numList = [1,2,3,4,5,6,7,8,9,0]
    for num in numList:
        if num in data:
            continue
        else:
            data[num] = 0

def checkIfPossible():
    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        print("Impossible")
        exit(0)

filler()
checkIfPossible()

hhmmss = [2,9,5,9,5,9]
i = 0
while len(time) != 6:
    if data[hhmmss[i]] == 0 and hhmmss[i] != 0:

        if time == "24":
            if data[0] >= 4:
                time += "0000"
                break
            else:
                time = "2"
                hhmmss[1] = 3
                data[4] += 1
                i -= 1
        else:
            hhmmss[i] -= 1

    else:

        if hhmmss[i] == 2 and i == 0:
            hhmmss[1] = 4

        time += str(hhmmss[i])
        # print(time)
        data[hhmmss[i]] -= 1
        i += 1

maxTime = time[:2] + ":" + time[2:4] + ":" + time[4:]
print(maxTime.strip())