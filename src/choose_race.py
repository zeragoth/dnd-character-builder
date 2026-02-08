from char_values import PC
from source_books import choose_books


def choose_race():
    if len(PC.books) <= 0:
        choose_books()

    available_races = []
    for book in PC.books:
        available_races.extend(book.races)

    print('Choose a race for your character. [ie "elf" to choose Elf]')
    for race in available_races:
        print(f"- {race.name}")
    inp = str.lower(input())
    if inp == "exit":
        quit()
    for race in available_races:
        if str.lower(race.name) in inp:
            if len(race.subraces) > 0:
                print(f"Which type of {race.name}?")
                for sub in race.subraces:
                    print(f"- {sub().name}")
                inp = str.lower(input())
                for sub in race.subraces:
                    if str.lower(sub().name) in inp:
                        PC.race = sub()
                        return
                print(f"{inp} is not a valid subrace name.")
                choose_race()
            else:
                PC.race = race
                return
    print(f"{inp} is not a valid race name.")
    choose_race()
