#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab Assignment 10b
# Date:        27 October 2020

import csv
from statistics import mean

maxlist = []
minlist = []
precip = []
dates = []
numList = []
xmas = []
pressureList = []
print('-------------------------------------------------------')
with open('WeatherDataWindows(1).csv', 'r') as csvfile:
    # begin reading of file as comma separated
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)  # skip the label field
    # loop through lines and record values to list
    for row in readCSV:
        maxlist.append(float(row[1]))
        minlist.append(float(row[3]))
        precip.append(float(row[13]))
        pressureList.append(float(row[10]))

        # using delimeter to find temps on christmas eve
        dates.append(row[0].split('/'))

    # algo for finding the specific indexes of christmas eves
    for num in range(len(dates)):
        if dates[num][0] == '12' and dates[num][1] == '24':

            numList.append(num)
    # finding max temps on christmas eves
    for val in numList:
        xmas.append(float(maxlist[val]))






print('Maximum Temperature:          ', max(maxlist), 'F')
print('Minimum Temperature:          ', min(minlist), 'F')
print('Average daily precipitation:  ', round(mean(precip),3), 'in.')
print()
print('Random interesting Facts:')
print('The average high temperature on xmas eve is:  ', round(mean(xmas),3), 'F')
print('The average high pressure for these dates is: ', round(mean(pressureList),3))
print('-------------------------------------------------------')

