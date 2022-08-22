# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright Nathaniel Bush Joshua Campos Alan Albiter
# Section:     480
# Assignment:  Lab 5
# Date:        22 september 2020
#-----------------------------------------------------------------------------------------------------
# ----- imports ----- #
import numpy
import matplotlib.pyplot as plt
import math as math
# ----- Test Cases ----- #
# 2x^3 + 3x^2 - 11x - 6 bounds[-4,-2]
# 3x^3 + 2^2 - 3x - 2 bounds[1,2]
# x^3 + 4x^2 - 11x -30 bounds[-6, -4]
# x^3 - 2x^2 - x + 2 bounds[-2, 0]

# ----- Inputs ----- #
print('-----------------------------------------------------------------------------------------')
print('Test cases:')
print('2x^3 + 3x^2 - 11x - 6 bounds[-4,-2]')
print('x^3 + 3x^2 - 18x - 40 bounds[3,5]')
print('x^3 + 4x^2 - 11x -30 bounds[-6, -4]')
print('x^3 - 2x^2 - x + 2 bounds[-2, 0]')
print('-----------------------------------------------------------------------------------------')
print('Enter the values of the coefficients for one of the test cases.')
A = float(input("What is the a value?"))  # these are asking for the coefficients on the cubic equation
B = float(input("What is the b value?"))
C = float(input("What is the c value?"))
D = float(input("What is the d value?"))
print('\n')
print('Must input bounds that have a zero')
u_bound = float(input("What is the upper bound?"))  # these are the upper and lower bounds
l_bound = float(input("What is the lower bound?"))  # technically it doesn't matter the order
p = (u_bound + l_bound) / 2  # this finds the midpoint of the two bounds
fp = A * (p ** 3) + B * (p ** 2) + C * p + D  # this plugs the midpoint into the equation
fu = A * (u_bound ** 3) + B * (u_bound ** 2) + C * u_bound + D  # this plugs the upper bound into the equation
fl = A * (l_bound ** 3) + B * (l_bound ** 2) + C * l_bound + D  # this plugs the lower bounds into the equation
tolerance = 1 * (10 ** -6)  # this is how close we want it to get to the x - axis to find the zero

# ----- Conditionals ----- #
i = 0  # this is how many iterations we start off with
while math.fabs(u_bound - l_bound) > tolerance:  # this defines how close we are getting to the x-axis
    i += 1  # this adds an iteration every time the while loop repeats
    p = (u_bound + l_bound) / 2  # this is midpoint between the upper and lower bounds and the bounds will be changed
    fp = A * (p ** 3) + B * (p ** 2) + C * p + D  # this plugs the midpoint into the cubic equation
    if (fu > fl) and (fp > 0):  # this decides which bound should be replaced by p
        fu = fp  # this redefines fu to be fp
        u_bound = p  # this redefines the upper bound to be p
    elif (fu < fl) and (fp < 0):  # this decides which bound should be replaced
        fu = fp
        u_bound = p
    else:  # this redefines the the lower bound with p instead of the upper bound
        fl = fp
        l_bound = p

print('-----------------------------------------------------------------------------------------')
# ----- print ----- #
print("x =", round(p, 2))  # this prints the zero between the bounds
print("Interations = ", i)  # this prints the number of iterations it took to find the zero

# ----- activity2 ----- #
print('-----------------------------------------------------------------------------------------')
print('Now lets graph the function with a domain you set.')
lower_range_val = float(input('What is the lower range?:'))
upper_range_val = float(input('What is the upper range?:'))
xvals = numpy.arange(lower_range_val, upper_range_val, 0.01)
yvals = (A*(xvals**3)) + (B*(xvals**2)) + (C*xvals) + D
plt.plot(xvals, yvals)
plt.show()
print('-----------------------------------------------------------------------------------------')




