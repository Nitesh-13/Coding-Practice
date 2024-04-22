# TCS NQT 24 Aug 2022

'''

Jack and Jill are playing a string game . Jack has given gill 2 strings A&B. Jill has to derive string C from A, by deleting elements from string A, such that string C does not contain any elements of string B.

Jill needs help to do this task, she wants you to write a program.
Given String A and B as input derive string C.

Input 1:
Tiger
Ti
Output 1:
ger

Input 2:
processed 
esd
Output 2:
proc

'''

str1 = input()
str2 = input()
str1 = [x for x in str1]
str2 = [x for x in str2]
difference = set(str1) -set(str2)
out = ''
for chr in str1:
    if chr in list(difference):
        out+= chr
print(out)
