#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Nathaniel Bush, Alan Albiter, Chase Albright, Joshua, Campos
# Section:     480
# Assignment:  Lab Assignment 2
# Date:        6 October 2020

### opens the file ###
name = input('First off, what is the name for your dependent variable?: ')
file = open('nailedIt.txt', 'w')
file.write('---------------------------------------------------------------------\n')
file.write('Team 1 Chase Albright, Nathaniel Bush, Joshua Campos, Alan Albiter\n')
file.write('October 20, 2020\n')
file.write('\n')
file.write('x-values = time, y-values = '+name+'\n')
file.write('---------------------------------------------------------------------\n')

### first part ###

#  Ask for x and y points until they input a letter q for x, don’t use it
x = 0
y = 0
x_list = []  # creates an empty  x list
y_list = []  # creates an empty y list
while x != 'q':  # while x does not equal q
    x = input("x = ")  # asks for x values
    if x != 'q':
        y = input("y = ")  # asks for y values
        x_list.append(int(x))  # appends it onto a list
        y_list.append(int(y))  # appends it onto a list
print(x_list)
print(y_list)

for i in range(len(x_list)):  # writes all the x and y values onto the file
    file.write(str(x_list[i])+', '+str(y_list[i])+'\n')

file.write('---------------------------------------------------------------------\n')

print('---------------------------------------')

# sorting x and y values
for j in range(len(x_list)):  # loops until everything is sorted
    for i in range(int(len(x_list) - 1)):  # loops until the length minus 1
        if x_list[i] > x_list[i + 1]:  # finds if the left value is bigger than the right
            x_list[i], x_list[i + 1] = x_list[i + 1], x_list[i]  # sorts if above statement true
            y_list[i], y_list[i + 1] = y_list[i + 1], y_list[i]  # sorts if above statement true
print(x_list)
print(y_list)

### third part ###

# interpolation extrapolation
x0 = None  # the x value before given x value
y0 = None  # y value before given x value
x1 = None  # x value after given x value
y1 = None  # y value after given x value
x = 0  # the input given
#  inter = y0 + (x - x0) * ((y1 - y0) / (x1 - x0))
xk = 0  # x value before given x value
yk = 0  # y value before given x value
xk0 = 0  # x value before closest x value
yk0 = 0  # y value before closest y value
#  extra = yk0 + ((x - xk0) / (xk - xk0)) * (yk - yk0)

equation = ''
while x != 'q':
    x = input("x = ")
    if x != 'q':

        if int(x) < x_list[0]:  # extrapolates if given x is before any x values
            xk = x_list[0]  # x value before given x value
            yk = y_list[0]  # y value before given x value
            xk0 = x_list[1]  # x value before closest x value
            yk0 = y_list[1]  # y value before closest y value
            y = round(yk0 + ((int(x) - xk0) / (xk - xk0)) * (yk - yk0), 1)
            equation = 'Extrapolation'

        elif x_list[0] <= int(x) <= x_list[-1]:  # interpolates
            for i in range(len(x_list)):
                if int(x) > x_list[i]:
                    i += 1
                    x0 = x_list[i - 1]
                    y0 = y_list[i - 1]
                    x1 = x_list[i]
                    y1 = y_list[i]
            y = round(y0 + (float(x) - x0) * ((y1 - y0) / (x1 - x0)), 1)
            equation = 'Interpolation'

        elif int(x) > x_list[-1]:  # extrapolates if given x is after any x values
            xk = x_list[-1]  # x value before given x value
            yk = y_list[-1]  # y value before given x value
            xk0 = x_list[-2]  # x value before closest x value
            yk0 = y_list[-2]  # y value before closest y value
            y = round(yk0 + ((int(x) - xk0) / (xk - xk0)) * (yk - yk0), 1)
            equation = 'Extrapolation'

        file.write(str(x) + ', ' + str(y).ljust(9) + equation)
        file.write('\n')