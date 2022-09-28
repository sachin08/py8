num_char = len(input("What is your name?"))
print("Your name has " + num_char + "characters.") #o/p -> throws error as string and integer can not be concatenated

print(type(num_char)) #o/p : class int, type() tells you the type of input data

#typecasting

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a)) #o/p returns class int

a = str(123)
print(type(a)) #o/p returns class str

a = float(123)
print(type(a)) #o/p returns class float

print(70 + int("100")) #o/p 170, str is typecasted to int and then added with already int

print(70 + float("100.5")) #o/p 170.5, str is typecasted to float and then added with int

print(str(70) + str(100)) #o/p 70100
