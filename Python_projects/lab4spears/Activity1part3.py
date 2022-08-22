# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright, Joshua Campos, Alan Albiter, and Nathaniel Bush
# Section:     480
# Assignment:  Lab 4 - Conditionals with Round-Off Error
# Date:        15 September 2020

# rocket's stage variables
first_stop = 0.3
second_go = 0.4
increment = 0.1

# ask for user input
current_increment = int(input("What is the current increment of the rocket, in kilometers?:"))
current_increment = current_increment * increment

# Tolerances and if statements
import math
tol = 1e-10
if math.fabs(current_increment - 0.3) < tol:
   print("Stop the first stage!")
elif current_increment == 0.4:
   print("Start the second stage!")
else:
   print("No action required at this point")

