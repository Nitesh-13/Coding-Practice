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

lcm = math.lcm(d1,d2)

do = lcm
no = min(n1,n2)*lcm + max(n1,n2)
print(f'{no}/{do}')

# Need Logic Fixing