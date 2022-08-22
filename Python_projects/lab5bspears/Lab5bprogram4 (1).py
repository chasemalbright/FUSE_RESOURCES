#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 5
# Date:        22 september 2020
#-----------------------------------------------------------------------------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt

print('Trajectory for Red')
print('\n')
i = 0
v = float(input('What is the birds initial velocity?(m/s): '))
print('---------------------------------------------------------------')
x = 202.3
g = 9.8
# Q is measure of angle in radians!!! not degrees
Q = 0

# --------------simplifying equation------------------
y = (x * math.tan(Q)) - ((g * (x**2))/(2 * (v**2) * (math.cos(Q)**2)))
#------------------------------------------------------

# while y is not between .9 and 1.1, and increase .5 degree to Q till it is between these values

while y <= .9 or y >= 1.1:
    i +=1
    Q = Q + (0.0174533/2)
    y = (x * math.tan(Q)) - ((g * (x**2))/(2 * (v**2) * (math.cos(Q)**2)))
    if y > .9 and y < 1.1 and i < 500:

        print('---------------------------------------------------------------')
        print('iterations=', i)
        print('Height=', y, 'm')
        print('The solution in degrees is:')
        print('Degrees=',Q*180/math.pi)
        print('Target height has been reached')
        print('---------------------------------------------------------------')
        print('To continue to the mars calculations, you must click into the graph then close it.')
        fig = plt.figure()
        a1 = fig.add_axes([0, 0, 1, 1])
        xvals = np.arange(0, 2, .01)
        a1.plot(xvals, (x * np.tan(xvals)) - ((g * (x ** 2)) / (2 * (v ** 2) * (np.cos(xvals) ** 2))), 'r')
        a1.set_title('Red')
        a1.set_ylim(0, 5)
        a1.set_xlim(0, 2)
        plt.show()
        break # break once solution ius found so other code will run after this loop


    if i > 500: # after 500 iterations there will not be a solution
        print('For this velocity, there is no solution')
        print('---------------------------------------------------------------')
        break

#------------------------------------------------------------------------------------------

print('Now if we were on Mars...')
print('---------------------------------------------------------------')
#accelation due to gravity on mars is 3.7
print('Trajectory for Red on Mars:')
print('\n')
i = 0

x = 202.3
g = 3.7
# Q is measure of angle in radians!!! not degrees
Q = 0

# Create x-values for plot

#---------------------------------------------------------------------------------------

ymars = (x * math.tan(Q)) - ((g * (x**2))/(2 * (v**2) * (math.cos(Q)**2)))
#------------------------------------------------------

# while y is not between .9 and 1.1, and increase 1 degree to Q till it is between these values

while ymars <= .9 or ymars >= 1.1: # while y is not between .9 and 1.1
    i +=1
    Q = Q + (0.0174533/2) # increment 1 radian at a time
    ymars = (x * math.tan(Q)) - ((g * (x**2))/(2 * (v**2) * (math.cos(Q)**2)))

    if ymars >= .9 and ymars <= 1.1 and i < 500:
        print('---------------------------------------------------------------')
        print('iterations=', i)
        print('Height=', ymars, 'm')
        print('The solution in degrees is:')
        print('Degrees=', Q*180/math.pi)
        print('Target height has been reached')
        print('---------------------------------------------------------------')
        fig = plt.figure()
        a1 = fig.add_axes([0, 0, 1, 1])
        xvals = np.arange(0, 2, .01)
        a1.plot(xvals, (x * np.tan(xvals)) - ((g * (x ** 2)) / (2 * (v ** 2) * (np.cos(xvals) ** 2))), 'b')
        a1.set_title('Red')
        a1.set_ylim(0, 5)
        a1.set_xlim(0, 2)
        plt.show()

    if i > 500: # after so many iterations there will never be a solution
        print('For this velocity on mars, there is no solution')
        print('---------------------------------------------------------------')
        break


