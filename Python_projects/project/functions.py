# this file is where our final versions of the functions were developed

# dynamic list of universal functions


# calling in the imports to be able to work with the modules
import random
import csv



def minigame():
    '''This function is the minigame that returns integer values for score and candies'''

    # --------------------------------------------- instructions
    # lots of words for the user
    print()
    print('--- Welcome to Random Number Guessing Game  ---')
    print()
    # instructions
    print('In this game you will guess a a number between 1 and 7. How quick you guess the magic number')
    print('will determine how many candies and pokemons you will be awarded.')
    print()
    print('if it only takes you 1 guess: you get two pokemons and 10 candies')
    print('if it takes 2 guesses: 7 candies and a pokemon')
    print('3 guesses is 5 candies and a pokemon')
    print('4 guesses 3 candies and a pokemon')
    print('5 and above guesses is 1 candy and a pokemon')
    print('')
    print()
    print('--- MAIN MENU ---')
    print()

    # user chooses game difficulty

    # ----------------------------------------------

    randRange = 7 # the random range for the game

    print('--------------------------------------------------------------------------')
    print()

    #############################

    # this is to choose a random int within these levels
    number = random.randint(1, randRange)
    # so now the random number is chosen

    # iterations to keep score
    i = 1
    # guesses start at 0
    guess = 0

    # list to track guesses
    guessList = []

    # while loop for guessing
    # enter a negative value to quit
    while guess != number:
        # input
        guess = int(input('What is your guess?:  '))
        # score counter
        i += 1
        # add guesses to list
        guessList.append(guess)

    print('--------------------------------------------------------------------------')
    print()
    # statements to record final info
    print()
    print('The random number was', number)
    print('it took you', i - 1, 'tries to guess this number')
    print('your score is', i - 1)
    print('here is the log of your guesses:')
    print(guessList)

        # if branches to determine candy count
    score = i - 1
    if score == 1:
        candies = 10
    if score == 2:
        candies = 7
    if score == 3:
        candies = 5
    if score == 4:
        candies = 3
    if score > 4:
        candies = 1
    # returns a list of the score and candies
    return [score, candies]




# functions

def playerFileWriteOPTION1(player):
    '''this file adds new pokemon to a players csv'''

    pFile = player + '.csv'  #sets a local variable in order to work with file
    with open(pFile,'a',newline='') as file: #newline prevents a blank line forming

        info = randomPokemonInfo() # uses the function that we determined earlier to get info
        writer = csv.writer(file) #using csv functions
        writer.writerow(info)

# this function is to display player info
def currentPlayerInfo(name):
    '''this function displays a current players stats and info'''
    player = name
    pFile = name + '.csv' # storing local variable
    with open(pFile, 'r') as file:
        csvReader = csv.reader(file) # using reader attribute and storing all the lines as a list
        rows = list(csvReader)
        currentCandies = rows[0]

        lines = len(rows) # using length for the range

        print('----------------------------------')
        print("player:", player)
        print('candies:', currentCandies)
        print('pokemons, CP, Level:')
        print(rows[1])

        if lines > 2: # handles cases for when there are more there are multiple lines
            for num in range(2, lines):
                print(rows[num])
        print('-----------------------------------')

# this function creates a random pokemon info for each player
def randomPokemonInfo():
    '''this function will assign a random pokemon'''
    with open('PokeList.csv', 'r') as PokeList:
        csvReader = csv.reader(PokeList)
        rows = list(csvReader)                      # this area is the same opening and reading process as before

        rand = random.randint(1,151)

        randompokelist = rows[rand]
        name = randompokelist[1]                    # calling on different portions of data in lists
        startCP = random.randint(int(randompokelist[2]),int(randompokelist[3]))

        startLevel = random.randint(1,40)   # randomly assigning a level
        return [name,startCP,startLevel]


# this function writes a to csv for each palyer
def playerFileWrite(player):
    '''this function will write new info to a player file'''
    pFile = player + '.csv'
    with open(pFile,'w',newline='') as file:
        candies = [3]                           # this function is similar in that it is used to write the info to a file
        info = randomPokemonInfo()
        writer = csv.writer(file)
        writer.writerow(candies)
        writer.writerow(info)