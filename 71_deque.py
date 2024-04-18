# https://www.geeksforgeeks.org/deque-in-python/

'''

Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.

'''

from collections import deque

nums = deque([1, 2, 3, 4, 5])
shiftby = 4
shift_to_right = False # Change shifting direction from here

# Manual
# for i in range(shiftby):
    # if shift_to_right:
    #     num = nums.pop()
    #     nums.appendleft(num)
    # else:
    #     num = nums.popleft()
    #     nums.append(num)
    
if shift_to_right:
    nums.rotate(shiftby)
else:
    nums.rotate(len(nums)-shiftby)
print(list(nums))