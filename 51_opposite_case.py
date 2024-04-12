# https://www.geeksforgeeks.org/convert-alternate-characters-string-upper-case/

'''

Given a string, convert the characters of the string into the opposite case,i.e. if a character is the lower case then convert it into upper case and vice-versa. 

'''

str = input()
str = "".join([chr.swapcase() for chr in str])
print(str)