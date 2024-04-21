# 

'''

Given an n x n matrix and an integer x, find the position of x in the matrix if it is present. Otherwise, print "Element not found". Every row and column of the matrix is sorted in increasing order. The designed algorithm should have linear time complexity. 

Input1: mat[4][4] = [[10, 20, 30, 40], 
                     [15, 25, 35, 45],
                     [27, 29, 37, 48],
                     [32, 33, 39, 50]]
        x=29
Output1: Found at (2, 1)
Explanation: Element at (2,1) is 29


Input 2:mat[4][4] = {{10, 20, 30, 40},
                     {15, 25, 35, 45},
                     {27, 29, 37, 48},
                     {32, 33, 39, 50}}
        x=100
Output2: Element not found
Explanation: Element 100 does not exist in the matrix

'''


n = int(input())
mat = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(int(input()))
    mat.append(temp)
x = int(input())
ind = 0
for i in range(n):
    if mat[i][0] > x:
       ind = i-1
       break
if x in mat[ind]:
    print((ind,mat[ind].index(x)))
else:
    print('Element not found')