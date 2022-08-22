# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 4b
# Date:        15 September 2020
#------------------------------------------------------------------------------------------------
print('------------------------------------------------------------')
print('Let\'s calculate your BMI to see if you are underweight, healthy, or overweight')
print('\n')
weight = float(input('What is your weight in kilograms?'))
height = float(input('What is your height in centimeters?'))
heightM = height / 100
print('\n')
BMI = weight / (heightM **2)
print('Your body mass index is', BMI)
print('\n')
# now we have the if else conditions
status = 'weightstatus'
if BMI < 18.5:
    status = 'underweight'
elif 18.5 <= BMI < 25:
    status = 'a healthy weight'
elif 25 <= BMI < 30:
    status = 'overweight'
elif BMI >= 30:
    status = 'obese'

print('You are', status)

print('------------------------------------------------------------')






