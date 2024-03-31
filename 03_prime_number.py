# https://www.geeksforgeeks.org/c-program-to-check-whether-a-number-is-prime-or-not/

'''

Prime Number Program in C
A prime number is a natural number greater than 1 that is completely divisible only by 1 and itself. For example, 2, 3, 5, 7, 11, etc. are the first few prime numbers.

'''

import math
n = int(input())
n1 = math.sqrt(n)
is_prime = True
for i in range(2,int(n1)):
    if(n%i == 0):
        is_prime = False
        break
print(is_prime)