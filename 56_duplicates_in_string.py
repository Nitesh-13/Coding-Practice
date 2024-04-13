# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

'''

Given a string S, the task is to print all the duplicate characters with their occurrences in the given string.

'''

from collections import Counter
s = input()
s = [x for x in s]
sFreq = Counter(s)
print([f'{chr} - {cnt}' for chr,cnt in sFreq.items() if sFreq[chr] >= 2])