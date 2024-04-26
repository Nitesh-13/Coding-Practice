# TCS NQT 2024 26 April Slot 1
# https://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/

'''

Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to reach (m, n). At
any instance, if you are on (x, y), you can either goto (x,y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space are marked as 1 and 0 respectively in the grid.

'''


def checkPath(i,j,m,n, matrix):

    if i == m or j == n:
        return 0
    if matrix[i][j] == 1:
        return 0
    if i == m-1 and j == n-1:
        return 1

    p1 = checkPath(i+1,j,m,n, matrix)
    p2 = checkPath(i,j+1,m,n, matrix)
    
    return p1+p2

    

matrix = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

print(checkPath(0,0,3,3,matrix))