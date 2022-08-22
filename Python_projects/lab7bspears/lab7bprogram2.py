# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        chase albright
# Section:     480
# Assignment:  lab 7b
# Date:        10/6/2020
# -------------------------------------------------------------------------------------------------
import numpy as np
print('The function is f(x) = x^3')
print()



min = float(input('What is the minimum?: '))
max = float(input('What is the maximum?: '))
vals = np.arange(min, max, 0.5)


list = []
list.append(vals)
list.append(max)
list2 = []

#list.append()

print('The data points within these bounds are:')
for d in list[0]:
    print(d)
print(max)
for i in list:
    y = i**3
    list2.append(y)


print('The max value of y(x) is :', list2[-1])


