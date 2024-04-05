# https://leetcode.com/problems/pascals-triangle/description/

'''

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''

rows = int(input())
triangle = []

def getSubList(arr):
    nums = []
    for index, element in enumerate(arr):
        if index == len(arr)-1:
            break
        sum = element+arr[index+1]
        nums.append(sum)
    return nums

for i in range(rows):
    triangle.append([1])
    if i == 0: 
        continue
    elif i == 1:
        triangle[i].extend([1])
        continue
    else:
        nums = getSubList(triangle[i-1])
        triangle[i].extend(nums)
        triangle[i].extend([1])

print(triangle)
