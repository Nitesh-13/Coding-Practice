# https://www.geeksforgeeks.org/program-check-given-year-leap-year/

'''

Program to check if a given year is leap year
A year is a leap year if the following conditions are satisfied: 

The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.

'''

year = int(input())
print((year%400 == 0) or (year%4 == 0 and year%100 != 0))