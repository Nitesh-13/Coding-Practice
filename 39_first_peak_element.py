# https://leetcode.com/problems/find-peak-element/

'''

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

'''

nums = [1,2,1,3,5,6,4]
for index, element in enumerate(nums):
    if(element > nums[index-1] and element > nums[index+1]):
        print(index)
        break