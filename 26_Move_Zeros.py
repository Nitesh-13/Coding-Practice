# https://leetcode.com/problems/move-zeroes/description/

'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

'''

nums = [0,1,0,3,12]
n = len(nums)

ptr = 0

for i in range(n):
    if nums[i] != 0:
        nums[ptr] = nums[i]
        ptr += 1

if ptr <= n-1:
    for i in range(ptr, n):
        nums[i] = 0

print(nums)