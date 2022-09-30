print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

 ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')

if direction.lower() == "right":
    action = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if action.lower() == "swim":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if color.lower() == "yellow":
            print("You Win! You have found the treasure! :D")
        elif color.lower() == "red":
            print("It's a room full of poisnous snakes! Game Over.")
        elif color.lower() == "blue":
            print("You enter a room of beasts! Game Over.")
        else:
            print("You chose a door to another dimension! Game Over and Good Luck.")
    else:
        print("You got attacked by an angry trout! Game Over.")
else:
    print("You fell into a hole! Game Over.")
