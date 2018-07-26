import sys

m, n = map(int, sys.stdin.readline().split(','))

nums = [[j for j in sys.stdin.readline().split(',')] for i in range(m)]


def lastArrNum(newM):
    # Returns a list of the first numbers in each chute
    lastNums = []
    i = 0
    while i < newM:
        lastNums.append(int(nums[i][len(nums[i])-1]))
        i += 1
    #print(lastNums)
    return lastNums

def maxInRow():
    # To get the maximum number in a chute in order to determine which chute to choose when 2 max numbers are the same.
    rowMaxArr = []
    for arr in nums:
        rowMaxArr.append(int(max(arr)))
    #print(rowMaxArr)
    return rowMaxArr

def ifSameMaxLastNums(rowMax, indLastNums):
    # Determines the chute to choose when more than one chute has the same max number next.
    max, maxPos, i = 0, 0, 0
    while i < len(indLastNums):
        if rowMax[indLastNums[i]] > max:
            maxPos = indLastNums[i]
            max = rowMax[indLastNums[i]]
        i += 1
    return maxPos

def solve(lastNumbs):
    # This is the method that computes the final maximum value that can be formed.
    global nums, maxNumPos
    maxNum = max(lastNumbs)
    maxCount = lastNumbs.count(maxNum)
    if maxCount == 1:
        maxNumPos = lastNumbs.index(maxNum)
    else:
        rowMaxArray = maxInRow()
        indices = [index for index in range(len(lastNumbs)) if lastNumbs[index] == maxNum]
        maxNumPos = ifSameMaxLastNums(rowMaxArray, indices)

    nums[maxNumPos] = nums[maxNumPos][:(len(nums[maxNumPos])-1)] # Removes the chosen number from the list representing the chosen chute.
    if len(nums[maxNumPos]) == 0:
        nums = nums[:maxNumPos] + nums[maxNumPos+1:] # This eliminates a chute from the 2D array if it is empty.
    return maxNum

ansArr = []

while len(nums) != 0:
    lastNums = lastArrNum(len(nums))
    currentGreatest = solve(lastNums)
    ansArr.append(str(currentGreatest))
    #print(ansArr, nums)

ans = ''.join(ansArr) # To convert the answer list into a single string that is the maximum value
print("Largest integer that could be formed is ", int(ans))
