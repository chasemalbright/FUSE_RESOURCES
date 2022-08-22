#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 6b
# Date:        9/29/20
#-----------------------------------------------------------------------------------------------------------------

num = int(input('Enter a number here for the conjecture: '))
iteration = []
iteration.append(0)
i = 0
collatz = []
collatz.append(num)
while num != 1:
    i += 1
    iteration.append(i)
    if num%2 == 0:
        num = num//2
    else:
        num = num*3 +1
    collatz.append(num)

print('collatz sequence:', collatz)
print('steps taken/counting numbers:', iteration)

import matplotlib.pyplot as plt

plt.plot(iteration, collatz)
plt.show()