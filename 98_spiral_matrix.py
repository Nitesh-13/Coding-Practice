# 

'''

Input a 2D matrix, print all elements in spiral format .

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]
while matrix:
    print(*matrix.pop(0), end = " ")
    matrix = [list(row) for row in zip(*matrix)][::-1]
