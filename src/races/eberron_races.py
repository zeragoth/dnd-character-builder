from char_values import PC, Race
from languages import languages
from skills import skills
from tools import tools, artisan_tools
from races.phb_races import Half_Elf, Human, Half_Orc, Halfling, Gnome, Elf, Dwarf


class Changeling(Race):
    def __init__(self):
        super().__init__()
        self.name = "Changeling"
        self.asi = [(5,2),("CHOICE",1)]
        self.traits = ["Shapechanger"]

    def choices(self):
        counter = 0
        available_skills = ["Deception", "Insight", "Intimidation", "Persuasion"]
        self.skill_profs = []

        print("Choose 2 skill proficiencies.")
        
        while counter < 2:
            for i in range(len(available_skills)):
                if available_skills[i-1] in self.skill_profs or available_skills[i-1] in PC.skill_profs:
                    del available_skills[i-1]
            for i in range(len(available_skills)):
                print(f"[{i+1}] - {available_skills[i]}")
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(available_skills) and available_skills[int(inp)-1] not in self.skill_profs and available_skills[int(inp)-1] not in PC.skill_profs:
                self.skill_profs.append(available_skills[int(inp)-1])
                counter += 1
            else:
                print(f"{inp} is not a valid skill name or your character is already proficient.")

        counter = 0
        self.langs = ["Common"]

        print("Choose 2 languages other than Common.")

        while counter < 2:
            for i in range(len(languages)):
                if languages[i-1] in self.langs or languages[i-1] in PC.langs:
                    del languages[i-1]
            for i in range(len(languages)):
                print(f"[{i+1}] - {languages[i]}")
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs and languages[int(inp)-1] not in PC.langs:
                self.langs.append(languages[int(inp)-1])
                counter += 1
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")


class Kalashtar(Race):
    def __init__(self):
        super().__init__()
        self.name = "Kalashtar"
        self.asi = [(4,2),(5,1)]
        self.traits = ["Dual Mind", "Mental Discipline", "Mind Link", "Severed from Dreams"]
        self.langs.append("Quori")

    def choices(self):
        self.langs - ["Common", "Quori"]

        for i in range(len(languages)):
            print(f"[{i+1}] - {languages[i]}")
        print("Choose a language other than Common or Quori.")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs and languages[int(inp)-1] not in PC.langs:
                self.langs.append(languages[int(inp)-1])
                return
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")


class Shifter(Race):
    def __init__(self):
        super().__init__()
        self.name = "Shifter"
        self.traits = ["Darkvision", "Shifting"]

class Beasthide_Shifter(Shifter):
    def __init__(self):
        super().__init__()
        self.parent = Shifter()
        self.name = "Beasthide Shifter"
        self.asi = [(2,2),(0,1)]
        self.skill_profs.append("Athletics")

class Longtooth_Shifter(Shifter):
    def __init__(self):
        super().__init__()
        self.parent = Shifter()
        self.name = "Longtooth Shifter"
        self.asi = [(0,2),(1,1)]
        self.skill_profs.append("Intimidation")

class Swiftstride_Shifter(Shifter):
    def __init__(self):
        super().__init__()
        self.parent = Shifter()
        self.name = "Swiftstride Shifter"
        self.asi = [(1,2),(5,1)]
        self.skill_profs.append("Acrobatics")

class Wildhunt_Shifter(Shifter):
    def __init__(self):
        super().__init__()
        self.parent = Shifter()
        self.name = "Wildhunt Shifter"
        self.asi = [(4,2),(1,1)]
        self.skill_profs.append("Survival")


