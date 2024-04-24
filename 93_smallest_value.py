#

'''

Write a program to find smallest integer value b for a given value of a . If we multiply the digits of b , We should get exact value of a . Result b must contain more than one digit.

Constraints :
1 <=a<=10000

Example 1:
10
Output :
25
Explanation = 2*5 = 10

Example 2:
100
Output :
455
Explanation = 4*5*5 = 100

'''

n = int(input())
i = 10
while True:
    nums = [int(x) for x in str(i)]
    su = 1
    for nu in nums:
        su *= nu
    if su == n:
        print(i)
        break
    i += 1