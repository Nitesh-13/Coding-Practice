# https://www.geeksforgeeks.org/bubble-sort/

'''

Bubble Sort:
    - Time Complexity: O(N2)
    - Auxiliary Space: O(1)

'''

arr = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)

bubble_sort(arr)