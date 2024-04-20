# 

'''

Consider the following series: 1,1,2,3,4,7,8,15,9,24,16,40,32,72,104,27...
This series is a mixture of 3 series -
    - All the prime position values are power of 2
    - All the perfect square position are power of 3
    - Remaining positions are sum of previous 2 values

for example if N = 15, the 15th term in the series is 104, so only value 104 should be printed to STDOUT.
You can assume that N will not exceed 40.

Input:
15
Output:
104

Input:
9
Output:
9

'''

import math

def is_prime(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True

keys = [x for x in range(1,41)]
series = dict.fromkeys(keys,0)
series[1] = 1
series[2] = 1
pwr_2 = 1
pwr_3 = 1

# Generating series upto 40, as mentioned in the question, N wont exceed 40 for the input
for i in range(3,41):
    if is_prime(i):
        pwr_2 *= 2
        series[i] = pwr_2
    elif int(math.sqrt(i))*int(math.sqrt(i)) == i:
        pwr_3 *= 3
        series[i] = pwr_3
    else:
        series[i] = series[i-1] +series[i-2]

n = int(input())
print(series[n])