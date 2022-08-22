# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright, Joshua Campos, Alan Albiter, and Nathaniel Bush
# Section:     480
# Assignment:  Lab 7 - Activity 1/2: Warm Ups
# Date:        06 October 2020



# Activity 1
# create list of strings and print results
strings = ['arroyo', 'elephantine', 'toy', 'shines', 'diamond','iron','pancake']

count = 0
for b in strings:
    if b[0]==b[-1]:
        count += 1

print('In the number of strings in a list are', len(strings), "strings.")
print('There are ', count, 'strings where the first and last character are the same')

print('---------------------------------------------------------------------------------')

# Activity 2
# ask user for sentence and letter input
sentence = input("Type in a sentence: ")
letter = input("What letter are you looking for in the sentence?: ")

# count how many times letter is in sentence
count = sentence.count(letter)

# print results
print("In your sentence there is", count, "letter {}(s).".format(letter))
