# https://www.geeksforgeeks.org/selection-sort/

'''

Selection Sort:
    - Time Complexity: O(N2)
    - Auxiliary Space: O(1)

'''

arr = [64, 34, 25, 12, 22, 11, 90]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        cur_min = i
        for j in range(i+1,n):
            ptr = j
            if arr[cur_min] > arr[ptr]:
                cur_min = ptr
            
        arr[i], arr[cur_min] = arr[cur_min], arr[i]
    
    print(arr)

selection_sort(arr)