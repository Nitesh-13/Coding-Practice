# TCS NQT 20 Aug 2022

'''

Vijay, an industrialist recently opened a fuel industry . There are N numbers of different category of fuels and each fuel is stored in a fixed size container. Size of each container can vary from fuel to fuel .

Hari, a fuel merchant, Visited Vijay's Industry and he wanted to purchase fuels for his shop. Hari has a limited amount of money (K) and wants to buy fuel. Hari will not buy more than one container of any fuel category. Hari wants to maximize the overall volume i.e sum of volume of fuels he buys. Your task is to get the maximum overall volume of fuels which Hari can purchase

Given the number of categories of fuels (N) money units (k) price of container of each category of fuel and volume contained in container for each category,

NOTE Quantity (volume) of container will be given in the same order as of the price.

Example 1:
Input :
5
105
10 10 40 50 90 -> prices
10 20 20 50 150 -> container
Output :
170

Example 2:
Input :
5
100
10 20 30 40 100
10 20 30 40 100

'''

def returnSubSequence(sequence, output, index = 0):
    if len(sequence) == 0:
        return [output] if output else []
    
    sub_with_element = returnSubSequence(sequence[1:], output + [(index,sequence[0])], index+1)
    sub_without_element = returnSubSequence(sequence[1:], output, index+1)
    
    return sub_with_element+sub_without_element


n = int(input())
k = int(input())
prices = []
containers = []
for i in range(n):
    prices.append(int(input()))
for i in range(n):
    containers.append(int(input()))
subprices = returnSubSequence(prices, [])
volume = 0
for price in subprices:
    pricecollection = [t[1] for t in price]
    indices = [t[0] for t in price]
    if sum(pricecollection) <= k:
        volume = max(volume, sum([containers[t] for t in indices]))
print(volume)



