# https://www.geeksforgeeks.org/binary-search/

'''

Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

'''

def bin_search(arr, target):
    start = 0
    end = len(arr)-1
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1
    return -1
    
arr = [2, 3, 4, 10, 40]
x = 5

print(bin_search(arr, x))