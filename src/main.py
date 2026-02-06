import sys

from char_values import PC
from level import input_level
from ability_scores import input_scores
from menu import menu


def main():
    print('Welcome to the D&D Character builder.  Type "exit" at any time to close the program.')
    print("Would you like to walk through the character creation process? [y/n]")
    inp = str.lower(input())
    if inp == "y" or inp == "yes":
        input_level()
        input_scores()
    elif inp == "n" or inp == "no":
        pass
    elif inp == "exit":
        quit()
    else:
        main()
    menu()
    

main()