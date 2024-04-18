# https://www.geeksforgeeks.org/subarraysubstring-vs-subsequence-and-programs-to-generate-them/

'''

A subarray is a contiguous part of the array. An array that is inside another array. For example, consider the array [1, 2, 3, 4], There are 10 non-empty sub-arrays. The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.

'''

arr = [1, 2, 3, 4] # Just use string instead of array for for substring
n = len(arr)

subarrays = []

for i in range(n):
    for j in range(i,n):
        subarrays.append(arr[i:j+1])
        
print(subarrays)