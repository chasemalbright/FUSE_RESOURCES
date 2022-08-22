# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 6b
# Date:        9/29/20
#-----------------------------------------------------------------------------------------------------------------
evenlist = []
list = []
num = input('enter \'start\' to begin:  ')
print()
while num != 'q' or num == 'start':
    num = input('Enter a value or \'q\' to quit:  ')
    if num != 'q':
        list.append(int(num))
    if num == 'q':
        break
print('this is the original list')
print(list)
for i in list:
    ii = int(i)
    if ii%2 == 0:
        evenlist.append(ii)
print('this is the even list in increasing order')
evenlist.sort()
print(evenlist)
