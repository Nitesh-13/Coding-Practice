# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

'''

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

'''

s = "azxxzy"
out = []

for ind, chr in enumerate(s):
    out.pop() if (len(out) != 0 and out[-1] == chr) else out.append(chr)

print("".join(out))