# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  11b
# Date:        11/4/20

from statistics import mean

# define function to find min max mean
def again(list):
    '''this function takes in a list and spits out mean, min, max'''
    # find min
    minVal = min(list)
    # find max
    maxVal = max(list)
    # find mean
    meanVal = mean(list)

    # return the desired statistics
    return [minVal, maxVal, meanVal]


def testFunction():
    '''This is  atest function with a preset list to test the again function'''

    # defining a test list ** THE GRADER CAN CHANGE VALUES **
    list = [1, 22, 23, 12, 45, 3, 99]

    # calling the function to test it and storing the results as a variable
    results = again(list)

    # print the results
    print('Min:   ', results[0])
    print('Max:   ', results[1])
    print('Mean:  ', results[2])

# calling the test function
testFunction()