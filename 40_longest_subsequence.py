# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

'''

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

'''

nums = [2,2,2,2]
count = 1
old = 0
sub = []
for index, element in enumerate(nums):
    if index == 0:
        old = element
        continue
    if element > old:
        count += 1
        old = element
    elif count != 0:
       sub.append(count)
       count = 0
print(max(sub))