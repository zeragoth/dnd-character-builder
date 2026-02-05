import sys

from char_values import Character

PC = Character()

def char_level():
    print("What level is your character?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.lvl = inp
            print(f"Your character is level {PC.lvl}.")
            return
        else:
            print("Please enter a number between 1 and 20.")
            char_level()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        char_level()

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
    elif inp == "n" or inp == "no":
        roll_scores()
    elif inp == "exit":
        quit()


def roll_scores():
    print("Would you like to randomize your ability scores? [y/n]")
    inp = str.lower(input())
    if inp == "y" or inp == "yes":
        pass
    elif inp == "n" or inp == "no":
        input_scores()
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
