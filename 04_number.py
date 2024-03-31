# https://www.geeksforgeeks.org/program-check-number-positive-negative-odd-even-zero/

'''

Program to check if a number is Positive, Negative, Odd, Even, Zero
Given a number n, the task is to check whether the given number is positive, negative, odd, even, or zero.

'''

n = int(input())
print("Positive" if n>0 else ("Negative" if n < 0 else "Zero"))
print("Even" if n%2 == 0 else "Odd")