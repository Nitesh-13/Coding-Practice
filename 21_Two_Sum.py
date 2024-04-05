# https://leetcode.com/problems/two-sum/description/

'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

'''

arr = [2,7,11,15]
t = 9
n = len(arr)

# O(n^2) Approach

# found = False
# for i in range(n):
#     for j in range(n):
#         if arr[i] + arr[j] == t:
#             found = True
#             print(i,j)
#             break
#     if found:
#         break


numHash = {}

for index, element in enumerate(arr):
    numHash[element] = index
    
for index, element in enumerate(arr):
    rem = t - element
    if rem in numHash and numHash[rem] != index:
        print(numHash[rem], numHash[element])
        break
