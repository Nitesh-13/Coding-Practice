# https://www.geeksforgeeks.org/print-characters-frequencies-order-occurrence/

'''

Given string str containing only lowercase characters. The problem is to print the characters along with their frequency in the order of their occurrence and in the given format explained in the examples below.
Input : str = "geeksforgeeks"
Output : g2 e4 k2 s2 f1 o1 r1

'''

from collections import Counter
str = input()
freq = Counter(str)
print(dict(freq))
for i in freq:
    print(f"{i}{freq[i]}", end=" ")
print("\n")