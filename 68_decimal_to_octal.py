# https://www.geeksforgeeks.org/program-decimal-octal-conversion/

'''

Given a decimal number as input, we need to write a program to convert the given decimal number into an equivalent octal number. i.e convert the number with base value 10 to base value 8.

'''

n = int(input())
print(oct(n).replace('0o',''))