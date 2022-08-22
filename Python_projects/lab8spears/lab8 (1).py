# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright Nathaniel Bush Joshua Campos Alan Albiter
# Section:     480R
# Assignment:  lab 8
# Date:        10/8/2020
import math
import matplotlib.pyplot as plt

t = 0

tvals = []
f1vals = []
f2vals = []

f1 = (t**2) * (math.exp(-t**2))

f2 = (t**4) * (math.exp(-t**2))

while t >= 0 and t <= 3:
    f1 = (t ** 2) * (math.exp(-t ** 2))
    t += 0.06
    tvals.append(t)
    f1vals.append(f1)

t = 0

while t >= 0 and t <= 3:
    f2 = (t ** 4) * (math.exp(-t ** 2))
    t += 0.06
    f2vals.append(f2)


x = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
y = [0, 0.23, 0.4, 0.18, 0.07, 0.01]

plt.subplot(2,1,1)
plt.scatter(x,y,color='k', label="Data")
plt.plot(tvals,f1vals,'-r',label='t^2*exp(-t^2)')
plt.plot(tvals,f2vals, '-b',label='t^4*exp(-t^2)')

plt.ylim(0, 1)
plt.xlabel("Time")
plt.ylabel("Y ")
plt.title('Data and two curves vs. time')

plt.legend()
print('\n')

plt.subplot(2,1,2)

label_x = 1.2
label_y = .133
arrow_x = 1.4
arrow_y = .29

arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

plt.annotate(
    "It is closest here", xy=(arrow_x, arrow_y),
    xytext=(label_x, label_y),
    arrowprops=arrow_properties)



plt.plot(x,y,'^y',label='Data')
plt.plot(x,y,'-y')
plt.plot(tvals,f1vals,'-b',label='t^2*exp(-t^2)')

plt.ylim(0, 0.5)
plt.xlim(1,2)
plt.xlabel("Time")
plt.ylabel("Y ")
plt.title('Data interpolation and Curve 1')
plt.legend()


plt.legend()
plt.tight_layout()
plt.show()
