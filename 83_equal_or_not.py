# TCS NQT 18 Aug 2022

'''

Given Two binary numbers (in 0 and 1 ) in the form of string. Find out whether there is a possibility whether these numbers can become equal by rearranging their respective Os and 1s.
For ex: 101 and 011 can be arranged within themselves to become either 101 or 011.

Example 1:
3 -> length of input string
101 -> input string 1
011 -> input string 2

Output 1:
Yes

'''

n = int(input())
str1 = input()
str2 = input()
print('Yes' if sorted(str1) == sorted(str2) else 'No')