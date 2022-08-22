#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 5
# Date:        22 september 2020
#-----------------------------------------------------------------------------------------------------
print('Enter as many measurements as you need, a negative value will terminate process')
measurements = 1
total = 0
min = 10**6
max = 0
i = 0

while measurements >= 0:
    measurements = float(input('What are the measurements?: '))

    if measurements >= 0: # finds the average
        i = i + 1
        total = total + measurements

        if measurements > max:
            max = measurements

        if measurements < min:
            min = measurements



print('-------------------------------------------------------------------------')
print('average =',total/i)
print('min =', min)
print('max =',max)