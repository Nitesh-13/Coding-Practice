# 

'''

TCS NQT Coding Question Day 3 Slot 2 - Question 1
A furnishing company is manufacturing a new collection of curtains. The curtains are of two colors aqua(a) and black (b). The curtains color is represented as a string(str) consisting of a's and b's of length N. Then, they are packed (substring) into L number of curtains in each box. The box with the maximum number of 'aqua' (a) color curtains is labeled. The task here is to find the number of 'aqua' color curtains in the labeled box.

Input :
bbbaaababa -> Value of str
3    -> Value of L

Output:
3   -> Maximum number of a's

'''

st = input()
n = int(input())

stlist = []
stlist.extend(st)
maxC = 0
count = 0
batch = 0
for element in stlist:
    batch += 1
    if element == 'a':
        count+=1
    if batch == n:
        batch = 0
        maxC = max(maxC, count)
        count = 0
maxC = max(maxC, count)
print(maxC)
    