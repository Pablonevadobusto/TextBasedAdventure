def IntroRoom():
    directions = ["forward", "backward", "right"]   # List items used in the while loop to go over and over if user hits anything else. Otherwise, will lead the user to other room
    print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    print("Options: forward, backward, right, left")
    user = ""
    while user not in directions:
        user = input()
        if user.lower().strip() == "forward":     # lower() and strip() modules make True the line even if the user enters the key word with capital letters and with spaces (behind or after the word)
            WolfRoom()
        elif user.lower().strip() == "backward":
            SicknessRoom()
        elif user.lower().strip() == "right":
            GhostRoom()
        elif user.lower().strip() == "left":
            print("You hit a wall, please choose other option.")
        else:
            print("Please enter a valid option.")

def GhostRoom():
    directions = ["backward"]
    print("You are now in a dark and silent room with murdered people lying on the floor. Where would you like to go?")
    print("Options: forward, backward, right, left")
    user = ""
    while user not in directions:
        user = input()
        if user.lower().strip() == "left":
            print("You made it! You have found an exit")
            quit()
        elif user.lower().strip() == "right":
            print("Multiple ghosts start emerging as you enter the room. You are killed.")
            quit()
        elif user.lower().strip() == "forward":
            print("You hit a wall, please choose other option.")
        elif user.lower().strip() == "backward":
            IntroRoom()
        else:
            print("Please enter a valid option.")

def SicknessRoom():
    directions = ["backward"]
    print("You feel sick suddenly. Where would you like to go?")
    print("Options: forward, backward, right, left")
    user = ""
    while user not in directions:
        user = input()
        if user.lower().strip() == "backward":
            IntroRoom()
        elif user.lower().strip() == "forward":
            print("After opening up the door you find drugs that make you feel better. However, this is and dead-end hallway and you need to go back.\nOptions: forward, backward, right, left")
        elif user.lower().strip() == "left":
            print("You worsen and die.")
            quit()
        elif user.lower().strip() == "right": 
            print("You made it! You have found an exit")
            quit()
        else:
            print("Please enter a valid option.")
    
def WolfRoom():
    directions = ["backward", "left"]
    print("You find a room with a pack of wolves. Where would you like to go?")
    print("Options: forward, backward, right, left")
    user = ""
    while user not in directions:
        user = input()
        if user.lower().strip() == "forward":
            print("You hit a wall, please choose other option.")
        elif user.lower().strip() == "backward":
            IntroRoom()
        elif user.lower().strip() == "right":
            print("You accidentally hurt a cub and the pack of wolves attack you and you are killed.")
            quit()
        elif user.lower().strip() == "left":
            SwimRoom()
        else: 
            print("Please enter a valid option.")

def SwimRoom():
    directions = ["backward"]  
    print("You are now in a swimming pool. Where would you like to go?")
    print("Options: forward, backward, right, left")
    user = ""
    while user not in directions:
        user = input()
        if user.lower().strip() == "right":
            print("You hit a wall, please choose other option.")
        elif user.lower().strip() == "left":
            print("You made it! You have found an exit")
            quit()
        elif user.lower().strip() == "backward":
            WolfRoom()
        elif user.lower().strip() == "forward":
            print("You get drowned as loads of water coming in. You die")
        else: 
            print("Please enter a valid option.")

while True:   # after defining all variables, this block of code will greet the user to the game as well as leading the player to the starting room.
    print("Welcome to Text Based Adventure Game!!.\n"
        "You have just awaken and you get yourself disoriented and do not know where you are. The aim is to find the way out by choosing the right direction. Would you please like to enter your name?")
    name = input()
    print("Good luck", name)
    IntroRoom()
