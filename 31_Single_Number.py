# https://leetcode.com/problems/single-number/

'''

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

'''

# New Approach needed

nums = [2,2,1]
n = len(nums)
str = ""
newStr = ""
mx = max(nums)
for i in range(mx+1):
    str += "0"
for element in nums:
    if str[element] == "0":
        newStr = str[:element] + "1" + str[element+1:]
    else:
        newStr = str[:element] + "2" + str[element+1:]
    str = newStr

print(str[str.find("1")])