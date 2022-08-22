# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright, Nathanial Bush, Joshua campos, Alan Albiter
# Section:     480
# Assignment:  Lab 6
# Date:        9/29/20
#-----------------------------------------------------------------------------------------------------------------


import math
import matplotlib.pyplot as plt
import numpy as np


# ask for user input of fuel cost and distance traveled
fuel_cost = float(input("What is the current fuel cost in $/gal?: "))
distance = int(input("What distance do you plan to travel in miles?: "))

# list where info is stored
MPH = []
MPG = []
cost = []
time = []

# loop to find info of every 5 mph increments
mph = 25
while mph < 81:
   MPH.append(mph)
   mpg = -5.9852 + 1.6052 * mph - 0.0141 * math.pow(mph,2)
   MPG.append(mpg)
   t = distance / mph
   time.append(t)
   t_gal = distance / mpg
   price = t_gal * fuel_cost
   cost.append(price)
   mph = mph + 5

print()
print('---------------------------------------------------------------------------------------------------------------')

option = int(input('Please enter a positive integer to continue to options. '))
print()

while option >= 0:
    option = int(input('What option do you choose?(choose 1-4 or 6 to quit) '))

    if option == 1:
        print('---------------------------------------------------------------------------------------------------------------')
        print("MPH          MPG        Cost        Time")
        print(MPH[0], "        ", '{:.3f}'.format(MPG[0]), "    ", '{:.3f}'.format(cost[0]), "     ",
              '{:.3f}'.format(time[0]))
        print(MPH[1], "        ", '{:.3f}'.format(MPG[1]), "    ", '{:.3f}'.format(cost[1]), "     ",
              '{:.3f}'.format(time[1]))
        print(MPH[2], "        ", '{:.3f}'.format(MPG[2]), "    ", '{:.3f}'.format(cost[2]), "     ",
              '{:.3f}'.format(time[2]))
        print(MPH[3], "        ", '{:.3f}'.format(MPG[3]), "    ", '{:.3f}'.format(cost[3]), "     ",
              '{:.3f}'.format(time[3]))
        print(MPH[4], "        ", '{:.3f}'.format(MPG[4]), "    ", '{:.3f}'.format(cost[4]), "     ",
              '{:.3f}'.format(time[4]))
        print(MPH[5], "        ", '{:.3f}'.format(MPG[5]), "    ", '{:.3f}'.format(cost[5]), "     ",
              '{:.3f}'.format(time[5]))
        print(MPH[6], "        ", '{:.3f}'.format(MPG[6]), "    ", '{:.3f}'.format(cost[6]), "     ",
              '{:.3f}'.format(time[6]))
        print(MPH[7], "        ", '{:.3f}'.format(MPG[7]), "    ", '{:.3f}'.format(cost[7]), "     ",
              '{:.3f}'.format(time[7]))
        print(MPH[8], "        ", '{:.3f}'.format(MPG[8]), "    ", '{:.3f}'.format(cost[8]), "     ",
              '{:.3f}'.format(time[8]))
        print(MPH[9], "        ", '{:.3f}'.format(MPG[9]), "    ", '{:.3f}'.format(cost[9]), "     ",
              '{:.3f}'.format(time[9]))
        print(MPH[10], "        ", '{:.3f}'.format(MPG[10]), "    ", '{:.3f}'.format(cost[10]), "     ",
              '{:.3f}'.format(time[10]))
        print(MPH[11], "        ", '{:.3f}'.format(MPG[11]), "    ", '{:.3f}'.format(cost[11]), "     ",
              '{:.3f}'.format(time[11]))
        print('---------------------------------------------------------------------------------------------------------------')
        print()

    if option == 2:
        x = np.arange(25.0, 80.0, 5.0)  # MPH
        mpg = -5.9852 + 1.6052 * x - 0.0141 * x ** 2
        t_gal = distance / mpg
        price = t_gal * fuel_cost
        y = price
        plt.scatter(x, y)
        plt.xlabel("Speed (MPH)")
        plt.ylabel("Cost $")
        plt.show()

    if option ==3:
        costFloat = []
        for num in cost:
            costFloat.append(float(num))

        timeFloat = []
        for tim in time:
            timeFloat.append(float(tim))

        plt.scatter(costFloat, timeFloat)
        plt.xlabel("Cost")
        plt.ylabel("Time")
        plt.show()

    if option == 4:
        print('---------------------------------------------------------------------------------------------------------------')
        SPEED = float(input('At which speed do you wish to calulate time and cost? '))
        mpg = -5.9852 + 1.6052 * SPEED - 0.0141 * math.pow(SPEED, 2)
        t_gal = distance / mpg
        price = t_gal * fuel_cost
        t = distance / mph
        print('At this speed the cost is', round(price, 3))
        print('At this speed the time is', round(t, 3))
        print('---------------------------------------------------------------------------------------------------------------')

    if option == 6:
        print('Have a nice day!')
        break
    if option != 1 and option != 2 and option != 3 and option != 4 and option != 6:
        print('Please enter numbers 1-4 or the number 6 to quit.')