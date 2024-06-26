# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

'''

Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.

'''

n = int(input())
print(hex(n).replace('0x','') if n >= 0 else "ffffffff")

# Need to revise manual method