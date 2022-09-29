print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

#if-else

#if height >= 120:
#    print("You can ride the rollercoaster!") #block of code lives inside the if statement
#else:
#    print("Sorry, you have to grow taller before you can ride.") #block of code lives inside the else statement

#Comparison Operators
#>, <, >=, <=, ==, !=

#Nested if/else

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#if elif else

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#Multiple if & if/elif/else
#Multiple ifs -> All conditions are checked which is not the case in if/elif/else

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")



#CombineIfConditions

##Logical Operators - and, or, not

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")