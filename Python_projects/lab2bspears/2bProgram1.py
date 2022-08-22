# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab2B
# Date:        1 September 2020


# Program 1
# a.)
Name = 'Chase Albright'
UIN = '529008060\n'
print(Name, UIN)

# b.)
InterestingFact = "I am from Richmond, Texas.\n"
print(InterestingFact)

# c.) formula: Voltage = Current * Resistance
Current = 5
Resistance = 20
Voltage = Current * Resistance
print(Voltage)

# d.) formula: kineticEnergy = (mass * (velocity **2))/2
mass = 100
velocity = 21
kineticEnergy = (mass * (velocity **2))/2
print(kineticEnergy)

# e.) formula: Reynoldsnumber = (Velocity * LinearDimension) / viscosity
Velocity = 100
LinearDimension = 2.5
viscosity = 1.2
Reynoldsnumber = (Velocity * LinearDimension) / viscosity
print(Reynoldsnumber)

# f.) formula: energyRadiated = Stefboltzconstant * (T ** 4)
Temperature = 2200
Stefboltzconstant = (5.67 * (10 ** -8))
energyRadiated = Stefboltzconstant * (Temperature ** 4)
print(energyRadiated)

# g.) formula: shearStress = (normalStress * tan(angleRadians)) + cohesion
# ----------TRIG FUNCTIONS IN PYTHON ARE IN RADIANS!!!!!----------
import math
normalStress = 20
angle = 35
angleRadians = (angle * math.pi) / 180
cohesion = 2
shearStress = (normalStress * math.tan(angleRadians)) + cohesion
print(shearStress)
print('----------------------------------------------------------------------')














