# 

'''

Given a number x, determine whether the given number is Armstrong's number or not.
A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if
abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

EG
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

'''

def isArmstrong(n):
    if int(n)<=9 and int(n) >= 0:
        return True
    num = list(map(int, n))
    sum = 0
    for element in num:
        sum += pow(element, len(num))
    return (sum == int(n))

def nth_armstrong(n):
    count = 0
    num = 1
    while True:
        if isArmstrong(str(num)):
            count += 1
        if count == int(n):
            print(num)
            break
        num += 1

n = input()
print(isArmstrong(n))
print(nth_armstrong(n))


