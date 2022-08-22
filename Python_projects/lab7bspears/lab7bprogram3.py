# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        chase albright
# Section:     480
# Assignment:  lab 7b
# Date:        10/6/2020
# -------------------------------------------------------------------------------------------------

word =''
while word != 'stop':
    word = input('Please enter a word: ')
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y':
        print(word + 'yay')
    else:
        print(word[1:len(word)]+word[0]+'ay')
