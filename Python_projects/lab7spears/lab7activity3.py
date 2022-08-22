#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Nathaniel Bush
# Section:     480
# Assignment:  Lab Assignment 2
# Date:        6 October 2020

# variables #
summation = 0
x = float(input("What is the x-value: "))
y = 1
n = 0
TOL = .000001
while abs(y) > TOL:
    y = x ** n
    n += 1
    summation += y
    print("y          = ", y)
    print("iterations = ", n)
    print("summation  = ", summation)
    print()