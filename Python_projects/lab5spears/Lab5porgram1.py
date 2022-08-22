# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright Nathaniel Bush Joshua Campos Alan Albiter
# Section:     480
# Assignment:  Lab 5
# Date:        22 september 2020
#---------------------------------------------------------------------------------------------------
# take accelartion
accel = float(input('What is the acceleration in ft/s^2? '))

i_velocity = 0
velocity = 0
time = 0
distance = 0
banana = 0
banana_peel = 0
# while loop for finding velocity and distance
while (velocity <= 129.067) and (time <= 10) and (distance <= 500):
    velocity = accel * time + i_velocity
    distance = (1/2) * accel * (time**2) + i_velocity * time
    time = time + 0.1
    banana = banana + 1
print('v=',velocity)
print('d=',distance)
print('time=',time)

# print results
if velocity < 129.067:
    if distance > 500:
        print("Warning: Required velocity will not be achieved. Not enough road. Higher acceleration required.")
    else:
        print("Warning: Required velocity will not be achieved. Ran out of time. Higher acceleration required.")
else:
    print("In order to reach 88 mph with a acceleration of", accel,"ft/s^2, you will need a time of",time,"seconds.")

# bannanas used
while banana >= 120:
    banana_peel = banana_peel + 1
    banana = banana - 120
print("During this calculation, there will be", banana_peel,"banana peel(s) used.")