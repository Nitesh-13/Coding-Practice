# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

'''

Let's define a function countUniqueChars(s) that returns the number of unique characters in s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

'''
# Solution needs to be revised
s = input()

def generate_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings

sub = generate_substrings(s)
print(sub)
out = 0
for string in sub:
    str = [x for x in string]
    if (len(set(str)) == len(str)):
        out += len(str)
print(out)