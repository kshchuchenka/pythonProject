# Import Random variable generators
import random

# Create a random list with length 100 and numbers from 0 to 1000 by using cycle 'for' and 'append' to form 'randomList'
randomlist = []
for i in range(0, 100):
    n = random.randint(0, 1000)
    randomlist.append(n)
print("Начальный список:")
print(randomlist)

# create 'randomlist1' as a copy of randomLlist to use it for sorting
randomlist1 = randomlist[:]
# create empty list 'sortlist' to fill it in with sorted results
sortlist = []
# use 'while' statement for identifying minimum value in the list 'randomlist1'
while randomlist1:
    # set the first element of the 'randomlist1' list as a minimum value
    minValue = randomlist1[0]
    # compare min value with each element value from the list
    for z in randomlist1:
        # if element value less than minValue, replace minValue with the lowest value
        if z < minValue:
            minValue = z
    # 'append' new sorted list with the lowest value
    sortlist.append(minValue)
    # delete lowest value from the 'randomlist1'
    randomlist1.remove(minValue)

# new sorted list
print("Отсортированный список:")
print(sortlist)

# use cycle 'for' and 'append' to form  even and odd lists based on 'randomList'
evenlist = []
oddlist = []
for x in randomlist:
    #
    if x % 2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)
# printing both even and odd lists for visibility
print("Список четных:")
print(evenlist)
print("Список нечетных:")
print(oddlist)

# using functions sum() and len() to calculate average value for even and odd lists and print out the result of calculation
avgEven = sum(evenlist) / len(evenlist)
print("Среднее арифметическое списка четных:", avgEven)
avgOdd = sum(oddlist) / len(oddlist)
print("Среднее арифметическое списка нечетных:", avgOdd)
