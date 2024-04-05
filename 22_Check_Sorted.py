# https://www.geeksforgeeks.org/program-check-array-sorted-not-iterative-recursive/

'''

Given an array of size n, write a program to check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

'''

arr = [20, 23, 23, 45, 78, 88, 79]
print("Yes") if (arr == sorted(arr)) else print("No")