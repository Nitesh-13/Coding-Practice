# https://www.geeksforgeeks.org/remove-characters-from-the-first-string-which-are-present-in-the-second-string/

'''

Given two strings string1 and string2, remove those characters from the first string(string1) which are present in the second string(string2). Both strings are different and contain only lowercase characters.
NOTE: The size of the first string is always greater than the size of the second string( |string1| > |string2|).

'''

string1 = "occurrence"
string2 = "car"
out = ""
for ind, chr in enumerate(string1):
    if chr not in string2:
        out += chr
print(out)