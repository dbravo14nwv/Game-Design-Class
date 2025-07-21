### Name - David Bravo
### Date - 7/21/2025
### Program Description - A small text adventure about a person stuck in a strange testing facility. It's small, but there's 7 endings to get.
### P.S. I wanted to make this way longer and much more intuitive, but the original project got corrupted 2 days ago, so I lost everything.

### Import system
import sys

### Import pygame
import pygame
pygame.init()

### Import fore, back, & style from colorama
from colorama import Fore,Back,Style

### Import random
import random

### Ask for the player's name
max_attempts = 3 # Set max attempts to enter Arkadi Petrov's name.
attempts = 0 # Set attempts to enter Arkadi Petrov's name to 0 before loop.

while attempts < max_attempts:
    name = input(Fore.BLUE + Style.NORMAL + "Please enter subject identification > ")

    if name == "Irina Petrov":
        print(Fore.RED + Style.BRIGHT + "... execute the program.")
        print(Fore.YELLOW + Style.BRIGHT + "ENDING 1")
        sys.exit()

    elif name == "Arkadi Petrov":
        attempts += 1

        if attempts < max_attempts:
            print(Fore.RED + Style.BRIGHT + "No, that is not your name.")

        else:
            print(Fore.RED + Style.BRIGHT + "You continue insisting... but it's pointless. Protocol terminated.")
            print(Fore.YELLOW + Style.BRIGHT + "ENDING 2")
            sys.exit()

    elif name == "D3-182":
        print(Fore.RED + Style.BRIGHT + "Very intriguing... how do you know your system id? This will require extensive research.")
        break  # Accept and continue

    else:
        break  # Any other name is accepted

print(Fore.BLUE + Style.NORMAL + "Initializing protocol for subject \"" + name + "\".")

### Print the intro message
print(Fore.WHITE + Style.NORMAL + "Your head feels heavy and your body feels weak. You can barely open your eyes, but a voice catches your attention.")
print(Fore.RED + Style.BRIGHT + "Wake up, " + name + ". You have much to see... and much to learn.")
print(Fore.WHITE + Style.NORMAL + "Suddenly, you feel a jolt of energy throughout your body. You get up and look around.")
print("You're in a dimly lit room with painted concrete walls and two doors on the opposite sides of each other.")

### Puzzle counter
puzzle_count = 0

