#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 5
# Date:        22 september 2020
#-----------------------------------------------------------------------------------------------------
print('------------------------------------------------------')
print('The fibonacci sequence begins 0,1,1,2,3,5,8,13...after the 1\'s, no value is repeated twice.')
print('Enter the sequence one at a time, wrong values will terminate sequence')
print('------------------------------------------------------')
n = int(input("Enter any positive integer to begin: "))
a = 0
b = 1
sum = 0
count = 1
print('------------------------------------------------------')
print("Fibonacci Series: ")
while n >= 0:
    n = int(input("Enter the value of 'n': "))

    if n == b or n == a:
      print(n, 'is correct')
    a = b
    b = sum
    sum = a + b
    if n == sum-a and n > 1:
      print(n, 'is correct')
    if n != sum-a:
      print(n, 'is not correct')
      break