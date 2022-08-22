# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        chase albright
# Section:     480
# Assignment:  lab 7b
# Date:        10/6/2020
# -------------------------------------------------------------------------------------------------

num = int(input('How many classes are you taking this year?: '))

names = []
credithours = []
lettergrades = []
numgrade = []

#asking for info
for i in range(1, num+1):
    name = input('What is the class name?: ')
    credithour = int(input('What are the credit hours for this class?: '))
    lettergrade = input('What was the letter grade?: ')
    names.append(name)
    credithours.append(credithour)
    lettergrades.append(lettergrade)
    print()

#converting letter grades to gpa grades
gpanum = 0
for grade in lettergrades:
    if grade == 'a':
        gpanum = 4.00
    if grade == 'b':
        gpanum = 3.00
    if grade == 'c':
        gpanum = 2.00
    if grade == 'd':
        gpanum = 1.00
    if grade == 'f':
        gpanum = 0
    if grade == 'u':
        gpanum = 0
    numgrade.append(gpanum)

#multiplying values in the two lists to find grade points
gradepoints = 0
for i in range(0, num):
    gradepoints += numgrade[i]*credithours[i]


#calculate total credit hours
totalcredithours = 0
for x in credithours:
    totalcredithours += x

print()
GPA = gradepoints/totalcredithours
print('Your GPA for this year is:')

print(GPA)