# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 3
# Date:        9 september 2020
#------------------------------------------------------------------------------------------------------------------------------------\
print('Calculating the energy radiated per unit surface area (across all wavelengths) for a black body with a given temperature')
T = float(input('What is the temperature in kelvin?'))
Stefboltzconstant = (5.67 * (10 ** -8))
energyRadiated = Stefboltzconstant * (T ** 4)
print('\n')
print('The energy radiated is', energyRadiated, 'per unit')