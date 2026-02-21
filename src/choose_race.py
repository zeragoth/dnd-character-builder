from char_values import PC, PCRace, Race
from source_books import choose_books


def choose_race():
    if len(PC.books) <= 0:
        choose_books()

    available_races = []

    for book in PC.books:
        for race in book.races:
            for arace in available_races:
                if race.name == arace.name:
                    break
            else:
                available_races.append(race)
    if len(available_races) <= 0:
        return

    PC.race = Race()

    while True:
        print('\nChoose a race for your character.')
        for i in range(len(available_races)):
            print(f"[{i+1}] - {available_races[i].name}")

        inp = str.lower(input())
        if inp == "exit":
            quit()

        for race in reversed(available_races):
            if str.lower(race.name) in inp:
                if len(race.subraces) > 0:
                    while True:
                        print(f"\nWhich type of {race.name}?")
                        for i in range(len(race.subraces)):
                            print(f"[{i+1}] - {race.subraces[i].name}")

                        inp = str.lower(input())
                        if inp == "exit":
                            quit()

                        for sub in race.subraces:
                            if str.lower(sub.name) in inp:
                                PCRace = sub
                                PC.race = PCRace
                                apply_race(PCRace)
                                return
                            
                        for i in range(len(race.subraces)):
                            if str(i+1) in inp:
                                PCRace = race.subraces[i]
                                PC.race = PCRace
                                apply_race(PCRace)
                                return
                        print(f"\n{inp} is not a valid subrace name.")
                else:
                    PCRace = race
                    PC.race = PCRace
                    apply_race(PCRace)
                    return
                
        if inp.isdigit() and 1 <= int(inp) <= len(available_races):
            race = available_races[int(inp)-1]
            if len(race.subraces) > 0:
                while True:
                    print(f"\nWhich type of {race.name}?")
                    for i in range(len(race.subraces)):
                        print(f"[{i+1}] - {race.subraces[i].name}")

                    inp = str.lower(input())
                    if inp == "exit":
                        quit()

                    for i in range(len(race.subraces)):
                        if str(i+1) in inp:
                            PCRace = race.subraces[i]
                            PC.race = PCRace
                            apply_race(PCRace)
                            return
                    print(f"\n{inp} is not a valid subrace name.")
            else:
                PCRace = race
                PC.race = PCRace
                apply_race(PCRace)
                return
        print(f"\n{inp} is not a valid race name.")


def apply_race(race):
    apply_race_asi(race)
    race.choices()
    race.check_lvl()


def apply_race_asi(race):
    score_list = [[0, "Strength"],[1, "Dexterity"],[2, "Constitution"],
                [3, "Intelligence"],[4, "Wisdom"],[5, "Charisma"]]
    PC.racial_scores = [0,0,0,0,0,0]
    
    # Need to implement contingencies for other races who can choose ASIs

    if race.name == "Half-Elf":
        del score_list[5]
    
    for i in range(len(race.asi)):
        if race.asi[i][0] != "CHOICE":
            PC.racial_scores[race.asi[i][0]] = race.asi[i][1]
            
        else:
            picked = False
            while picked == False:
                print(f"\nChoose an ability score to increase by {race.asi[i][1]}.")
                for j in range(len(score_list)):
                    print(f"[{j+1}] - {score_list[j][1]}")

                inp = str.lower(input())
                if inp == "exit":
                   quit()
                if len(score_list) <= 0:
                    print("Error: No available ability scores!")

                x = None
                if "1" in inp and len(score_list) >= 1:
                    x = score_list[0][0]
                    PC.racial_scores[x] = race.asi[i][1]
                    del score_list[0]
                    picked = True
                elif "2" in inp and len(score_list) >= 2:
                    x = score_list[1][0]
                    PC.racial_scores[x] = race.asi[i][1]
                    del score_list[1]
                    picked = True
                elif "3" in inp and len(score_list) >= 3:
                    x = score_list[2][0]
                    PC.racial_scores[x] = race.asi[i][1]
                    del score_list[2]
                    picked = True
                elif "4" in inp and len(score_list) >= 4:
                    x = score_list[3][0]
                    PC.racial_scores[x] = race.asi[i][1]
                    del score_list[3]
                    picked = True
                elif "5" in inp and len(score_list) >= 5:
                    x = score_list[4][0]
                    PC.racial_scores[x] = race.asi[i][1]
                    del score_list[4]
                    picked = True
                elif "6" in inp and len(score_list) >= 6:
                    x = score_list[5][0]
                    PC.racial_scores[x] = race.asi[i][1]
                    del score_list[5]
                    picked = True
                else:
                    print(f"{inp} is not a valid choice.")
