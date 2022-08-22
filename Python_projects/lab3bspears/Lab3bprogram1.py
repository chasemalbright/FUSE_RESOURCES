# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 3
# Date:        9 september 2020
#------------------------------------------------------------------------------------------------------------------------------------\
print('Calculating kinetic energy with asn input of mass and velocity')
mass =  float(input('What is the mass in kilograms?'))
velo = float(input('What is the velocity in meters/second'))
KE = .5 * mass * (velo ** 2)
print('\n')
print('The kinetic energy is ', KE, 'Joules')