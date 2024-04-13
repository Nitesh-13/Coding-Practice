# https://www.geeksforgeeks.org/count-common-subsequence-in-two-strings/

'''

Given two string S and T. The task is to count the number of the common subsequence in S and T.

Examples:

Input : S = “ajblqcpdz”, T = “aefcnbtdi” 
Output : 11 
Common subsequences are : { “a”, “b”, “c”, “d”, “ab”, “bd”, “ad”, “ac”, “cd”, “abd”, “acd” }

'''

def generate_subsequences(s):
    if len(s) == 0:
        return ['']
    subseq_without_first = generate_subsequences(s[1:])
    subseq_with_first = [s[0] + subseq for subseq in subseq_without_first]

    return subseq_with_first + subseq_without_first

s = input()
t = input()
out = 0
sList = [x for x in s]
tList = [x for x in t]
for element in s:
    if element not in t:
        sList.remove(element)

for element in t:
    if element not in s:
        tList.remove(element)
        
sSub = set(generate_subsequences("".join(sList)))
tSub = set(generate_subsequences("".join(tList)))

print(len(sSub & tSub)-1)