class Warforged(Race):
    def __init__(self):
        super().__init__()
        self.name = "Warforged"
        self.asi = [(2,2),("CHOICE",1)]
        self.traits = ["Constructed Resilience", "Sentry's Rest", "Integrated Protection"]

    def choices(self):
        available_skills = skills.copy()
        self.skill_profs = []

        print("Choose a skill proficiency.")
        for i in range(len(available_skills)):
                if available_skills[i-1] in self.skill_profs or available_skills[i-1] in PC.skill_profs:
                    del available_skills[i-1]
        for i in range(len(available_skills)):
            print(f"[{i+1}] - {available_skills[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(available_skills) and available_skills[int(inp)-1] not in self.skill_profs and available_skills[int(inp)-1] not in PC.skill_profs:
                self.skill_profs.append(available_skills[int(inp)-1])
                break
            else:
                print(f"{inp} is not a valid skill name or your character is already proficient.")

        available_tools = tools.copy()
        self.tool_profs = []

        print("Choose a tool proficiency.")
        for i in range(len(available_tools)):
                if available_tools[i-1] in self.tool_profs or available_tools[i-1] in PC.tool_profs:
                    del available_tools[i-1]
        for i in range(len(available_tools)):
            print(f"[{i+1}] - {available_tools[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(available_tools) and available_tools[int(inp)-1] not in self.tool_profs and available_tools[int(inp)-1] not in PC.tool_profs:
                self.tool_profs.append(available_tools[int(inp)-1])
                break
            else:
                print(f"{inp} is not a valid tool name or your character is already proficient.")

        self.langs = ["Common"]

        print("Choose a language other than Common.")
        for i in range(len(languages)):
            print(f"[{i+1}] - {languages[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs and languages[int(inp)-1] not in PC.langs:
                self.langs.append(languages[int(inp)-1])
                return
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")

class Mark_of_Detection(Half_Elf):
    def __init__(self):
        super().__init__()
        self.parent = Half_Elf()
        self.name = "Half-Elf (Mark of Detection)"
        self.asi = [(4,2),("CHOICE",1)]
        self.traits.extend(["Deductive Intuition", "Spells of the Mark"])
        self.spells[1] = ["Detect Magic*", "Detect Poison and Disease*"]

    def choices(self):
        self.langs = ["Common", "Elvish"]

        while True:
            print("Choose a language other than Common or Elvish.")
            for i in range(len(languages)):
                print(f"[{i+1}] - {languages[i]}")
            while True:
                inp = str.lower(input())
                if inp == "exit":
                    quit()
                if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs and languages[int(inp)-1] not in PC.langs:
                    self.langs.append(languages[int(inp)-1])
                    return
                else:
                    print(f"{inp} is not a valid language name or is already known by your character.")

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Invisibility*"]

class Mark_of_Finding_A(Half_Orc):
    def __init__(self):
        super().__init__()
        self.parent = Half_Orc()
        self.name = "Half-Orc (Mark of Finding)"
        self.asi = [(4,2),(2,1)]
        self.traits = ["Darkvision", "Hunter's Intuition", "Spells of the Mark"]
        self.spells[1] = ["Hunter's Mark*"]
        self.langs = ["Common", "Goblin"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Locate Object*"]

class Mark_of_Finding_B(Human):
    def __init__(self):
        super().__init__()
        self.parent = Human()
        self.name = "Human (Mark of Finding)"
        self.asi = [(4,2),(2,1)]
        self.traits = ["Darkvision", "Hunter's Intuition", "Spells of the Mark"]
        self.spells[1] = ["Hunter's Mark*"]
        self.langs = ["Common", "Goblin"]

    def choices(self):
        pass

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Locate Object*"]

class Mark_of_Handling(Human):
    def __init__(self):
        super().__init__()
        self.parent = Human()
        self.name = "Human (Mark of Handling)"
        self.asi = [(4,2),("CHOICE",1)]
        self.traits.extend(["Wild Intuition", "The Bigger They Are", "Spells of the Mark"])
        self.spells[1] = ["Animal Friendship*", "Speak with Animals*"]

class Mark_of_Healing(Halfling):
    def __init__(self):
        super().__init__()
        self.parent = Halfling()
        self.name = "Halfling (Mark of Healing)"
        self.asi.append((4,1))
        self.traits.extend(["Medical Intuition", "Spells of the Mark"])
        self.spells[1] = ["Cure Wounds*"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Lesser Restoration*"]

class Mark_of_Hospitality(Halfling):
    def __init__(self):
        super().__init__()
        self.parent = Halfling()
        self.name = "Halfling (Mark of Hospitality)"
        self.asi.append((5,1))
        self.traits.extend(["Ever Hospitable", "Spells of the Mark"])
        self.spells[0] = ["Prestidigitation*"]
        self.spells[1] = ["Purify Food and Drink*", "Unseen Servant*"]

class Mark_of_Making(Human):
    def __init__(self):
        super().__init__()
        self.parent = Human()
        self.name = "Human (Mark of Making)"
        self.asi = [(3,2),("CHOICE",1)]
        self.traits = ["Artisan's Intuition", "Spells of the Mark"]
        self.spells[0] = ["Mending*"]
        self.spells[2] = ["Magic Weapon*"]

    def choices(self):
        available_tools = artisan_tools.copy()
        self.tool_profs = []

        print("Choose a tool proficiency.")
        for i in range(len(available_tools)):
                if available_tools[i-1] in self.tool_profs or available_tools[i-1] in PC.tool_profs:
                    del available_tools[i-1]
        for i in range(len(available_tools)):
            print(f"[{i+1}] - {available_tools[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(available_tools) and available_tools[int(inp)-1] not in self.tool_profs and available_tools[int(inp)-1] not in PC.tool_profs:
                self.tool_profs.append(available_tools[int(inp)-1])
                break
            else:
                print(f"{inp} is not a valid tool name or your character is already proficient.")

        self.langs = ["Common"]

        print("Choose a language other than Common.")
        for i in range(len(languages)):
            print(f"[{i+1}] - {languages[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs and languages[int(inp)-1] not in PC.langs:
                self.langs.append(languages[int(inp)-1])
                return
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")

class Mark_of_Passage(Human):
    def __init__(self):
        super().__init__()
        self.parent = Human()
        self.name = "Human (Mark of Passage)"
        self.asi = [(1,2),("CHOICE",1)]
        self.speed["walk"] = 35
        self.traits.extend(["Intuitive Motion", "Spells of the Mark"])
        self.spells[2] = ["Misty Step*"]

class Mark_of_Scribing(Gnome):
    def __init__(self):
        super().__init__()
        self.parent = Gnome()
        self.name = "Gnome (Mark of Scribing)"
        self.asi.append((5,1))
        self.traits.extend(["Gifted Scribe", "Spells of the Mark"])
        self.spells[0] = ["Message*"]
        self.spells[1] = ["Comprehend Languages*"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Magic Mouth*"]

class Mark_of_Sentinel(Human):
    def __init__(self):
        super().__init__()
        self.parent = Human()
        self.name = "Human (Mark of Sentinel)"
        self.asi = [(2,2),(4,1)]
        self.traits.extend(["Sentinel's Intuition", "Vigilant Guardian", "Spells of the Mark"])
        self.spells[1] = ["Shield*"]

class Mark_of_Shadow(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "Elf (Mark of Shadow)"
        self.asi.append((5,1))
        self.traits.extend(["Cunning Intuition", "Spells of the Mark"])
        self.spells[0] = ["Minor Illusion*"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Invisibility*"]

class Mark_of_Storm(Half_Elf):
    def __init__(self):
        super().__init__()
        self.parent = Half_Elf()
        self.name = "Half-Elf (Mark of Storm)"
        self.asi = [(5,2),(1,1)]
        self.traits.extend(["Windwright's Intuition", "Storm's Boon", "Spells of the Mark"])
        self.spells[0] = ["Gust*"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = "Gust of Wind*"

class Mark_of_Warding(Dwarf):
    def __init__(self):
        super().__init__()
        self.parent = Dwarf()
        self.name = "Dwarf (Mark of Warding)"
        self.asi = [(4,2),(1,1)]
        self.traits.extend(["Warder's Intuition", "Spells of the Mark"])
        self.spells[1] = ["Alarm*", "Mage Armor*"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Arcane Lock*"]
