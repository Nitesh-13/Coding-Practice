# https://www.geeksforgeeks.org/perfect-number/

'''

Perfect Number
A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. Write a function to check if a given number is perfect or not. 

'''

n = int(input())
divisors = []

for i in range(1,n):
    if n%i == 0:
        divisors.append(i)
print(sum(divisors) == n)