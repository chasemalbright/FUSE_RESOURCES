# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright, Nathanial Bush, Joshua campos, Alan Albiter
# Section:     480
# Assignment:  Lab 6
# Date:        9/29/20
#-----------------------------------------------------------------------------------------------------------------

import math as math



# variables #
pokemon = []  # empty
poke = input("What is the name?")  # name
cp = int(input("What is the CP?"))  # cp
level = int(input("What is the level?"))  # level
candy = int(input("What is the number of candies?"))  # candy

# list #
pokemon = [poke, cp, level, candy]  # inserts variables to list

# configuration #
print()
print(pokemon[0])  # prints name
print("Current CP:   ", pokemon[1])  # prints cp
print("Current level:", pokemon[2])  # prints level
print("Candies:      ", pokemon[3])  # prints candies
print("1 - Add Candy")  # choices to continue
print("2 - Use Candy to Level- Up")
print("3 - Exit to Main Menu")
print()

next = int(input("What would you like to do?:"))  # asks what to do

# add candies #
if next == 1:  # adds candies
   plus = int(input("How much candy would you like to add?"))  # asks how much to add
   pokemon[3] = pokemon[3] + plus  # adds the candies
   print("New candy:", pokemon[3])  # new candies

# level-up #
candy = 0  # creates candy variable
cont = 1  # continue varible might not be used
if next == 2:  # lelvel up function
   while cont == 1 or pokemon[2] <= 40 or pokemon[3] <= 0 or candy == 0:  # criteria to be able to level up
       print("Would you like to give a candy (0 or 1)?")
       candy = int(input("Candies:"))  # asks how much to add
       if candy == 0:  # ends program if adding no candy
           print("OK")
           break
       if pokemon[2] <= 30:  # if pokemon under 31 this is how much cp it goes up
           if pokemon[3] >= 1:
               pokemon[2] = pokemon[2] + candy
               pokemon[1] = pokemon[1] + pokemon[1] * .0094/ ((.095 * math.sqrt(pokemon[2])) ** 2)
               pokemon[3] -= 1
           else:
               print("Out of candy")
               break

       elif 31 <= pokemon[2] < 40:  # if pokemon over 30 this is how mch cp goes up
           if pokemon[3] >= 2:
               print("Must give another candy")
               candy = candy + int(input("Give another? (0 or 1)"))
               pokemon[2] = pokemon[2] + (candy * .5)
               pokemon[1] = pokemon[1] + pokemon[2] * .0045 / (( .095 * math.sqrt(pokemon[2])) ** 2)
               pokemon[3] -= 2
           else:
               print("Out of candy")
               break

       elif pokemon[2] >= 40:  # means pokemon cannot level up
           print("Pokemon has reached max level")
           break
       print()
       print(pokemon[0])
       print("Current CP:", pokemon[1])
       print("Current level:", pokemon[2])
       print("Candies:", pokemon[3])
       print()
       if pokemon[3] > 0:  # if enough candy asks if you want to continue
           print("Would you like to continue?")
       else:  # if out of candy it ends
           print("Out of candy")
           break
# Main Menu #
if next == 3:  # main menu function
   print("Exited to Main Menu")
