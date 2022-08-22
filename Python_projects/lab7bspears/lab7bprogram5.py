# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        chase albright
# Section:     480
# Assignment:  lab 7b
# Date:        10/6/2020
# -------------------------------------------------------------------------------------------------
scores1 = 1
scores2 = 1
player = ''
total_list_score = []
players_list = []

while scores1 >= 0:
    score1 = int(input('Enter a score for round 1 or enter a negative number to stop: '))
    if scores1 >= 0:
        score2 = int(input('Enter a score for round 2: '))
        player = str(input("Enter the players name: "))
        total = scores1 + scores2
        total_list_score.append(total)
        players_list.append(player)

        print(players_list)
        print(total_list_score)

length = len(total_list_score)

list1 = total_list_score
for x in range(length):
    for y in range(0, length-x-1):
        if list1[y] > list1[y+1]:
            list1[y], list1[y+1]= list1[y+1], list1[y]

if length%2==0:
   m1=list1[length//2]
   m2=list1[length//2-1]
   med=(m1+m2)/2
else:
   med=list1[length//2]

print("The players did not make the cut are(scores were too high) ",med)
print("The players Below cut are")
for i in range(length):
   if total_list_score[i]<med:
       print(players_list[i],end=" ")
print()
print("The players Below cut are(scores were good!)")
for i in range(length):
   if not total_list_score[i]<med:
       print(players_list[i],end=" ")
