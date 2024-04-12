# https://www.geeksforgeeks.org/sort-string-characters/

'''

Given a string of lowercase characters from 'a' - 'z'. We need to write a program to print the characters of this string in sorted order.

Examples: 

Input : bbccdefbbaa 
Output : aabbbbccdef

'''

str = input()
str = [chr for chr in str]
str.sort()
print("".join(str))