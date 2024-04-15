# https://www.geeksforgeeks.org/merge-sort/

'''

Merge Sort:
    - Time Complexity: O(NLogN)
    - Auxiliary Space: O(N)

'''

arr = [64, 34, 25, 12, 22, 11, 90]

def merge(arr1, arr2):
    arr3 = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] > arr2[0]:
            arr3.append(arr2[0])
            arr2.pop(0)
        else:
            arr3.append(arr1[0])
            arr1.pop(0)
    
    while len(arr1) != 0:
        arr3.append(arr1[0])
        arr1.pop(0)
        
    while len(arr2) != 0:
        arr3.append(arr2[0])
        arr2.pop(0)
        
    return arr3

def merge_sort(arr):
    n = len(arr)
    
    if n == 1:
        return arr
    
    arr1 = arr[0:n//2]
    arr2 = arr[(n//2):n]
    
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    
    return merge(arr1,arr2)

print(merge_sort(arr))