# https://www.geeksforgeeks.org/program-for-mean-and-median-of-an-unsorted-array/

'''

Given an unsorted array a[] of size N, the task is to find its mean and median. 

'''
import statistics

nums = [4, 4, 4, 4, 4]
nums.sort()
mean = statistics.mean(nums)
median = statistics.median(nums)
print(mean, median)