import sys

from char_values import Character
from functions import char_level, input_scores, PC

def main():
    print('Welcome to the D&D Character builder.  Type "exit" at any time to close the program.')
    char_level()
    input_scores()
    while True:
        print(f"Name: {PC.name} ----- Class & Level: {PC.job} {PC.lvl}")
        print(f"Race: {PC.race} ----- Background: {PC.bground}")
        print(f"STR {PC.scores[0]}\nDEX {PC.scores[1]}\nCON {PC.scores[2]}\nINT {PC.scores[3]}\nWIS {PC.scores[4]}\nCHA {PC.scores[5]}")
        print(f"Proficiencies: {PC.profs} ----- Languages: {PC.langs}")
        print(f"Feats: {PC.feats} ----- Spells: {PC.spells}")
        print('Type "commands" to see available commands')
        inp = str.lower(input())
        if "commands" in inp:
            print('Available commands:\n"lvl" or "level" - Change your character level')
            print('"ability scores" or "scores" - Change your Ability Scores')
            print('"exit" - exits the program')
        if "lvl" in inp or "level" in inp:
            char_level()
        if "abilit" in inp or "score" in inp:
            input_scores()
        if inp == "exit":
            quit()

main()