# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

'''

A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

'''
from collections import Counter

s1 = "this apple is sweet"
s2 = "this apple is sour"
s1 = s1.split()
s2 = s2.split()
c1 = Counter(s1)
c2 = Counter(s2)
s1 = [x for x in s1 if c1[x] == 1]
s2 = [x for x in s2 if c2[x] == 1]
print(list(set(s1) ^ set(s2)))