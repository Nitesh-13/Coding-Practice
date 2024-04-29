# TCS NQT 2024 April 29

'''

List of max elements in contiguous sub-array of given k from main array

Input: 
3,6,7,1,6,3
3
Output:
7 7 7 6
Explanation: Maximum element in contiguous sub-array of size 3
in first subarray of size 3 [3,6,7] max is 7
in next subarray of size 3 [6,7,1] max is 7...

'''

arr = list(map(int,input().split(',')))
n = int(input())
out = []
for ind, element in enumerate(arr):
    if ind+3 == len(arr)+1: break
    out.append(max(arr[ind:ind+n]))
print(out)