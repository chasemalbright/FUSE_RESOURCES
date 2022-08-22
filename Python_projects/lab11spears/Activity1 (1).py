#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Nathaniel Bush, Alan Albiter, Chase Albright, Joshua, Campos
# Section:     480
# Assignment:  Lab Assignment 11: Activity 1
# Date:        3 November 2020
# ----------------------------------------- IMPORTS STATEMENTS------------------------------------------
from math import *
import random
import matplotlib.pyplot as plt
# ---------------------------------------- FUNCTION DEFINITIONS-----------------------------------------
# (Then put any function definitions)

def get_basics():
#    """Takes user selections for active bird and planet. Returns (bird, planet). 'Bird' includes name,
#    color and size. 'Planet' includes name and gravity. """
    a = bird_picker() # Runs fn to provide bird menu
    b = planet_picker() # Runs fn to provide planet menu
    return a, b

def trajectory_y(x, g, vo, angle):
#    """Returns (y-value) of the trajectory for a given x-value, gravity, initial velocity, and angle."""
    angle = radians(angle)
    return (x*tan(angle))-(g*x**2)/(2*(vo**2)*cos(angle)**2)

def bird_picker():
    # ask user to pick bird from menu but doesn't determine its size yet(needed)
    print('The available birds are:')
    print('Red = red, small bird\nChuck = yellow, small bird\nBomb = black, large bird\nTerence = red, large bird')
    angry_bird = input('Which bird would you like to pick?: ')
    while True:
        if angry_bird == 'Red' or angry_bird == 'Chuck' or angry_bird == 'Bomb' or angry_bird == 'Terence':
            break
        else:
            print('That bird is unavailable. Try again')
            angry_bird = input('Which bird would you like to pick?: ')
    return angry_bird


def planet_picker():
    # ask user to pick a planet from the menu and returns planet's gravity to be used in calculating trajectory
    print('The available planets are: ')
    print('Earth = 9.807 m/s^2\nMars = 3.711 m/s^2 \nMoon = 1.625 m/s^2\nJupiter = 24.79 m/s^2')
    planet = input('What planet would you like to pick?')
    while True:
        if planet == 'Earth':
            gravity = 9.807
            break
        elif planet == 'Mars':
            gravity = 3.711
            break
        elif planet == 'Moon':
            gravity = 1.625
            break
        elif planet == 'Jupiter':
            gravity = 24.79
            break
        else:
            print("That planet is available. Try again.")
            planet = input('What planet would you like to pick?')
    return gravity

def get_guesses():
    # ask user for velocity and angle used in the trajectory function
    v = float(input('At what velocity would you like to launch your bird?(m/s^2): '))
    a = float(input('At what angle would you like to launch your bird?(deg): '))
    return v, a

def trajectory(g, v_guess, theta_guess):
    # determines the birds trajectory and returns bird's x and y value
    x_val = target[0]
    y_val = trajectory_y(x_val, g, v_guess, theta_guess)
    return x_val, y_val

def hit(x, y, pig):
    # determines whether bird hit or not
    if bird == 'Red' or bird == 'Chuck': # check to see if size of bird is small
        bird_size = 10
    elif bird == 'Bomb' or bird == 'Terence': # check to see if size of is bird big
        bird_size = 50
    if y == pig[1] : # checks to see if bird height matches targets
        if x == pig[0]: # checks to see if bird distance matches targets
            f_hit = True
        else:
            f_hit = False
    # checks to see if bird height matches targets including size. (pig[2] / 2) is pig's radius and (bird_size / 2) is bird's radius
    elif pig[1] >= (y + (bird_size / 2)) >= (pig[1] - (pig[2] / 2)):
        f_hit = True
    elif (pig[1] + (pig[2] / 2)) >= (y - (bird_size / 2)) >= pig[1]:
        f_hit = True
    else:
        f_hit = False
    return f_hit

def birds_plot(x, y, target, bird,ax=None):
    ax = None
    # for color of the line
    if bird == 'Red':
        color = 'red'
        size = 2 # thiner line
    elif bird == 'Chuck':
        color = 'yellow'
        size = 2
    elif bird == 'Bomb':
        color = 'black'
        size = 4 # thicker line
    elif bird == 'Terence':
        color = 'red'
        size = 4
    x = range(0, target[0])
    y = []
    for b in x:
        y_val = trajectory_y(b, g, v_guess, theta_guess)
        y.append(y_val)
    plt.plot(x, y, linewidth = size, color = color, linestyle = 'dashed') # bird trajectory
    plt.plot(target[0],target[1], 'go', linewidth = 4) # pig location
    plt.show()
# plot location of pig with additional instructions mentioned in assignment page
# line of trajectory must mach bird color and size and must be dotted line
# mark X where bird hit pig(if did hit)


# -------------------------------------------- MAIN PROGRAM --------------------------------------------
# (Then your Main Program)

# Sets up loop so user can repeat the game as many times as desired ('y' to continue, 'n' to quit)
pig_counter = 0
again = 'y'
while again == 'y':

    # Program will pick a random distance (x from 10-1000), height (y from 0-50) and size of a target
    target = (random.randint(10, 1000), random.randint(0, 50), random.randint(10, 50))

    # Takes initial guesses
    bird, g = get_basics()                          # Runs fn to get bird and planet information
    v_guess, theta_guess = get_guesses()            # Runs fn to get initial velocity and angle guesses

    # Loops guesses until bird hits target
    x, y = trajectory(g, v_guess, theta_guess)      # Create current x- and y- value lists
    while not hit(x, y, target):                    # Program cycles until throw hits the target
        birds_plot(x, y, target, bird)              # Plots trajectory & target of miss
        v_guess, theta_guess = get_guesses()        # Gets updated guesses from user
        x, y = trajectory(g, v_guess, theta_guess)  # Creates updated lists of x- and y-values

    # Handles winning case and asks if user would like to play again
    print('Yay!')
    pig_counter += 1
    birds_plot(x, y, target, bird, True)
    again = input('Would you like to play again? (y/n)')
    while again not in {'y', 'n'}:
        again = input('Please type either y or n only. Would you like to play again? (y/n)')

# Exiting when user decides to quit
print('\nThanks for playing! You popped %d pig(s) today!' % pig_counter)
