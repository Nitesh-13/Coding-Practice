# https://www.scaler.com/topics/maximum-subarray-sum/

'''

We are given an array A of size N which consists of both positive and negative integers. We have to write a program to find the Maximum Sum of Subarray.

Note: A subarray is a contiguous part of an Array.

'''

arr = [-2, 5, 2, -3]
n = len(arr)
maxSum = float('-inf')

for i in range(n):
    tsum = 0
    for j in range(i,n):
        tsum += arr[j]
        maxSum = tsum if maxSum < tsum else maxSum
        
print(maxSum)