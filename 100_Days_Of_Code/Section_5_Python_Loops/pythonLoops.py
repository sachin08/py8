#For Loop

#1. for in -> for item in list_of_items:

fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

#2. for loops and range() function
#range() function -> really helpful if you want to generate a range of numbers to loop through
#syntax -> for number in range(a,b): -> range(a,b) -> includes a but not b

for number in range(1, 10):
    print(number) #prints 1 to 9 but not 10.

#range(a,b) by default steps through from a to b increasing by 1, if you want it to increase/step through by any other number, then you need to provide another input 'step' to the range()
for number in range(1,11,3):
    print(number) #prints 1, 4, 7, 10 i.e., steping/increasing by 3 between the specified range 1 to 11.

#How to add up all numbers from 1 to 100 using range()?

total=0
for number in range(1,101):
    total += number
print(total) #5050
