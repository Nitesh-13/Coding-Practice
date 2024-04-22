#

'''

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

123
456
989

The left-to-right diagonal = 1+5+9 = 15, The right to left diagonal = 3+5+9 = 17, Their absolute difference is [15-17] = 2

Sample Input:
3
11 2 4
4 5 6
10 8 -12

Sample Output:
15

'''

n = int(input())
ldiag = 0
rdiag = 0
for i in range(n):
    for j in range(n):
        ele = int(input())
        if i == j:
            ldiag += ele
        if i+j == n-1:
            rdiag += ele
print(abs(ldiag-rdiag))
