# https://www.geeksforgeeks.org/permutations-to-arrange-n-persons-around-a-circular-table/

'''

Permutations to arrange N persons around a circular table
Given N, the number of persons. The task is to arrange N person around a circular table.

'''
import math
n = int(input())
print(math.factorial(n-1))

'''
Permutation
nPr = n!/(n-r)!

Circular Permutation
P = (n-1)!

Combination
nCr = n!/r!(n-r)!
'''