# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

'''

The idea of Kadane's algorithm is to maintain a variable max_ending_here that stores the maximum sum contiguous subarray ending at current index and a variable max_so_far stores the maximum sum of contiguous subarray found so far, Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if it is greater than max_so_far.

Input: [-2, -3, 4, -1, -2, 1, 5, -3]
Output: 7

'''

arr = list(map(int, input().split(' ')))

maxi = float('-inf')
sum = 0

# Finds only the maximum sum from all subarrays
# for element in arr:
#     sum += element
#     maxi = max(sum, maxi)
#     sum = max(sum,0)

# Finds subarrray with maximum sum
subarr = []
for element in arr:
    sum += element
    subarr.append(element)
    if sum > maxi:
        maxi = sum
    maxi = max(sum, maxi)
    if sum < 0:
        sum = 0
        subarr.clear()

print(maxi, subarr)

# Just carry the sum forward only if its positive