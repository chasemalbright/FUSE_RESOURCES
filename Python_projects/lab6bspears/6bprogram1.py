# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 6b
# Date:        9/29/20
#-----------------------------------------------------------------------------------------------------------------


import statistics
from typing import List, Any, Union

mossgrowth: List[Union[float, Any]] = [15.80, 19.60, 21.85, 33.61, 49.73, 51.27, 56.26, 63.06, 76.56, 76.57, 85.78, 90.74, 92.60, 99.71,
100.51, 101.12, 101.25, 102.19, 104.85, 110.59, 125.92, 131.25, 136.04, 141.15, 148.54, 150.02]

# add num to list
mossgrowth.append(162.76)

# add to 9th day
mossgrowth.insert(8, 71.01)

print('The length of the list is', len(mossgrowth), 'days of data points')
print('----------------------------------------------------------------------------------')

# splitting lists
week1 = mossgrowth[0:7]
week2 = mossgrowth[7:14]
week3 = mossgrowth[14:21]
week4 = mossgrowth[21:29]

print('Average moss mass in week 1:  ',round(statistics.mean(week1),2),' g')
print('Average moss mass in week 2:  ',round(statistics.mean(week2),2),' g')
print('Average moss mass in week 3:  ',round(statistics.mean(week3),2),'g')
print('Average moss mass in week 4:  ',round(statistics.mean(week4),2),'g')
print('----------------------------------------------------------------------------------')

a = mossgrowth[1]-mossgrowth[0]
b = mossgrowth[2]-mossgrowth[1]
c = mossgrowth[3]-mossgrowth[2]
d = mossgrowth[4]-mossgrowth[3]
e = mossgrowth[5]-mossgrowth[4]
f = mossgrowth[6]-mossgrowth[5]
g = mossgrowth[7]-mossgrowth[6]
week1pd = round((a+b+c+d+e+f+g)/7,2)

h = mossgrowth[8]-mossgrowth[7]
i = mossgrowth[9]-mossgrowth[8]
j = mossgrowth[10]-mossgrowth[9]
k = mossgrowth[11]-mossgrowth[10]
l = mossgrowth[12]-mossgrowth[11]
m = mossgrowth[13]-mossgrowth[12]
n = mossgrowth[14]-mossgrowth[13]
week2pd = round((h+i+j+k+l+m+n)/7,2)

a1 = mossgrowth[15]-mossgrowth[14]
b1 = mossgrowth[16]-mossgrowth[15]
c1 = mossgrowth[17]-mossgrowth[16]
d1 = mossgrowth[18]-mossgrowth[17]
e1 = mossgrowth[19]-mossgrowth[18]
f1 = mossgrowth[20]-mossgrowth[19]
g1 = mossgrowth[21]-mossgrowth[20]
week3pd = round((a1+b1+c1+d1+e1+f1+g1)/7,2)

h1 = mossgrowth[22]-mossgrowth[21]
i1 = mossgrowth[23]-mossgrowth[22]
j1 = mossgrowth[24]-mossgrowth[23]
k1 = mossgrowth[25]-mossgrowth[24]
l1 = mossgrowth[26]-mossgrowth[25]
m1 = mossgrowth[27]-mossgrowth[26]
n1 = mossgrowth[27]-mossgrowth[27]
week4pd = round((h1+i1+j1+k1+l1+m1+n1)/7,2)

print('Average daily growth during week 1:  ', week1pd, 'g/day')
print('Average daily growth during week 2:  ', week2pd, 'g/day')
print('Average daily growth during week 3:  ', week3pd, 'g/day')
print('Average daily growth during week 4:  ', week4pd, 'g/day')
print('----------------------------------------------------------------------------------')
print('Average growth for the month is:',round((week1pd+week2pd+week3pd+week4pd)/4,2), 'g/day')






