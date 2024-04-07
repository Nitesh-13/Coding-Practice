# https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/

'''

Find the smallest and second smallest elements in an array

'''

nums = [12, 13, 1, 10, 34, 1]

# O(N^2)

# mi = min(nums)
# seMin = mi
# nums.remove(mi)
# while True:
#     if seMin == min(nums):
#         nums.remove(seMin)
#     else:
#         seMin = min(nums)
#         break
# print(mi, seMin)


# O(NLogN)

# nums.sort(reverse=True)
# i = len(nums)-2
# mi = nums[i+1]
# seMi = 0
# while i>=0:
#     if nums[i] == mi:
#         i -= 1
#     else:
#         seMi = nums[i]
#         break
# print(mi,seMi)

# O(N) Approach
mi = float('inf')
seMi = 0

for element in nums:
    if element <= mi:
        if mi != element:
            seMi = mi
        mi = element
    elif element <= seMi:
        seMi = element
print(mi, seMi)