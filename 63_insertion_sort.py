# https://www.geeksforgeeks.org/insertion-sort/

'''

Insertion Sort:
    - Time Complexity: O(N2)
    - Auxiliary Space: O(1)

'''

arr = [64, 34, 25, 12, 22, 11, 90]

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1,n):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1] ,arr[j] = arr[j], arr[j-1]
            j -= 1

    print(arr)

insertion_sort(arr)