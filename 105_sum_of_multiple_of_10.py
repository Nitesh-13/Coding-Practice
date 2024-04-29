# TCS NQT 2024 April 29

'''

Sum of starting 10 multiples of given number

Input: 10
Output: 550
Explanation: 10*1+10*2+10*3+10*4 and so on upto 10*10

'''

print(sum([i*10 for i in range(1,int(input())+1)]))
