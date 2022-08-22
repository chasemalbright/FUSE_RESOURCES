# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  11b
# Date:        11/4/20

# define the function
def perfectNumber(num):
    '''This function takes in a number and calculates whether or not it is a perfect number'''
    sum = 0
    # for loop tp check divisibitly
    for i in range(1,num):
        # finding the divisors
        if num % i == 0:
            sum += i
    return sum == num
print('Test input with the number 6:')
print(perfectNumber(6))
print('6 is a perfect number')


# to test your self remove the # and put your number where the indicator is
#print(perfectNumber(INPUT NUMBER HERE))