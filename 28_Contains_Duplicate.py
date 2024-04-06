# https://leetcode.com/problems/contains-duplicate/description/

'''

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''

nums = [1,1,1,3,3,4,3,2,4,2]
out = False
for element in nums:
    if nums.count(element) > 1:
        out = True
        break
print(out)