alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
go_ahead = 'yes'

#Encryption
def encrypt(msg, snum):
    final_msg = ''
    new_index = 0
    for i in msg:
        if not alphabet.__contains__(i):
            final_msg += i
        else:
            new_index = alphabet.index(i) + snum
            if new_index > 25:
                final_msg += alphabet[new_index - len(alphabet)]
            else:
                final_msg += alphabet[new_index]
    print(f"Here\'s the encoded result: {final_msg}")

#Decryption
def decrypt(msg, snum):
    final_msg = ''
    new_index = 0
    for i in msg:
        if not alphabet.__contains__(i):
            final_msg += i
        else:
            new_index = alphabet.index(i) - snum
            if new_index < 0:
                final_msg += alphabet[len(alphabet) - abs(new_index)]
            else:
                final_msg += alphabet[new_index]
    print(f"Here\'s the encoded result: {final_msg}")

while go_ahead == 'yes':
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if action == 'encode' or action == 'decode':
        msg = input("Type your message:\n")
        snum = int(input("Type the shift number:\n"))
        if action == 'encode':
            encrypt(msg.lower(),snum)
        else:
            decrypt(msg.lower(),snum)
    else:
        print("Incorrect input. Exiting!")
        exit(0)
    go_ahead = input("Type \'yes\' if you want to go again, otherwise type \'no\'\n")
    