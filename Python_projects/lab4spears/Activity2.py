# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright, Joshua Campos, Alan Albiter, and Nathaniel Bush
# Section:     480
# Assignment:  Lab 4
# Date:        15 September 2020
# -----------------------------------------------------------------------------------------------------------------------
# FINDING THE AGE OF LADY
print('Welcome! If you are a woman between the ages of 20 to 59 we will be able to calculate your potential risk for heart disease ')
age = float(input('What is your age? (between 20 and 59)'))
agepoints = 0
if 20 <= age <= 34:
    agepoints = -7
elif 34 < age <= 39:
    agepoints = -3
elif 39 < age <= 44:
    agepoints = 0
elif 44 < age <= 49:
    agepoints = 3
elif 49 < age <= 54:
    agepoints = 6
elif 54 < age <= 59:
    agepoints = 8
print('Your points for your age is', agepoints)
# ------------------------------------------------------------------------------
print('------------------------------------------------------------------------------')
# FINDING CHOLESTEROL POINTSSSS
print('Now we need your cholesterol level')
chole = float(input('What is your cholesterol level?'))
cholepoints = 0
if chole < 160:
    # for any age cholepoints is 0
    cholepoints = 0

elif 160 <= chole <= 199:
    if 20 <= age <= 39:
        cholepoints = 4
    elif 39 < age <= 49:
        cholepoints = 3
    elif 49 < age <= 59:
        cholepoints = 2

elif 199 < chole <= 239:
    if 20 <= age <= 39:
        cholepoints = 8
    elif 39 < age <= 49:
        cholepoints = 6
    elif 49 < age <= 59:
        cholepoints = 4

elif 239 < chole < 280:
    if 20 <= age <= 39:
        cholepoints = 11
    elif 39 < age <= 49:
        cholepoints = 8
    elif 49 < age <= 59:
        cholepoints = 5

elif chole >= 280:
    if 20 <= age <= 39:
        cholepoints = 13
    elif 39 < age <= 49:
        cholepoints = 10
    elif 49 < age <= 59:
        cholepoints = 7
print('Your cholesterol points for you age group and cholesterol levels is', cholepoints)
print('------------------------------------------------------------------------------')
# FINDING SMOKER POINTSSS
print('Now we must determine your smoker points!')

smokehabits = input('Are you a smoker(smoker/nonsmoker)?')
smokepoints = 0

if smokehabits == 'smoker':
    if 20 <= age <= 39:
        smokepoints = 9
    elif 39 < age <= 49:
        smokepoints = 7
    elif 49 < age <= 59:
        smokepoints = 4
elif smokehabits == 'nonsmoker':
    if 20 <= age <= 39:
        smokepoints = 0
    elif 39 < age <= 49:
        smokepoints = 0
    elif 49 < age <= 59:
        smokepoints = 0
print('your smoke habit points are', smokepoints)
print('------------------------------------------------------------------------------')
print('What is your hdl levels')
hdl = float(input('input HDL levels'))  # This takes the HDL level of the lady
hdl_points = 0

if hdl >= 60:
    hdl_points = -1
elif 50 <= hdl < 60:
    hdl_points = 0
elif 40 <= hdl < 50:
    hdl_points = 1
elif hdl < 40:
    hdl_points = 2


print('your hdl points are', hdl_points)

print('------------------------------------------------------------------------------')
print('Now we can calculate BP points')
bp = float(input('What is your BP level?'))

iftreated = input('Is your BP treated (treated/untreated)?')

bppoints = 0

if iftreated == 'treated':
    if bp < 120:
        bppoints = 0
    elif 120 <= bp <= 129:
        bppoints = 3
    elif 129 < bp <= 139:
        bppoints = 4
    elif 139 < bp < 160:
        bppoints = 5
    elif bp >= 160:
        bppoints = 6

if iftreated == 'untreated':
    if bp < 120:
        bppoints = 0
    elif 120 <= bp <= 129:
        bppoints = 1
    elif 129 < bp <= 139:
        bppoints = 2
    elif 139 < bp < 160:
        bppoints = 3
    elif bp >= 160:
        bppoints = 4
print('Your BP points are', bppoints)
print('------------------------------------------------------------------------------')
total = bppoints + hdl_points + smokepoints + cholepoints + agepoints
print('Your total points are', total)
print('------------------------------------------------------------------------------')
print('Now we can calculate your risk percentage for heart disease')
print('\n')

risk = 0
if total < 9:
    risk = '<1'
elif 9 <= total <= 12:
    risk = 1
elif 13 <= total <= 14:
    risk = 2
elif total == 15:
    risk = 3
elif total == 16:
    risk = 4
elif total == 17:
    risk = 5
elif total == 18:
    risk = 6
elif total == 19:
    risk = 8
elif total == 20:
    risk = 11
elif total == 21:
    risk = 14
elif total == 22:
    risk = 17
elif total == 23:
    risk = 22
elif total == 24:
    risk = 27
elif total == 25:
    risk = 30
elif total > 25:
    risk = '>30'


print('Your risk for heart disease if you are a woman between the ages of 20 and 59 is ', risk,'%')