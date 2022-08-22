# this is where the all the increments were tested and developed, we deleted the code once it worked and tested
# then moved that code into the deployment file

#the try except statements were required so we left the last two tests for the grading team to inspect


import csv
import time
import math

POKETESTLIST = ['Snorlax','230','30']

try:
    score = POKETESTLIST[2] * POKETESTLIST[1]
except:                                         # we used this type of error trial to find improprieties in
    print('could not multiply the values')      # the data types of info stored in lists
# the solution we discovered was that we had to take the int() of each numerical index


playercandies = [['3']]

try:
    scoreMUlTIPLE = 3 * playercandies[0]

except:
    print(' could not multiply a list data type')
# the solution that we found and discovered was that it was a nested list so we the working product looked like this
# scoreMULTIPLE = 3 * int(playercandies[0][0]) and this statement ended up working





