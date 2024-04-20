#

'''

Given an array of integers, find an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. If no such index exists, return -1.

Input: [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explaination: Index 3 is an equilibrium index because the sum of elements on the left, -7+1+5=-1, is equal to the sum of elements on the right, -4+3+0=-1.

'''

def equilibrium_index(arr, sum):
    left_sum = 0
    n = len(arr)
    for i in range(n):
        if sum - arr[i] - left_sum == left_sum:
            return i
        else:
            left_sum += arr[i]
    
    return -1
    
arr = input().split(' ')
sum = 0
for i, x in enumerate(arr):
    arr[i] = int(x)
    sum += int(x)
print(equilibrium_index(arr, sum))