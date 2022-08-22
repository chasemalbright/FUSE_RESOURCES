#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab Assignment 12b
# Date:        11 November 2020

#import the packages
import numpy as np
import matplotlib.pyplot as plt

#begin to arrange the matrix into an array with numpy
M = np.array([[1.00583, -0.087156], [0.087156, 1.00583]])
p = np.array([[1,0]])

# this function will switches the row and index column indices of the matrix to produce another matrix
v = p.transpose()

# arrange variables for matrix
x = np.array([1])
y = np.array([0])

# loop to divide into 250 pieces
for num in range(0,250):
    #arrnaging vals
    constant = np.dot(M,v)
    # appending vals
    x = np.append(x, constant[0][0])
    y = np.append(y, constant[1][0])
    v = constant
# begin plotting
plt.plot(x, y, 'b')
plt.title('The matrix spiral')
plt.show()
