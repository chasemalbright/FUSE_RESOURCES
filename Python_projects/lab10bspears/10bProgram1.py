#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab Assignment 10b
# Date:        27 October 2020

fVals = []
celsVals = []
with open('Celsius.dat', 'r') as fileC: # reading data from the celsius file
    lines = fileC.readlines() # reading each line on celsius file
    for i in lines: # for loop to read each line in file and store in list
        c = float(i.strip('\n'))  #strips the blank line
        celsVals.append(c)
    for x in celsVals: # converting in F
        f = (x*(9/5)) + 32
        fVals.append(f)

    with open('Fahrenheit.dat', 'w') as Ffile: # writing the F values into the fahrenheit file
        for temps in fVals:
            Ffile.write(str(temps)+'\n')
