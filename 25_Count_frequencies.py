# https://www.geeksforgeeks.org/counting-frequencies-of-array-elements/

'''

Given an array which may contain duplicates, print all elements and their frequencies.

'''

arr = [10, 20, 20, 10, 10, 20, 5, 20]
map = {}

for element in arr:
    if element in map:
        map[element] += 1
    else:
        map[element] = 1

for key in map.keys():
    print(f'{key} - {map[key]}')