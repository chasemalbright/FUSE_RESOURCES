# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 4b
# Date:        15 September 2020
#------------------------------------------------------------------------------------------------
# ny sources for the RE are https://www.softschools.com/formulas/physics/reynolds_number_formula/78/
#*********************************************************************************************************************
#******I hope points arent taken off, but the most reliable online resources included density in the formula**********
#*********************************************************************************************************************
print('----------------------------------------------------------------------')
print('Let\'s calculate the reynolds number!')
print('\n')

velocity = float(input('What is the fluid velocity in m/s?'))
linearDimension = float(input('What is the linear dimension in m?'))
viscosity = float(input('What is the viscosity in kg/(m*s) or Pa*s ?'))
density = float(input('What is the density in kg/m^3?'))
print('\n')

re = (velocity * linearDimension * density) / viscosity
print('The reynolds number for these parameters is', re)
print('\n')

flowtype = 'flowtype'

if re <= 2300:
    flowtype = 'laminar'
elif 2300 < re <= 4000:
    flowtype = 'transient'
elif re > 4000:
    flowtype = 'turbulent'
print('The flow type is', flowtype)
print('----------------------------------------------------------------------')