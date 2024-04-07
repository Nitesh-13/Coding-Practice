# https://www.geeksforgeeks.org/print-array-after-it-is-right-rotated-k-times/

'''

Given an Array of size N and a value K, around which we need to right rotate the array. How do you quickly print the right rotated array?

'''

nums = [1, 2, 3, 4, 5]
n = 4
size = len(nums)
for i in range(n):
    nu = nums.pop(size-1)
    nums.insert(0, nu)
print(nums)