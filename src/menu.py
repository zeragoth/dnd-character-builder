from char_values import PC
from level import input_level
from ability_scores import input_scores
from source_books import choose_books, get_book_titles
from choose_race import choose_race


def menu():
    while True:
        print(f"\nName: {PC.name} ----- Class & Level: {PC.job} {PC.lvl}")
        print(f"Race: {PC.race.name} ----- Background: {PC.bground}")
        print(f"STR {PC.scores[0]+PC.racial_scores[0]}\nDEX {PC.scores[1]+PC.racial_scores[1]}\nCON {PC.scores[2]+PC.racial_scores[2]}\nINT {PC.scores[3]+PC.racial_scores[3]}\nWIS {PC.scores[4]+PC.racial_scores[4]}\nCHA {PC.scores[5]+PC.racial_scores[5]}")
        print(f"Proficiencies: {PC.armor_profs}\n{PC.weapon_profs}\n{PC.tool_profs}\n{PC.skill_profs} ----- Languages: {PC.langs}")
        print(f"Feats: {PC.feats} ----- Spells: {PC.spells}")
        print(f"Source Books: {get_book_titles()}")
        print('\nType "commands" to see available commands')
        inp = str.lower(input())
        if "commands" in inp:
            print("\nAvailable commands:\n[lvl] or [level] - Change your character level")
            print("[ability scores] or [scores] - Change your Ability Scores")
            print("[books] - Change the available source book(s)")
            print("[race] - Change your character's race")
            print("[exit] - Exits the program")
        elif "lvl" in inp or "level" in inp:
            input_level()
        elif "abilit" in inp or "score" in inp:
            input_scores()
        elif "book" in inp:
            choose_books()
        elif "race" in inp:
            choose_race()
        elif inp == "exit":
            quit()