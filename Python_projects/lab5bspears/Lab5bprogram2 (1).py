#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 5
# Date:        22 september 2020
#-----------------------------------------------------------------------------------------------------

for x in range(2,101): #sets range as 2 to 100
    for y in range(2,x+1): # sets range as 2 to whatever x is in the range
        if x % y == 0: # if there is no remainder when x/y then print y divides x
            print(y, 'divides', x)