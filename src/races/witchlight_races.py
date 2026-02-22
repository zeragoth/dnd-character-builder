from char_values import PC, Race
from languages import languages


class Fairy(Race):
    def __init__(self):
        super().__init__()
        self.name = "Fairy"
        self.asi = [["CHOICE",2],["CHOICE",1]]
        self.size = "Small"
        self.traits = ["Fey"]
        self.speed["fly"] = self.speed["walk"]
        self.spells[0] = ["Druidcraft*"]

    def choices(self):
        self.langs = ["Common"]

        print("\nChoose a language other than Common.")
        for i in range(len(languages)):
            print(f"[{i+1}] - {languages[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs:
                self.langs.append(languages[int(inp)-1])
                return
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[1] = "Faerie Fire*"
        if PC.lvl >= 5:
            self.spells[2] = "Enlarge/Reduce*"


class Harengon(Race):
    def __init__(self):
        super().__init__()
        self.name = "Harengon"
        self.asi = [["CHOICE",2],["CHOICE",1]]
        self.traits = ["Hare Trigger", "Lucky Footwork", "Rabbit Hop"]
        self.skill_profs = ["Perception"]

    def choices(self):
        print("\nChoose a size.")
        print("[1] - Medium\n[2] - Small")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if "1" in inp:
                self.size = ["Medium"]
                break
            elif "2" in inp:
                self.size = ["Small"]
                break
            else:
                print(f"{inp} is not a valid size.")

        self.langs = ["Common"]

        print("\nChoose a language other than Common.")
        for i in range(len(languages)):
            print(f"[{i+1}] - {languages[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs:
                self.langs.append(languages[int(inp)-1])
                return
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")