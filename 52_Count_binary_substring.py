# https://leetcode.com/problems/count-binary-substrings/

'''

Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

'''

str = input()
n = len(str)
zero, one, res = 0,0,0
for i in range(n):
    if(str[i] == '0'):
        if(i > 0 and str[i-1] != '0'):
            zero = 1
        else:
            zero += 1
        
        if zero<=one:
            res += 1
    else:
        if(i > 0 and str[i-1] != '1'):
            one = 1
        else:
            one += 1
        
        if one<=zero:
            res += 1

print(res)