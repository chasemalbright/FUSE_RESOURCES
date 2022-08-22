# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 3
# Date:        9 september 2020
#------------------------------------------------------------------------------------------------------------------------------------\
#-----first have the user input the first observed point and the secont observed point
import math
print('first you must enter the x,y position and the time for the First observed point')
x1 = float(input('What is the x component of position in meters?'))
y1 = float(input('What is the y component of position in meters?'))
print('\n')
t1 = float(input('What is the time in seconds of the first observed point?'))
print('\n')
print('The first observed point has an (x,y) position of','(', x1,',',y1,')', 'at a time of', t1)
print('--------------------------------------------------------------------------------------------')
# have user enter data for second observed point
print('Now you must enter the x,y position and the time for the SECOND observed point')
x2 = float(input('What is the x component of position in meters?'))
y2 = float(input('What is the y component of position in meters?'))
print('\n')
t2 = float(input('What is the time in seconds of the second observed point?'))
print('\n')
print('The second observed point has an (x,y) position of','(', x2,',',y2,')', 'at a time of', t2)
print('--------------------------------------------------------------------------------------------')
# Finding the xvelocity and yvelocity components
print('Now we will calculate the x and y components of velo')
print('\n')
Xvelo = (x2 - x1) / (t2 - t1)
Yvelo = (y2 - y1) / (t2 - t1)
print('The velocity in x-direction and y-direction is is represented (x,y) as', '(', Xvelo,',',Yvelo,')')
print('--------------------------------------------------------------------------------------------')
#------------------------------------------------------------------------------------------------------------------------------
#find the overall velocity now
print('Now let\'s find the overall velocity by finding the hypotenuse between the x and y components of velocity')
print('\n')


import math


overallVelo = math.hypot(Xvelo,Yvelo)
print('The overall velocity of our bird red is', overallVelo)
print('--------------------------------------------------------------------------------------------')
#now we must find the kinetic energy of the bird

mass = 2.8

print('Now let\'s find the kinetic energy of the bird that has a mass of 2.8 kg')
print('\n')
ke = (.5 * mass * (overallVelo ** 2))
print('The kinetic energy of the bird is', ke)
print('--------------------------------------------------------------------------------------------')