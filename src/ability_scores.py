# Contains the function that is called when the user inputs "score" in the main menu.
# Allows the user to either input their own ability scores,
# or choose from a number of methods to randomly determine ability scores.

# WIP, needs option to roll for scores, then choose where to "place" the rolled scores.

import random

from char_values import PC


def input_scores():
    print("Do you have the Ability Scores for your character? [y/n]")
    inp = str.lower(input())
    if inp == "y" or inp == "yes":
        input_str()
        input_dex()
        input_con()
        input_int()
        input_wis()
        input_cha()
        print(f"Your Ability Scores are:\nSTR {PC.scores[0]}\nDEX {PC.scores[1]}\nCON {PC.scores[2]}\nINT {PC.scores[3]}\nWIS {PC.scores[4]}\nCHA {PC.scores[5]}")
        print(f"Is this correct? [y/n]")
        inp = str.lower(input())
        if inp == "y" or inp == "yes":
            return
        elif inp == "exit":
            quit()
        else:
            input_scores()
            return
    elif inp == "n" or inp == "no":
        roll_scores()
    elif inp == "exit":
        quit()


def input_str():
    print("What is your Strength score?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.scores[0] = inp
            return
        else:
            print("Please enter a number between 1 and 20.")
            input_str()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        input_str()

def input_dex():
    print("What is your Dexterity score?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.scores[1] = inp
            return
        else:
            print("Please enter a number between 1 and 20.")
            input_dex()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        input_dex()

def input_con():
    print("What is your Constitution score?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.scores[2] = inp
            return
        else:
            print("Please enter a number between 1 and 20.")
            input_con()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        input_con()

def input_int():
    print("What is your Intelligence score?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.scores[3] = inp
            return
        else:
            print("Please enter a number between 1 and 20.")
            input_int()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        input_int()

def input_wis():
    print("What is your Wisdom score?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.scores[4] = inp
            return
        else:
            print("Please enter a number between 1 and 20.")
            input_wis()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        input_wis()

def input_cha():
    print("What is your Charisma score?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.scores[5] = inp
            return
        else:
            print("Please enter a number between 1 and 20.")
            input_cha()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        input_cha()


def roll_scores():
    print("Would you like to randomize your ability scores? [y/n]")
    inp = str.lower(input())
    if inp == "y" or inp == "yes":
        print("Which method would you like to use?\n")
        print("[1] - 3d6\n[2] - 4d6 drop lowest\n[3] - 1d20\n[4] - 2d20 drop lowest")
        inp = str.lower(input())
        if inp == "1":
            for i in range(6):
                result = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
                PC.scores[i] = result
            return
        if inp == "2":
            for i in range(6):
                roll = []
                roll.append(random.randint(1,6))
                roll.append(random.randint(1,6))
                roll.append(random.randint(1,6))
                roll.append(random.randint(1,6))
                roll.sort()
                del roll[0]
                result = roll[0] + roll[1] + roll[2]
                PC.scores[i] = result
            return
        if inp == "3":
            for i in range(6):
                roll = random.randint(1,20)
                PC.scores[i] = roll
            return
        if inp == "4":
            for i in range(6):
                roll = []
                roll.append(random.randint(1,20))
                roll.append(random.randint(1,20))
                roll.sort()
                del roll[0]
                result = roll[0]
                PC.scores[i] = result
            return
        elif inp == "exit":
            quit()
        else:
            print("Please enter a number [1-4]")
            roll_scores()
    elif inp == "n" or inp == "no":
        input_scores()
        return
    elif inp == "exit":
        quit()
    else:
        roll_scores()
