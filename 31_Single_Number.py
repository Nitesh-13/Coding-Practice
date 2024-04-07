# https://leetcode.com/problems/single-number/

'''

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

'''

nums = [5,1,5,4,1]
x = 0
for element in nums:
    x ^= element
print(x)
