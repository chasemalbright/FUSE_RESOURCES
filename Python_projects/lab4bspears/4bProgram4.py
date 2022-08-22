# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 4b
# Date:        15 September 2020
#------------------------------------------------------------------------------------------------
from math import *



print('We will be finding the roots of a quadratic equation.')
print('A quadratic equation is in the form of Ax^2 + Bx + C = 0')
print('\n')
print('Now enter values for A B C')
print('\n')


a = float(input('What is the value of A?  '))
b = float(input('What is the value of B?  '))
c = float(input('What is the value of C?  '))
print('\n')

r = (b**2)-(4*a*c)

if a == 0 and b != 0 and c != 0:
    xroot1 = -c / b
    print('This is a linear equation, the one root is x =',xroot1)

elif a == 0 and b == 0 and c == 0:
    print('You have entered 0 for each variable, evaluating to 0 = 0')

elif a == 0 and b == 0 and c != 0:
    print('You have entered a non zero value for c, evaluating to',c,'= 0 which is an error')

else:
    if r > 0:
        xroot1 = ((-b) + sqrt(r))/(2*a)
        xroot2 = ((-b) - sqrt(r))/(2*a)
        print('There are two real roots:', xroot1,xroot2)


    elif r == 0:
        xroot1 = (-b)/(2*a)
        print('There is one root:',xroot1)


    elif r < 0:
        print('There are imaginary roots when r < 0')
        rsqrABS = str(sqrt(abs(r)))
        print('(', -b, '+', rsqrABS + 'i', ')', '/', '(', 2 * a, ')')
        print('(', -b, '-', rsqrABS + 'i', ')', '/', '(', 2 * a, ')')

print('--------------------------------------------------------------------------------------------')
