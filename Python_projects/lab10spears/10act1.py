#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Nathaniel Bush, Alan Albiter, Chase Albright, Joshua, Campos
# Section:     480
# Assignment:  Lab Assignment 10
# Date:        27 October 2020


# this gets the values
x_list = []
y_list = []
user_file = input('What file would you like to use? ')
with open (user_file) as myfile:
    for line in myfile:
        if 1 < len(line) < 10:
            x1,x2 = map(float,line.split(','))
            x_list.append(float(x1))
            y_list.append(float(x2))


# sorting x and y values
for j in range(len(x_list)):  # loops until everything is sorted
    for i in range(int(len(x_list) - 1)):  # loops until the length minus 1
        if x_list[i] > x_list[i + 1]:  # finds if the left value is bigger than the right
            x_list[i], x_list[i + 1] = x_list[i + 1], x_list[i]  # sorts if above statement true
            y_list[i], y_list[i + 1] = y_list[i + 1], y_list[i]  # sorts if above statement true
print(x_list)
print(y_list)


# interpolation and extrapolation
print('Enter q to end interpolation and extrapolation')
interx = []
intery = []


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
y = 0
while x != 'q':
    x = input("x = ")

    if x != 'q':
        interx.append(int(x))
        if int(x) < x_list[0]:  # extrapolates if given x is before any x values
            xk = x_list[0]  # x value before given x value
            yk = y_list[0]  # y value before given x value
            xk0 = x_list[1]  # x value before closest x value
            yk0 = y_list[1]  # y value before closest y value
            y = round(yk0 + ((int(x) - xk0) / (xk - xk0)) * (yk - yk0), 1)

        elif x_list[0] <= int(x) <= x_list[-1]:  # interpolates
            for i in range(len(x_list)):
                if int(x) > x_list[i]:
                    i += 1
                    x0 = x_list[i - 1]
                    y0 = y_list[i - 1]
                    x1 = x_list[i]
                    y1 = y_list[i]
            y = round(y0 + (int(x) - x0) * ((y1 - y0) / (x1 - x0)), 1)

        elif int(x) > x_list[-1]:  # extrapolates if given x is after any x values
            xk = x_list[-1]  # x value before given x value
            yk = y_list[-1]  # y value before given x value
            xk0 = x_list[-2]  # x value before closest x value
            yk0 = y_list[-2]  # y value before closest y value
            y = round(yk0 + ((int(x) - xk0) / (xk - xk0)) * (yk - yk0), 1)

        intery.append(int(y))


print('The x,y values for the data point that is interpolated/extrapolated is:')
print('(',interx[0],',',intery[0],')')

# THIS SECTION IS FOR PLOTTING

import matplotlib.pyplot as plt

plt.scatter(x_list,y_list,color='k', label='Cheese')
plt.plot(x_list,y_list,'--k')

plt.scatter(interx,intery,color='b') #properties of lines
for i in interx: # loop through each val in lists
    for v in intery:
        #plt.axvline(x=i,color='green',linestyle='--')
        plt.vlines(x=i,ymin=0,ymax=v,color='green',linestyle='--')
        #properties of arrows
        arrow_properties = dict(
            facecolor="black", width=0.5,
            headwidth=2, shrink=0.1)

        plt.annotate(
            "Data point\n y="+str(v), xy=(i, v),
            xytext=(i-2, v),
            arrowprops=arrow_properties)

plt.xlabel('Time')
plt.ylabel('Cheese')
plt.title('Cheese vs. Time')
plt.legend()
plt.show()