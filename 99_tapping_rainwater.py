# 

'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9

'''

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len(arr)
subarr = []

def is_subarray(subarr, arr):
    n = len(subarr)
    m = len(arr)
    for i in range(m - n + 1):
        if arr[i:i + n] == subarr:
            return True
    return False
    
for i in range(n):
    if arr[i] == 0:
        continue
    
    for j in range(i+1,n):
            
        if arr[j] >= arr[i]:
            subar = arr[i:j+1]
            shouldAppend = True
            if len(subarr) > 0:
                shouldAppend = not is_subarray(subar, subarr[-1])
            if shouldAppend:
                subarr.append(subar)
            break

sum = 0
for arr1 in subarr:
    first = arr1[0]
    for i in range(1, len(arr1)):
        sum += (first-arr1[i] if (first-arr1[i]) >0 else 0)
print(sum)