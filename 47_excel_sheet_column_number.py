# https://leetcode.com/problems/excel-sheet-column-number/description/

'''

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

'''

str = input()
num = 0

n = len(str)
for ind, chr in enumerate(str):
    num = (ord(chr)-64) + num*26
print(num)