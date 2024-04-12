# https://leetcode.com/problems/valid-anagram/

'''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''

s = input()
t = input()
# O(nLogn)
# print(sorted(s) == sorted(t))

# O(N)
from collections import Counter
freq_s = Counter(s)
freq_t = Counter(t)
print(freq_s == freq_t)