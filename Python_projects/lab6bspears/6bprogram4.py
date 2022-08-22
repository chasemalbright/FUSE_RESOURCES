#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 6b
# Date:        9/29/20
#-----------------------------------------------------------------------------------------------------------------

# user created dictionary
Users = {}

#number of username and pass
num = int(input('How many username/passwords are there?: '))
print()
users = []
passwords = []
for i in range(num):
    users.append(input('What is the username: '))
print()
for i in range(num):
    passwords.append(input('What is the password: '))
print()
#makes the user dictionary

for i in range(num):
    Users[users[i]]=passwords[i]

stop = 1
while stop != 0:
    u = input('Enter username:  ')
    p = input('Enter password:  ')
    if u in Users and Users[u]==p:
        print('You have successfully logged in!')
        break
    else:
        if u in Users:
            print('Invalid password try again')
        else:
            print('Invalid username entered')