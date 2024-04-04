# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

'''

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

'''

nums = [-1,-2,-3,-4]
n = len(nums)
if n < 3:
    print(-1)
else:
    nums.sort()
    print(max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])) # Second condition for edge case 2 max negatives and 1 positive