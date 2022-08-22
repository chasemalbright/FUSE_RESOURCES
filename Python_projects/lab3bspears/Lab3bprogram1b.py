# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 3
# Date:        9 september 2020
#------------------------------------------------------------------------------------------------------------------------------------\
print('Calculating Reynolds number for a fluid with a given velocity, kinematic viscosity and characteristic linear dimension')
Velocity = float(input('What is the velocity in m/s?'))
LinearDimension = float(input('What is the linear dimension in meters?'))
viscosity = float(input('What is the kinematic viscosity in meters squared / second?'))
Reynoldsnumber = (Velocity * LinearDimension) / viscosity
print('\n')
print('The reynolds number is', Reynoldsnumber)
