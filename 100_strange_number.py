# 

'''

Numbers are everywhere around us. We deal with different types of numbers on a daily basis.
There are real numbers, whole numbers, natural numbers, etc. Another kind of numbers is called strange numbers, which has the following properties: 
- A strange numberis an integer number 'N' which has factors that are prime numbers.
- The square root of the number 'N' should be less than the greatest prime factor of 'N'.

The task here is to find out if the given number 'N' is "Strange" Or "Not Strange".

Input:
15
Output:
Strange

Input:
25
Output:
Not Strange

'''
import math
def returnfactors(n):
    
    factors = []
    for i in range(2, n+1):
        if n% i == 0:
            factors.append(i)
    return factors

def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if n%i == 0:
            return False
    return True

def primefactors(n):
    primeFactors = []
    factors = returnfactors(n)
    for factor in factors:
        if isprime(factor):
            primeFactors.append(factor)
    return primeFactors

n = int(input())
half1 = False
half2 = False
factors = returnfactors(n)
p = []
for factor in factors:
    if isprime(factor):
        p.append(factor)

if len(p) > 0:
    half1 = True

pfactors = primefactors(n)
if int(math.sqrt(n)) < pfactors[-1]:
    half2 = True

if half1 and half2:
    print('Strange')
else:
    print('Not Strange')