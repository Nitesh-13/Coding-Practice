# https://leetcode.com/problems/add-digits/description/

'''

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

'''

n = input()
nums = [int(nu) for nu in list(n)]
sum = 0
while True:
    for element in nums:
        sum = sum + element
    if sum >= 10:
        nums = [int(nu) for nu in list(str(sum))]
        sum = 0
    else:
        break
    
# print((n%9)+1 if n!= 0 else 0) - O(1) Approach
print(sum)