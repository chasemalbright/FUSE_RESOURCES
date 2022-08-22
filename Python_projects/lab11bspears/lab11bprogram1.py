# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  11b
# Date:        11/4/20

#program to find the least profitable
def minprofitfinder(facility, facilityopcost, productvalue):
    '''This function takes the input of 3 lists,name,opcost,and net profit
        it calculates the least profitable facility'''
    # find len of lists
    length = len(facility)
    #profit of least valuble factory
    minfacilityprofit = productvalue[0]-facilityopcost[0]
    minfacility = facility[0]

    # go thru list to find least profitable
    for i in range(1,length):
        currentprofit = productvalue[i] - facilityopcost[i]

        if minfacilityprofit > currentprofit:
            minfacilityprofit = currentprofit
            minfacility = facility[i]

    # spit out the name and profit of least valuable facility
    return [minfacility, minfacilityprofit]

def testFunction():
    '''This is the test function that is required in the directions ** FEEL FREE TO CHANGE LIST TO FURTHER TEST **'''

    # define the lists
    # ******** THESE ARE TESTS LISTS THE DIRECTIONS WERENT SUPER CLEAR SO THIS WAS MY INTERPRETATION***********
    facility = ['Chevron', 'Dow Jones','Shell']
    facilityopcost = [5000, 2000, 1000]
    productvalue = [10000, 9000, 3000]

    # call function and store result
    leastprofitable = minprofitfinder(facility, facilityopcost, productvalue)

    print('The name and absolute profitability of the least profitable facility is:')
    print('Name:    ',leastprofitable[0])
    print('Profit:  ', leastprofitable[1])


# CALLING THE TEST FUNCTION
testFunction()
