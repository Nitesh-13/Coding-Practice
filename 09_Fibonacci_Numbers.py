# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

'''

Nth Fibonacci Number
Given a number n, print n-th Fibonacci Number. 

'''

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))