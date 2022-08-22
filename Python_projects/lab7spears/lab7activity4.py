# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        chase albright joshua campos alan albiter nathaniel bush
# Section:     480
# Assignment:  lab 7
# Date:        10/6/2020
# -------------------------------------------------------------------------------------------------

print('Welcome to the widget calculator')
print()
num = 1

list = []

day = 0
while num >= 0:
    num = int(input('Please enter a positive integer or a negative number to quit: '))
    if num >= 0:
        list.append(num)
        day +=1

#print(day)
#print(list)
print('-------------------------------------------------------------------------------------------------------------------------------')
for interval in range(1, day):
    decrease = 0
    increase = 0
    firstnum = 0
    secondnum = firstnum + interval
    count = 0

    while secondnum <= (day-1):
        diff = list[secondnum]-list[firstnum]
        if diff > 0:
            increase +=1
        elif diff < 0:
            decrease -= 1
        firstnum +=1
        secondnum = firstnum + interval
        count += 1

    a = str(interval)
    b = str(round(increase/count*100, 1))
    c = str(round(abs(decrease/count*100), 1))
    print("For "+ a+"-day intervals, "+b+"% of the intervals had increasing and "+c+ "% had decreasing productions.")