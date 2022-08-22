#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Nathaniel Bush, Alan Albiter, Chase Albright, Joshua, Campos
# Section:     480
# Assignment:  Lab Assignment 12
# Date:        20 November 2020



import csv
import functions        # this area is where i imported our necessary modules
import math
import time
import random



##################################################################################################################
##################################################################################################################

#lists
playerList = []     # players will be stored in lists for easy access when creating files

print('---------- Welcome to the Pokemon Game ----------')
print()                                                                 # these are just commentary for the game
print('Now, let\'s decide how many players will play today...')
print()

# here we select the amount of players playing the game which saves each name to a list
players = ''

# while loop to add players
while players != 'DONE':        # loop for users to enter names of players
    players = input('Please enter a name of player - enter DONE to finish entering players  ')
    if players != 'DONE':
        playerList.append(players)


# this loop opens a csv for each player we chose to open a file for each player that is our chosen data structure
for i in playerList:            # this for loop opens a csv for each player
    open(i+'.csv', 'w')

# tells how many players
print()
print('There are',len(playerList),'players.') # displays number of palyers


# this assigns a random pokemon to each player and adds it to a csv file for each player

for player in playerList:
    functions.playerFileWrite(player)


# displays player info for each player starting
for name in playerList:
    functions.currentPlayerInfo(name)


                ################################# GAME STARTS ################################
print()
print()
print('----- Who will be the two starting players? -----')   ## this part establishes who the two main players are
print()
print('make sure to enter names correctly and as entered before')
player1 = input('who is player 1?:  ')
print()
player2 = input('who is player 2?:  ')


#______________----------------------------------------------------------------------_________________________
print()


            # there are similar menus that are displayed for each of the two players in order to organize their input



# for player 1    # there two menus for each of the two starting players that look like this
print('player 1:',player1,'- what do you wish to do?')
print('1 -> View current pokemon and info AND not catch a pokemon?')
print('2 -> Catch pokemon?')
print()
choice = int(input('Enter number:  '))
if choice !=1 and choice != 2:
    print('please enter a valid option')
    choice = int(input('Enter number:  '))          # user makes decisions for choices
# acting on the player 1 input
if choice == 1:
    functions.currentPlayerInfo(player1)

print()
with open(player1+ '.csv','r') as p1file:           # opens user csv to display info
    csvReader = csv.reader(p1file)
    rows = list(csvReader)
    player1candies = int(rows[0][0])

#play game option
if choice == 2:                                                 # in this feild the user selects to play a game
    print('You have chosen to catch a pokemon...')
    print('You have two choices now for getting a new pokemon')
    print('choice 1 -> be assigned a random pokemon without candies')
    print('choice 2 -> play a minigame and your score determines how many candies you get')
    choice2 = int(input('Enter number:  '))
    print('-----------------------------------------------------------------------------------')
    if choice2 != 1 and choice2 != 2:
        print('please enter a valid option')
        choice2 = int(input('Enter number:  '))
    if choice2 == 1:                                #adding the winnings
        player = player1
        functions.playerFileWriteOPTION1(player)
        print()
        print('Your random pokemon has been added')
        print('-----------------------------------------------------------------------------------')
    if choice2 == 2:
        print('------------------------------------------------------------------------------------')
        listNewInfo = functions.minigame()
                                                        # this area writes the pokemons and stores candies
        if listNewInfo[0] == 1:
            functions.playerFileWriteOPTION1(player1)
            functions.playerFileWriteOPTION1(player1)
        if listNewInfo[0] > 1:
            functions.playerFileWriteOPTION1(player1)

        player1candies = player1candies + listNewInfo[1]
print()
print(player1,'enter 1 to see your pokemons and stats or 2 to continue')
choice3 = int(input('Enter number:  '))


if choice3 !=1 and choice3 != 2:
    print('please enter a valid option')
    choice3 = int(input('Enter number:  '))

if choice3 == 1:
    name = player1                                      # continues the selection and writing process
    functions.currentPlayerInfo(name)
if choice3 == 2:
    print()
    print('continuing...')
    print('---------------------------------------------------------------------------------')

print()
#########################################################################################################################

# now the same process for player 2


print('player 2:',player2,'- what do you wish to do?')
print('1 -> View current pokemon and info AND not catch a new pokemon?')
print('2 -> Catch pokemon?')
print()
choice4 = int(input('Enter number:  '))
if choice4 != 1 and choice4 != 2:
    print('please enter a valid option')
    choice4 = int(input('Enter number:  '))
# acting on the player 1 input
if choice4 == 1:                                                        # this code is very similar to the above code
    functions.currentPlayerInfo(player1)                    # it would be redundant to comment on this portion
                                                    # only the variable names are different
print()
with open(player2+ '.csv','r') as p2file:
    csvReader = csv.reader(p2file)
    rows = list(csvReader)
    player2candies = int(rows[0][0])

