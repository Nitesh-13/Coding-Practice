# TCS NQT 2024 26 April Slot 1
# https://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/

'''

Given an unsorted array of integers, find a subarray that adds to a given number.
If there is more than one subarray with the sum of the given number, print any of them.

'''

arr = [1, 4, 20, 3, 10, 5]
k = 33
n = len(arr)


# O(N^2) Approach
# subarrs = []
# for i in range(n):
#     for j in range(i,n):
#         subarrs.append(arr[i:j+1])
# for arr in subarrs:
#     if sum(arr) == k:
#         print(arr)

# O(N) Approach
sumMap = {}
cursum = 0
for i in range(n):
    cursum += arr[i]
    
    if cursum == k:
        print(arr[0:i+1])
        break
    
    if (cursum - k) in sumMap:
        print(arr[sumMap[cursum-k]+1:i+1])
        break
    
    sumMap[cursum] = i
