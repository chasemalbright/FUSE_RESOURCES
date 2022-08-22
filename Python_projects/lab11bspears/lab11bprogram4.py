# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  11b
# Date:        11/4/20

# define the function
def findVelo(time, distance):
    '''This function calculates velocity from time and distance'''
    #store velos in a list
    velocities = []
    # looping through positions in lists
    for i in range(1, len(time)):
        velocities.append((distance[i]-distance[i-1])/(time[i]-time[i-1]))
    return velocities

# creating test function
def testFunction():
    '''this function is just a test '''
    # defining tests lists **THESE ARE TESTS LISTS**
    time = [2,4,6,8]
    distance = [10,20,40,80]

    print('The corresponding velocities are:')
    # calling function to test function
    print(findVelo(time,distance))

# calling test function
testFunction()