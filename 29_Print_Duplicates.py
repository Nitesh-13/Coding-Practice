# https://geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

'''

Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and use only constant memory space.
Note: The repeating element should be printed only once.

'''

# Need a better approach

nums = [1, 2, 3, 6, 3, 6, 1]
nums.sort()

for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        print(nums[i])