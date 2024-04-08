# https://www.geeksforgeeks.org/sort-elements-by-frequency/

'''

Print the elements of an array in the decreasing frequency if 2 numbers have the same frequency then print the one which came first

'''

nums = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]

numsFreq = dict.fromkeys(nums, 0)

for element in nums:
    numsFreq[element] += 1

sortedDict = dict(sorted(numsFreq.items(), key=lambda x: x[1], reverse= True))
nums.clear()

for key in sortedDict.keys():
    for i in range(sortedDict[key]):
        nums.append(key)

print(nums)