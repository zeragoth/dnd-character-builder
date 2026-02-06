from char_values import PC
from level import input_level
from ability_scores import input_scores


def menu():
    while True:
        print(f"\nName: {PC.name} ----- Class & Level: {PC.job} {PC.lvl}")
        print(f"Race: {PC.race} ----- Background: {PC.bground}")
        print(f"STR {PC.scores[0]}\nDEX {PC.scores[1]}\nCON {PC.scores[2]}\nINT {PC.scores[3]}\nWIS {PC.scores[4]}\nCHA {PC.scores[5]}")
        print(f"Proficiencies: {PC.profs} ----- Languages: {PC.langs}")
        print(f"Feats: {PC.feats} ----- Spells: {PC.spells}\n")
        print('Type "commands" to see available commands')
        inp = str.lower(input())
        if "commands" in inp:
            print('\nAvailable commands:\n"lvl" or "level" - Change your character level')
            print('"ability scores" or "scores" - Change your Ability Scores')
            print('"exit" - exits the program')
        elif "lvl" in inp or "level" in inp:
            input_level()
        elif "abilit" in inp or "score" in inp:
            input_scores()
        elif inp == "exit":
            quit()