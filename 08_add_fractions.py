# https://www.geeksforgeeks.org/program-to-add-two-fractions/

'''

Program to add two fractions
Add two fraction a/b and c/d and print answer in simplest form.

'''
import math

n1 = int(input())
d1 = int(input())
n2 = int(input())
d2 = int(input())
n = n1*d2+n2*d1
d = d1*d2
gcd = math.gcd(n,d) # lcm = (a*b)/gcd
print(f'{int(n/gcd)}/{int(d/gcd)}')
