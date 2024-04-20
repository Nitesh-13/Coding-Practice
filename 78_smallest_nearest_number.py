#

'''

Given an array of integers, find the nearest smallest number for every element such that the smaller element is on the left side.
Input: {1,6,4,10,2,5}
Output: {-1,1,1,4,1,2}

Input: {3,2,1}
Output: {-1,-1,-1}

'''

def nearest_smallest(arr):
    nearest = [-1]
    n = len(arr)
    small = arr[0]
    smallest = []
    for i in range(1,n):
        if i >= 2:
            for j in range(i-1,-1,-1):
                if arr[j] < arr[i]:
                    smallest.append(arr[j])
            if smallest:
                small = smallest[0]
                smallest.clear()
        if arr[i] > small:
            nearest.append(small)
        else:
            nearest.append(-1)
    return nearest
    
arr = input().split(' ')
arr = [int(x) for x in arr]

print(nearest_smallest(arr))