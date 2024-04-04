# https://geeksforgeeks.org/find-all-factors-of-a-natural-number-in-sorted-order/

'''

Find all factors of a Natural Number in sorted order

'''

n = int(input())
output = []
for i in range(1,n+1):
    if(n%i == 0):
        output.append(i)
print(output)