#play game option
if choice4 == 2:
    print('You have chosen to catch a pokemon...')
    print('You have two choices now for getting a new pokemon')
    print('choice 1 -> be assigned a random pokemon without candies')
    print('choice 2 -> play a minigame and your score determines how many candies you get')
    choice5 = int(input('Enter number:  '))
    print('-----------------------------------------------------------------------------------')
    if choice5 != 1 and choice5 != 2:
        print('please enter a valid option')
        choice5 = int(input('Enter number:  '))
    if choice5 == 1:
        player = player2
        functions.playerFileWriteOPTION1(player)
        print()
        print('Your random pokemon has been added')
        print('-----------------------------------------------------------------------------------')
    if choice5 == 2:
        print('------------------------------------------------------------------------------------')
        listNewInfo2 = functions.minigame()

        if listNewInfo2[0] == 1:
            functions.playerFileWriteOPTION1(player2)
            functions.playerFileWriteOPTION1(player2)               #saving the results as before
        if listNewInfo2[0] > 1:
            functions.playerFileWriteOPTION1(player2)

        player2candies = player2candies + listNewInfo2[1]
print()
print(player1,'enter 1 to see your pokemons and stats or 2 to continue')
choice6 = int(input('Enter number:  '))


if choice6 !=1 and choice6 != 2:
    print('please enter a valid option')
    choice6 = int(input('Enter number:  '))

if choice6 == 1:
    name = player2
    functions.currentPlayerInfo(name)
if choice6 == 2:
    print()
    print('continuing...')
    print('---------------------------------------------------------------------------------')

print()
print('--------------------------------------------------------------------------------------')





#-------------------------------------------------------------------------------------------------------------------
# player 1 levling
print('player 1,',player1,', has',player1candies,'candies')
print()
print('players now have two options...')
print('1 -> continue without leveling up.')
print('2 -> select a pokemon to level up before battling')
print()                                                         # here players are able to level their pokemon
levelchoice1 = int(input('Enter 1 or 2 here:  '))

if levelchoice1 != 1 and levelchoice1 != 2:
    print('invalid choice ')
    levelchoice1 = int(input('Enter 1 or 2 here:  '))


if levelchoice1 == 1:
    print('continuing...')

