# Data Structures -> way of storing and organizing data
# eg., names of cities in a country -> makes sense to store them together as they kind of belong together??
# eg., when you want to have order in your data like storing names in a queue of people


# lists -> items in [] in python having same or mixed data type
# syntax -> fruits = ["Apple", "Banana"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Maryland"]

# List of us states in order of their joining? -> it is determined by the position of the item in the list.

# print a specific ordered item in the list? -> print(<listname>[<index_number/offset]) eg., print(states_of_america[0] -> prints Delaware)

print(states_of_america[0])

# in python if you use a negative index/offset starting from -1 while getting item from a list it starts moving from backwards of the list data structure items.
# eg., print(states_of_america[-1] -> will start printing from end of the list and print Maryland

print(states_of_america[-1])



# change items in a list 

states_of_america[1] = "Pencilvania" #override the original value
print(states_of_america)

# add an item in a list say towards the end

states_of_america.append("SachinLand")
print(states_of_america)


# complete list of functions -> check the Python Docs.

# add a list to end of another list or add a bunch of items say towards the end

states_of_america.extend(["ShefaliLand", "DadLand", "MomLand", "SisLand"])
print(states_of_america)

# Index Errors and Nested Lists
# eg., print(states_of_america[50]) -> 'IndexError: list index out of range' as 50 'index/offset' doesn't exist, there are 50 states but since the index starts from 0, the 50th state would be indexed as the 49th one.


# print(states_of_america[50])

# len() function in Python -> returns the number of items in a container -> last index would length - 1.
print(len(states_of_america))

# Nested Lists -> List within a list

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Bell", "Celery", "Tomatoes"]
dirty_dozen = [fruits, vegetables] #dirty_dozen is a NestedList

print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][2])
print(dirty_dozen[1][3])