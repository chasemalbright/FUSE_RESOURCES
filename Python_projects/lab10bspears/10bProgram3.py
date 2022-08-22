#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab Assignment 10b
# Date:        27 October 2020

import csv

# program to open and read the csv file
file = input('Enter the name of the loan csv file you wish to visualize: ')

monthList = []
balanceList = []

#open the file
with open(file,'r') as csvfile:
    #read each line seperated by a comma
    readCSV = csv.reader(csvfile, delimiter=',')
    #loop to run through each and while loop to limit to 30 values
    next(readCSV) # skip the label field
    for row in readCSV:
        monthList.append(row[0])
        balanceList.append(row[1])
#print(monthList)
#print(balanceList)

# convert list vals into floats
monthNum = []
for numM in monthList:
    x = float(numM)
    monthNum.append(x)

balNum = []
for numB in balanceList:
    y = float(numB)
    balNum.append(y)

#print(monthNum)
#print(balNum)

#limits length to 30 points if longer than 30
if len(monthNum) >= 30:
    del monthNum[29:]
    del balNum[29:]


# here we begin the graphing
import matplotlib.pyplot as plt

plt.scatter(monthNum,balNum,color='k',label='Balance')
plt.plot(monthNum,balNum,'--k')
plt.xlabel('Months')
plt.ylabel('Principal Balance')
plt.title('Balance vs. Time in Months')
plt.legend()
plt.show()
