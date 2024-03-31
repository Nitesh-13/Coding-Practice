# https://leetcode.com/problems/climbing-stairs/

'''

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

def countWays(n):
    if n == 0 or n == 1:
        return 1
    return countWays(n-1) + countWays(n-2)

n = int(input())
print(countWays(n))
