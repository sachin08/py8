#like dictionaries in real life, they allows us to group together and tag related pieces of information
#key & value pair {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over agin.",
}

#retrieve an item from the dictionary
#print(programming_dictionary["Bug"]) #take care of providing the key in the original data type, string in this case.


#adding new item to dictionary
programming_dictionary["Variable"] = "Anything which stores a value."
#print(programming_dictionary)

#empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary)

#Loop through a dictionary

for key in programming_dictionary:
    print(key) #prints the keys
    print(programming_dictionary[key]) #prints the actual value now