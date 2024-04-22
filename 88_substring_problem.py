# TCS NQT 30 Oct 2022

'''

Alice has a very unique problem . He has a string which contain elements for 0 to 9. Find the number of substring of the string where sum of elements of the substring is not equal to the length of substring

Input 1:
3 -> length of string
201 -> string
Output 1 :
3

'''

n = int(input())
str1 = input()
substr = []
for i in range(n):
    for j in range(i,n):
        substr.append([int(x) for x in str1[i:j+1]])

count = 0

for sub in substr:
    if sum(sub) != len(sub):
        count += 1

print(count)

