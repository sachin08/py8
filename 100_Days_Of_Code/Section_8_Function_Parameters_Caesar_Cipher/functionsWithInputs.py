# def greet(name):
#     for _ in range(3):
#         print(f"Hello {name}")

# greet("Sachin")

#multipleInputs

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#greet_with("Sachin", "Dublin") #Positional Arguments
# #or 
greet_with(location="Dublin", name="Sachin") #Keyword Arguments
#greet_with("Shefali", "Galway") #or 
greet_with(location="Galway", name="Shefali")
greet_with("Maa", "India") #or greet_with(location="India", name="Maa")