# https://www.geeksforgeeks.org/program-decimal-binary-conversion/

'''

Given a decimal number as input, we need to write a program to convert the given decimal number into an equivalent binary number.

'''

n = int(input())
print(bin(n).replace('0b',''))