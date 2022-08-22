


# this file is where the minigame was developed for the catching procedure
# this is a working game function


def minigame():
    import random
    # --------------------------------------------- instructions
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

    randRange = 7

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

    return [score, candies]




listtt = minigame()
print(listtt)
a = listtt[1]+2
print(a)