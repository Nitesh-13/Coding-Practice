# TCS NQT 20 Aug 2022

'''

Bobs going to bet today on horse riding . There are N horses listed in a sequence of 1 to N.

The probability of winning of each horse is different so the prices for making a bet on the horses are not the same . There is no limit on the number of horses on which he can bet, but he thinks that if he bets on continuous sequence of horses then he has better chance of win.

Bob will get K units of money if any horse on which he bets will win. But as the award is only k units so he wants to put money less than K. Bob wants to bet as many horses as he can.

Example 1:
Input :
10
100
30 40 50 20 20 10 90 10 10 10
Output :
3

Example 2 :
Input :
10
100
10 90 80 20 90 60 40 60 70 75
Output :
1
'''

n = int(input())
k = int(input())
horses = []

for i in range(n):
    horses.append(int(input()))

sub = []
for i in range(n):
    for j in range(i,n):
        if sum(horses[i:j]) < k:
            sub.append(horses[i:j])
max = sorted(sub, key=len)
print(len(max[-1]))