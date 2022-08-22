# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab1B
# Date:        26 August 2020

# a.)
print('Chase Albright, 529008060\n')

# b.)
print('I am from Richmond, Texas.\n')

# c.) formula: V = IR
I = 5
R = 20
print(I * R )

# d.) formula: k = (m * (v**2))/2
m = 100
v = 21
print(int((m * (v**2))/2))

# e.) formula: Re = (V * L)/v
V = 100
L = 2.5
v = 1.2
print((V * L)/v)

# f.) formula: energy radiated / unit surface area = SB * (T ** 4)
T = 2200
SB = (5.67 * (10 ** -8))
print(SB * (T ** 4))

# g.) formula: shear stress = (normal * tan(angleRadians)) + cohesion
import math
normal = 20
angle = 35
angleRadians = (angle * math.pi) / 180
cohesion = 2
print((normal * math.tan(angleRadians)) + cohesion)