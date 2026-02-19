from char_values import PC
from level import input_level
from ability_scores import input_scores
from source_books import choose_books, get_book_titles
from choose_race import choose_race
from spells import spellbook


def menu():
    while True:
        skills = PC.skill_profs.copy()
        for i in range(len(PC.race.skill_profs)):
            if PC.race.skill_profs[i] not in PC.skill_profs:
                skills.append(PC.race.skill_profs[i])

        feats = PC.feats.copy()
        for i in range(len(PC.race.feats)):
            if PC.race.feats[i] not in PC.feats:
                feats.append(PC.race.feats[i])

        armors = PC.armor_profs.copy()
        for i in range(len(PC.race.armor_profs)):
            if PC.race.armor_profs[i] not in PC.armor_profs:
                armors.append(PC.race.armor_profs[i])

        weapons = PC.weapon_profs.copy()
        for i in range(len(PC.race.weapon_profs)):
            if PC.race.weapon_profs[i] not in PC.weapon_profs:
                weapons.append(PC.race.weapon_profs[i])

        tools = PC.tool_profs.copy()
        for i in range(len(PC.race.tool_profs)):
            if PC.race.tool_profs[i] not in PC.tool_profs:
                tools.append(PC.race.tool_profs[i])

        langs = PC.langs.copy()
        for i in range(len(PC.race.langs)):
            if PC.race.langs[i] not in PC.langs:
                langs.append(PC.race.langs[i])

        print(f"\nName: {PC.name} ----- Class & Level: {PC.job} {PC.lvl}")
        print(f"Race: {PC.race.name} ----- Background: {PC.bground}")
        print(f"Speed: {PC.race.speed} ----- Size: {PC.race.size}")
        print(f"STR {PC.scores[0]+PC.racial_scores[0]}\nDEX {PC.scores[1]+PC.racial_scores[1]}\nCON {PC.scores[2]+PC.racial_scores[2]}\nINT {PC.scores[3]+PC.racial_scores[3]}\nWIS {PC.scores[4]+PC.racial_scores[4]}\nCHA {PC.scores[5]+PC.racial_scores[5]}")
        print(f"Skills: {skills}")
        print(f"Armor Proficiencies: {armors} ----- Weapon Proficiencies: {weapons}")
        print(f"Tool Proficiencies: {tools} ----- Languages: {langs}")
        print(f"Feats: {feats}")
        print(f"Traits: {PC.race.traits}")
        print(f"Source Books: {get_book_titles()}")
        print('\nType "commands" to see available commands')
        inp = str.lower(input())
        if "commands" in inp:
            print("\nAvailable commands:\n[lvl] or [level] - Change your character level")
            print("[ability scores] or [scores] - Change your Ability Scores")
            print("[books] - Change the available source book(s)")
            print("[race] - Change your character's race")
            print("[spellbook] or [spells] - Shows a list of Known Spells")
            print("[exit] - Exits the program")
        elif "lvl" in inp or "level" in inp:
            input_level()
        elif "abilit" in inp or "score" in inp:
            input_scores()
        elif "book" in inp:
            choose_books()
        elif "race" in inp:
            choose_race()
        elif "spell" in inp:
            spellbook()
        elif inp == "exit":
            quit()