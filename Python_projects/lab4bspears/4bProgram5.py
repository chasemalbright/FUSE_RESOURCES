# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright
# Section:     480
# Assignment:  Lab 4b
# Date:        19 September 2020
#------------------------------------------------------------------------------------------------
print('-----------------------------------------------------------------------------------')
print('Welcome, we will be calculating and interpreting important information')
print('about the relationship between strain(x) and stress(y) for this structural steel')
print('-----------------------------------------------------------------------------------')
print('\n')


# have user input the value greater than 0 for strain(x) varialble
strain = float(input('What is the value for strain? (Has to be > 0): '))
print('\n')
print('-----------------------------------------------------------------------------------')

# this is for case 1 strain is in O to A region 0 --> .02

# start value for stress ** forgot what its called**
stress = 0

#linear elastic region

if strain < 0:
    print('You have entered a negative value for strain this isn\'t possible')

elif strain == 0:
    print('You have entered 0, there is no strain applied to the steel with this value')

elif 0 < strain <= 0.02:
    stress = 2200 * strain
    print('The value you inputted falls within the linear elastic region')
    print('The slope of this region is called Young\'s Modulus')
    print('For',strain, 'as the value for strain,',stress, 'is the associated stress level')
    print('(',strain,',', stress,')')

# i believe this section is a horizontal line it also appears to be horizontal on the link to the civil engr site
elif 0.02 < strain <= 0.06:
    stress = (0 * strain) + 44
    print('The value you inputted falls within the plastic region')
    print('For', strain, 'as the value for strain,', stress, 'is the associated stress level')
    print('(', strain, ',', stress, ')')

#hardening region
elif 0.06 < strain <= 0.18:
    stress = ((400/3)*strain) + 36
    print('The value you inputted falls within the strain hardening region')
    print('This segment of the graph contains the point of maximum strength')
    print('For', strain, 'as the value for strain,', stress, 'is the associated stress level')
    print('(', strain, ',', stress, ')')

#necking region
elif 0.18 < strain < .265:
    stress = (-105.8823529 * strain) + 79.05882352
    print('The value you inputted falls within the necking region')
    print('For', strain, 'as the value for strain,', stress, 'is the associated stress level')
    print('(', strain, ',', stress, ')')

#fracture point
elif strain == .265:
    stress = int((-105.8823529 * strain) + 79.05882352)
    print('At this value, the fracture point has been reached')
    print('For', strain, 'as the value for strain,', stress, 'is the associated stress level')
    print('(', strain, ',', stress, ')')

# this is for high values and imaginary numbers
else:
    print('You have entered an invalid value or the value for strain has exceeded the fracture point')

print('-----------------------------------------------------------------------------------')