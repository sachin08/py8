# input() will get user input in console and replace the "What is your name?" text with it
# print() will further concatenate "Hello " and the o/p of the input() function
print("Hello " +input("What is your name?"))

# Variables

name = input("What is your name?")
length = len(name)
print(length)

# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

temp=a
a=b
b=temp

print("a: " + a)
print("b: " + b)
