# https://leetcode.com/problems/find-common-characters/

'''

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

'''
from collections import Counter
words = ["cool","lock","cook"]
out = set(words[0])
for i in range(1,len(words)):
    out = out & set(words[i])
freq = dict.fromkeys(list(out),float('inf'))

for word in words:
    for chr in freq.keys():
        freq[chr] = min(freq[chr], word.count(chr))

out = list(Counter(freq).elements())
print(out) 
