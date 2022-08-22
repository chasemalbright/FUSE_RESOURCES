# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        CHase Albright
# Section:     480
# Assignment:  lab 9b
# Date:        10/20/10
#-------------------------------------------------------------------------------
age = 0
gender = ''
maleAge = []
femaleAge = []
genderList = []
with open('Student_Data_19Sp.txt', 'w') as file:

    file.write('{}     {}     {}     {}'.format('Gender','Number of Students','Minimum Age', 'Maximum Age'))
    file.write('\n')

    while age >= 0:
        age = int(input('What is student\'s age? Enter negative number to quit: '))
        if age >= 0:
            gender = input('What is the student\'s gender?(enter \'Male\' or \'Female\'): ')
            if gender == 'Male':
                maleAge.append(age)
                genderList.append(gender)
            if gender == 'Female':
                femaleAge.append(age)
                genderList.append(gender)

    maleNum = len(maleAge)
    maleMin = min(maleAge)
    maleMax = max(maleAge)


    femaleNum = len(femaleAge)
    femaleMin = min(femaleAge)
    femaleMax = max(femaleAge)

    file.write('{:6}     {:<18}     {:<11}     {:<1}'.format('Female', femaleNum, femaleMin, femaleMax))
    file.write('\n')
    file.write('{:6}     {:<18}     {:<11}     {:<1}'.format('Male', maleNum, maleMin, maleMax))