### Game loop
while True:
    print(Fore.BLUE + Style.NORMAL + "What would you like to do?")
    print(Fore.BLUE + Style.NORMAL + "Examine Room\nExamine Walls\nEnter Left Room\nEnter Right Room")
    choice = input(" > ").strip().lower()

    if choice == "examine room":
        print(Fore.WHITE + Style.NORMAL + "You look around the room. There seems to only be a couple of useless children's puzzle sheets on the floor. Some are half solved; others completely blank.")
        print(Fore.BLUE + Style.NORMAL + "Would you like to try and solve one of these puzzles?")

        while True:
            print(Fore.BLUE + Style.NORMAL + "Yes\nNo")
            choice = input(" > ").strip().lower()

            if choice == "yes":
                random_integer = random.randint(1, 10)

                if random_integer == 10:
                    print(Fore.WHITE + Style.NORMAL + "You try to solve one of the puzzle sheets. However, the one you picked up seemed to get the better of you.")
                    print(Fore.RED + Style.BRIGHT + "Subject failed to solve crossword sheet #16... just like all the others.")
                    print(Fore.BLUE + Style.NORMAL + "Would you like to try and solve another puzzle?")
                else:
                    puzzle_count += 1
                    print(Fore.WHITE + Style.NORMAL + "You try to solve one of the puzzle sheets. It was trivial.")
                    print(Fore.RED + Style.BRIGHT + "Subject succeeded in solving one of the crossword sheets in record time. This is promising.")
                    print(Fore.BLUE + Style.NORMAL + "Would you like to try and solve another puzzle?")

                    if puzzle_count == 5:
                        print(Fore.WHITE + Style.NORMAL + "The fifth puzzle clicks into place... something has changed.")
                        print(Fore.RED + Style.BRIGHT + "Subject " + name + " has shown consistent cognitive performance. This may warrant release.")
                        print(Fore.YELLOW + Style.BRIGHT + "ENDING 6")
                        sys.exit()

            elif choice == "no":
                print(Fore.WHITE + Style.NORMAL + "You ignored the puzzle sheets on the floor.")
                print(Fore.RED + Style.BRIGHT + "Subject showed no interest in the crossword sheets. Disappointing to say the least.")
                break

            else:
                print(Fore.RED + Style.BRIGHT + "An interesting choice to say the least, but not one that can be fulfilled. Try again, " + name + ".")

    elif choice == "examine walls":
        print(Fore.WHITE + Style.NORMAL + "You examine the walls. One of them has a red line that reaches towards the left door. the other has a blue line that reaches towards the right door.")

    elif choice == "enter left room":
        print(Fore.WHITE + Style.NORMAL + "You enter the left room. A long hallway stretches down, and a red line on the wall reaches down a hall.")

        while True:
            print(Fore.BLUE + Style.NORMAL + "Would you like to go down the hall?")
            choice = input(" > ").strip().lower()

            if choice == "yes":
                go_down_hall = True

                while go_down_hall:
                    print(Fore.WHITE + Style.NORMAL + "You go down the hall. As you travel down, you see labs and office spaces.")
                    print(Fore.RED + Style.BRIGHT + "I see that you've left the testing room. I would advise your return.")
                    print(Fore.BLUE + Style.NORMAL + "You've reached a fork in the hall. You have 3 options.")

                    while True:
                        print(Fore.BLUE + Style.NORMAL + "Go Forward\nGo Right\nReturn")
                        choice = input(" > ").strip().lower()

                        if choice == "go forward":
                            print(Fore.WHITE + Style.NORMAL + "You go further down the hall. You reach an open door, and as you look inside, your vision darkens. You fall to the ground, and your thoughts start to slip away.")
                            print(Fore.RED + Style.BRIGHT + "Subject \"" + name + "\" has gone into a restricted area. I've stopped the program. We'll try this again later.")
                            print(Fore.YELLOW + Style.BRIGHT + "ENDING 3")
                            sys.exit()

                        elif choice == "go right":
                            print(Fore.WHITE + Style.NORMAL + "You take a right turn. The lights brighten and a red door is revealed at the end of the hall.")
                            print(Fore.RED + Style.BRIGHT + "I would normally stop the program here, but something's different this time... you may proceed.")
                            print(Fore.BLUE + Style.NORMAL + "Would you like to go through the door?")

                            while True:
                                print(Fore.BLUE + Style.NORMAL + "Yes\nNo")
                                choice = input(" > ").strip().lower()

                                if choice == "yes":
                                    print(Fore.WHITE + Style.NORMAL + "You enter the door and see a man sitting down at a desk. He looks at you with intrigue.")
                                    print(Fore.RED + Style.NORMAL + "Hello, " + name + ".")
                                    print(Fore.YELLOW + Style.BRIGHT + "ENDING 4")
                                    sys.exit()

                                elif choice == "no":
                                    print(Fore.WHITE + Style.NORMAL + "You decide not to enter the door.")
                                    print(Fore.RED + Style.BRIGHT + "A shame. I thought we had finally succeeded. Terminate the program.")
                                    print(Fore.YELLOW + Style.BRIGHT + "ENDING 5")
                                    sys.exit()

                                else:
                                    print(Fore.RED + Style.BRIGHT + "You're thinking hard about this, aren't you. It's alright. Take your time.")

                        elif choice == "return":
                            print(Fore.WHITE + Style.NORMAL + "You turn back towards the room you were in.")
                            print(Fore.RED + Style.BRIGHT + "Thank you, " + name + ". Now let us continue our testing.")
                            go_down_hall = False  # Exit the 'go down hall' loop to return to main room
                            break  # Break the fork loop

                        else:
                            print(Fore.RED + Style.BRIGHT + "That action is not valid.")

            elif choice == "no":
                print(Fore.WHITE + Style.NORMAL + "You head back to the room.")
                break

    elif choice == "enter right room":
        print(Fore.WHITE + Style.NORMAL + "The door is locked.")

    else:
        print(Fore.RED + Style.BRIGHT + "An interesting choice to say the least, but not one that can be fulfilled. Try again, " + name + ".")