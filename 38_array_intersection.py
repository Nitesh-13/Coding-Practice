# https://leetcode.com/problems/intersection-of-two-arrays/

'''

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

'''

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# O(N^2) Approach
# out = list(set(filter(lambda x: nums2.count(x)>0, nums1)))
# print(out)

# O(N) space and time Approach
set1 = set(nums1)
set2 = set(nums2)
out = list(set1.intersection(set2))
print(out)