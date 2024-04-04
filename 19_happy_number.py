# https://leetcode.com/problems/happy-number/description/

'''

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

'''

n = input()
nums = [int(x) for x in n]
sum = 0
outs = []
while True:
    for element in nums:
        sum += (element*element)
    if sum == 1:
        print(True)
        break
    if sum in outs:
        print(False)
        break
    outs.append(sum)
    nums = [int(x) for x in str(sum)]
    sum = 0