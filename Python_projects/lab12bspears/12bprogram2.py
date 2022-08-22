#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab Assignment 12b
# Date:        11 November 2020

# import modules
import numpy as np
import matplotlib.pyplot as plt

# sets up graphs for intersections
b = [(np.pi/4),(np.pi/4)+np.pi,(np.pi/4)+2*np.pi,(np.pi/4)+3*np.pi]
a = [np.sin(b[0]),np.sin(b[1]),np.sin(b[2]),np.sin(b[3])]

# arrange a number of values that are between 0 and 4pi
x = np.arange(0,4*np.pi,.05)


# functions
y1 = np.sin(x)
y2 = np.cos(x)

plt.title('plot of sine and cosine 0 to 4pi')
plt.plot(x,y1,'r--')
plt.plot(x,y2,'b')
plt.plot(b,a,'k*')
plt.show()