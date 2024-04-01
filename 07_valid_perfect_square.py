# https://leetcode.com/problems/valid-perfect-square/description/

'''

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

'''

import math
n = int(input())
sqrt = int(math.sqrt(n))
print((sqrt*sqrt == n))

# Need to revise manual logic for sqrt (cant rely on library)