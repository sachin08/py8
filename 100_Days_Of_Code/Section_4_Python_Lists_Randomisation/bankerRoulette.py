import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length_of_list = len(names)
n = random.randint(0,length_of_list - 1)

person = names[n]

print(f"{person} is going to buy the meal today!")