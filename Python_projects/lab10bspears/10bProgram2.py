#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab Assignment 10b
# Date:        27 October 2020

import csv

# taking the inputs for info
loan = float(input('Enter amount of the loan: '))
interest = float(input('Enter the annual interest rate: '))
monthly = float(input('Enter amount paid monthly: '))
fileID = input('Enter the file name without the extension: ')
fileID = fileID + '.csv'

monthlist = []
loanlist = []
ailist = []

num = loan
ai = 0
month = 0.0
aiadd = 0.000000

# while loop to stop calculating once loan is paid off or if it is increasing, stopping at 10x the initial amount
while 0 <= loan <= (num*10):
    monthlist.append(round(month,1))
    loanlist.append(round(loan,6))
    ailist.append(round(aiadd,6))
    month += 1

    ai = loan*((interest/100)/12)

    aiadd += ai

    loan = loan-(monthly-ai)

#print(monthlist)
#print(loanlist)
#print(ailist)

# creating list for first collumn
fields = ['Month','Principal Balance','Accrued Interest']
#creating list for the data values in a comma seperated list
rows =  []
for i in range(len(monthlist)):
    row = [monthlist[i],loanlist[i],ailist[i]]
    rows.append(row)

file = open(fileID, 'w')
# writing to the csv file with csv commands and using the linetermiantor to prevent skipping lines
csvwriter = csv.writer(file,lineterminator = '\n')
csvwriter.writerow(fields)
csvwriter.writerows(rows)
#close file out
file.close()