# 

'''
A chocolate factory is packing chocolates into packets. The chocolate packets here represent an array of N number of integer values. The Task is to find the empty packets(0) of chocolate and push it to end of the conveyer belt. 

Input 1: N = 8, arr = [4, 5, 0, 1, 9, 0, 5, 0 ] 
Output 1 : [4 5 1 9 5 0 0 0]

Input 2: N = 6, arr = [0,0,1,2,4,5]
Output 2: [1,2,4,5,0,0]
'''

from collections import deque

def push_bach_empty_packets(arr,n):
    filled = 0
    for i in range(n):
        if arr[i] != 0:
            arr[filled] = arr[i]
            filled += 1
    for i in range(filled,n):
        arr[i] = 0
    return arr

def pack_chocolates(arr):
    que = deque(arr)
    for _ in range(len(que)):
        if que[0] == 0:
            que.rotate(-1)
        else:
            que.rotate(1)
    return list(que)

n = int(input())
arr = input().split(' ')
arr = [int(x) for x in arr]
print(pack_chocolates(arr))