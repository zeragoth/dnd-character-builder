from char_values import PC
from source_books import choose_books


def choose_race():
    if len(PC.books) <= 0:
        choose_books()

    available_races = []
    for book in PC.books:
        available_races.extend(book.races)
    if len(available_races) <= 0:
        return

    while True:
        as_list = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]

        print('Choose a race for your character. [ie "elf" to choose Elf]')
        for race in available_races:
            print(f"- {race.name}")
        inp = str.lower(input())
        if inp == "exit":
            quit()
        for race in reversed(available_races):
            if str.lower(race.name) in inp:
                if len(race.subraces) > 0:
                    while True:
                        print(f"Which type of {race.name}?")
                        for sub in race.subraces:
                            print(f"- {sub().name}")
                        inp = str.lower(input())
                        if inp == "exit":
                            quit()
                        for sub in race.subraces:
                            if str.lower(sub().name) in inp:
                                PC.race = sub()
                                for i in range(len(sub().asi)):
                                    if sub().asi[i][0] != "CHOICE":
                                        PC.scores[sub().asi[i][0]] += sub().asi[i][1]
                                    else:
                                         picked = False
                                         while picked == False:
                                            print(f"Choose an ability score to increase by {sub().asi[i][1]}.")
                                            print("[1] - Strength\n[2] - Dexterity\n[3] - Constitution\n[4] - Intelligence\n[5] - Wisdom\n[6] - Charisma")
                                            inp = str.lower(input())
                                            if inp == "exit":
                                               quit()
                                            if "1" in inp:
                                                PC.scores[0] += sub().asi[i][1]
                                                picked = True
                                            elif "2" in inp:
                                                PC.scores[1] += sub().asi[i][1]
                                                picked = True
                                            elif "3" in inp:
                                                PC.scores[2] += sub().asi[i][1]
                                                picked = True
                                            elif "4" in inp:
                                                PC.scores[3] += sub().asi[i][1]
                                                picked = True
                                            elif "5" in inp:
                                                PC.scores[4] += sub().asi[i][1]
                                                picked = True
                                            elif "6" in inp:
                                                PC.scores[5] += sub().asi[i][1]
                                                picked = True
                                            else:
                                                print(f"{inp} is not a valid choice.")
                                return
                        print(f"\n{inp} is not a valid subrace name.")
                else:
                    PC.race = race
                    for i in range(len(race.asi)):
                        if race.asi[i][0] != "CHOICE":
                            PC.scores[race.asi[i][0]] += race.asi[i][1]
                        else:
                            picked = False
                            while picked == False:
                                print(f"Choose an ability score to increase by {race.asi[i][1]}.")
                                print("[1] - Strength\n[2] - Dexterity\n[3] - Constitution\n[4] - Intelligence\n[5] - Wisdom\n[6] - Charisma")
                                inp = str.lower(input())
                                if inp == "exit":
                                   quit()
                                if "1" in inp:
                                    PC.scores[0] += race.asi[i][1]
                                    picked = True
                                elif "2" in inp:
                                    PC.scores[1] += race.asi[i][1]
                                    picked = True
                                elif "3" in inp:
                                    PC.scores[2] += race.asi[i][1]
                                    picked = True
                                elif "4" in inp:
                                    PC.scores[3] += race.asi[i][1]
                                    picked = True
                                elif "5" in inp:
                                    PC.scores[4] += race.asi[i][1]
                                    picked = True
                                elif "6" in inp:
                                    PC.scores[5] += race.asi[i][1]
                                    picked = True
                                else:
                                    print(f"{inp} is not a valid choice.")
                    return
        print(f"\n{inp} is not a valid race name.")
