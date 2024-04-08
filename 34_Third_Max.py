# https://leetcode.com/problems/third-maximum-number/description/

'''

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

'''

nums = [1,2]
nums = list(set(nums))
nums.sort(reverse = True)
if len(nums)>=3:
    print(nums[2])
else:
    print(nums[0])
