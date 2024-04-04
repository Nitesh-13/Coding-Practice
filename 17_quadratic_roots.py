# https://www.geeksforgeeks.org/program-to-find-the-roots-of-quadratic-equation/

'''

Program to find the Roots of a Quadratic Equation
Given a quadratic equation in the form ax2 + bx + c, (Only the values of a, b and c are provided) the task is to find the roots of the equation.

'''
import math

a = int(input())
b = int(input())
c = int(input())

def printRoots(a,b,c):
    b2 = math.pow(b,2)
    ac4 = 4*a*c
    b24ac = b2-ac4
    urb24ac = math.sqrt(abs(b24ac))
    
    if (b2 > ac4): # Real and Different
        r1 = (-b+urb24ac)/2*a
        r2 = (-b-urb24ac)/2*a
    elif (b2 == ac4): # Real and Equal
        r1 = r2 = -b/(2*a)
    else: # Complex and Not real
        r1 = f'{-b/(2*a)} + i {urb24ac/(2*a)}'
        r2 = f'{-b/(2*a)} - i {urb24ac/(2*a)}'
    
    print(r1,r2)

if a == 0:
    print("Invalid Equation")
else:
    printRoots(a,b,c)

'''
x = -b+-(b^2-4ac)/2a - for finding roots

Determinant (b^2-4ac):
    > 0 = real and different    | roots = {-b ± √(b2 - 4ac)}/2a
    < 0 = complex               | roots = {-b ± i√(b2 - 4ac)}/2a
    = 0 = real and equal        | roots = (-b/2a)
'''
