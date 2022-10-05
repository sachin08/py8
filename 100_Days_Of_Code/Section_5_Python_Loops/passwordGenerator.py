import random

ls_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ls_numbers = ['0','1','2','3','4','5','6','7','8','9']
ls_symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

password = ''

for n1 in range(0,letters):
    random.shuffle(ls_letters) #could have also used random.choice(ls_letters) i.e., password += random.choice(ls_letters)
    password += ls_letters[n1]

for n2 in range(0,symbols):
    random.shuffle(ls_numbers) #could have also used random.choice()
    password += ls_numbers[n2]

for n3 in range(0,symbols):
    random.shuffle(ls_symbols) #could have also used random.choice()
    password += ls_symbols[n3]

f_password = ''.join(random.sample(password,len(password))) #random.sample is for strings and tuples, shuffle is for lists, objects
print(f"Here is your password:{f_password}") 