if levelchoice1 == 2:
    print('You have chosen to level up a pokemon from your collection with candies')
    print()

    # opening the user file and displying the users pokemons

    p1pokelist = []

    print('here is your pokemon collection...')
    with open(player1+'.csv','r') as pfile1:
        csvReader = csv.reader(pfile1)
        rows = list(csvReader)

        lines = len(rows) # this area displays and appends the users selection of a pokemon to a list for later battling
        print('Name  ','CP  ','Level')
        print('1 :',rows[1])
        p1pokelist.append(rows[1])

        if lines > 2:
            for num in range(2, lines):
                print(num,':',rows[num])
                p1pokelist.append(rows[num])
    print()
    print(
        'Now you can select a pokemon to level up LEVELING UP WILL USE ALL CANDIES, just enter the number that is next to your desired pokemon')

    pokeselector = int(input('Enter the number here: '))

    print('You have selected to level up this pokemon:')
    print(p1pokelist[pokeselector - 1])
                                                                        # displays rules for battling and the calculations
    print('you currently have', player1candies, 'candies')
    print()
    print('----- Leveling Rules -----')
    print('Level 40 is the maximum')
    print(
        'One (1) candy is required to level the Pokemon by 1 level from levels 1–30, two (2) candies arerequired to level-up to levels 31–40')
    print('CP will also be updated when leveling')
    print()
    print()

    currLevel = int(p1pokelist[pokeselector - 1][2])
    print('candy count =', player1candies)                  # pulls data from necessary lists
    if currLevel == 40:
        print('Your pokemon is already max level')

    if currLevel >= 30:
        if ((player1candies // 2) + currLevel) <= 40:           # the leveling requires a logical understanding
            currLevel = currLevel + (player1candies // 2)       # of differntiating the above and below of 31
        if ((player1candies // 2) + currLevel) >= 40:
            currLevel = 40

    if currLevel < 30:
        key = 30 - currLevel
        if player1candies <= key:
            currLevel = currLevel + player1candies

        if player1candies > key:
            currLevel = currLevel + key                 # this is where more logic is required to make it work
            player1candies = player1candies - key
            currLevel = currLevel + (player1candies // 2)
    print('----------------------------------------------------------------------------')
    print('The new pokemon level is ', currLevel)

    print('Now the pokemons new CP will be calculated')
    print()
    time.sleep(3)

    p1battleinfolist = []
    p1battleinfolist.append(p1pokelist[pokeselector - 1][0])

    ogCP = int(p1pokelist[pokeselector - 1][1])
    if currLevel <= 30:
        newCP = ogCP + (2 * math.sqrt(currLevel))       # this area is where the new cp is calculated
    if currLevel > 30:
        newCP = ogCP + math.sqrt(currLevel)
    p1battleinfolist.append(round(newCP, 1))
    p1battleinfolist.append(currLevel)
    # -----------------------------------------------------------------------------------------------

###############################################################################################################

# player 2 levling
print('player 2,',player2,', has',player2candies,'candies')
print()
print('players now have two options...')
print('1 -> continue without leveling up.')
print('2 -> select a pokemon to level up before battling')          # SAME PROCESS AS ABOVE REFERENCE PAST COMMENTS
print()
levelchoice2 = int(input('Enter 1 or 2 here:  '))

if levelchoice2 != 1 and levelchoice2 != 2:
    print('invalid choice ')
    levelchoice2 = int(input('Enter 1 or 2 here:  '))


if levelchoice2 == 1:
    print('continuing...')

if levelchoice2 == 2:
    print('You have chosen to level up a pokemon from your collection with candies')
    print()

    # opening the user file and displaying the users pokemons

    p2pokelist = []

    print('here is your pokemon collection...')
    with open(player2+'.csv','r') as pfile2:
        csvReader = csv.reader(pfile2)                                  # SAME PROCESS AS ABOVE REFERENCE PAST COMMENTS
        rows = list(csvReader)

        lines = len(rows)
        print('Name  ','CP  ','Level')
        print('1 :',rows[1])
        p2pokelist.append(rows[1])

        if lines > 2:
            for num in range(2, lines):
                print(num,':',rows[num])
                p2pokelist.append(rows[num])
    print()
    print('Now you can select a pokemon to level up LEVELING UP WILL USE ALL CANDIES, just enter the number that is next to your desired pokemon')

    pokeselector = int(input('Enter the number here: '))

    print('You have selected to level up this pokemon:')
    print(p2pokelist[pokeselector - 1])

    print('you currently have', player2candies, 'candies')
    print()
    print('----- Leveling Rules -----')
    print('Level 40 is the maximum')
    print(
        'One (1) candy is required to level the Pokemon by 1 level from levels 1–30, two (2) candies arerequired to level-up to levels 31–40')
    print('CP will also be updated when leveling')
    print()
    print()

    currLevel2 = int(p2pokelist[pokeselector - 1][2])
    print('candy count =', player2candies)
    if currLevel2 == 40:
        print('Your pokemon is already max level')

    if currLevel2 >= 30:
        if ((player2candies // 2) + currLevel2) <= 40:
            currLevel2 = currLevel2 + (player2candies // 2)
        if ((player2candies // 2) + currLevel2) >= 40:
            currLevel2 = 40                                         # SAME PROCESS AS ABOVE REFERENCE PAST COMMENTS

    if currLevel2 < 30:
        key2 = 30 - currLevel2
        if player2candies <= key2:
            currLevel2 = currLevel2 + player2candies

        if player2candies > key2:
            currLevel2 = currLevel2 + key2
            player2candies = player2candies - key2
            currLevel2 = currLevel2 + (player2candies // 2)
    print('----------------------------------------------------------------------------')
    print('The new pokemon level is ', currLevel2)

    print('Now the pokemons new CP will be calculated')
    print()
    time.sleep(3)

    p2battleinfolist = []
    p2battleinfolist.append(p2pokelist[pokeselector - 1][0])

    ogCP2 = int(p2pokelist[pokeselector - 1][1])                    # SAME PROCESS AS ABOVE REFERENCE PAST COMMENTS
    if currLevel2 <= 30:
        newCP2 = ogCP2 + (2 * math.sqrt(currLevel2))
    if currLevel2 > 30:
        newCP2 = ogCP2 + math.sqrt(currLevel2)
    p2battleinfolist.append(round(newCP2, 1))
    p2battleinfolist.append(currLevel2)
    # -----------------------------------------------------------------------------------------------
print('----------------------------------------------------------------------------------')
print('Now what we have all been waiting for.... BATTLING')
print()
print('The rules are simple... the winner will be determined by the product of level*CP*random number')
print('you had to strategize for the level and cp but the random number will be a gamble.')
print('the random number can be anywhere between 1 and 5 inclusive')
print('-------------------------------------------------------------')      # describing the directions
time.sleep(2)
print('player 1',player1)
print('Your current pokemon and stats are',p1battleinfolist)
randonum = random.randint(1,6)
print('your random number is',randonum)                 #assigns the random number portion as vsariable
print('final score is:')
score1 = randonum * p1battleinfolist[1] * p1battleinfolist[2] # calculations
print(score1)
print('--------------------------------------------------------------------------------------------------------------')
time.sleep(2)
print('player 2',player2)
print('Your current pokemon and stats are',p2battleinfolist)
randonum2 = random.randint(1,6)
print('your random number is',randonum2)            # random number
print('final score is:')
score2 = randonum2 * p2battleinfolist[1] * p2battleinfolist[2] # calculations
print(score2)

#-------------------------------------------------------------------------------------




print('BATTLE TIME')
time.sleep(1)
print('battling...')
time.sleep(1)
print('battling...')
time.sleep(1)                   # delays to create excitement
print('battling...')
time.sleep(1)
print('battling...')
print()

if score1 > score2:
    print('CONGRATULATIONS!',player1,'has defeated',player2)
    print(player1, 'has won!')
                                                    # if branches that determine winner
if score1 < score2:
    print('CONGRATULATIONS!',player2,'has defeated',player1)
    print(player2, 'has won!')











