from char_values import PC, Race
from tools import tools
from languages import languages


class Centaur(Race):
    def __init__(self):
        super().__init__()
        self.name = "Centaur"
        self.asi = [(0,2),(4,1)]
        self.speed["walk"] = 40
        self.traits = ["Charge", "Hooves", "Equine Build"]
        self.langs.append("Sylvan")

    def choices(self):
        available_skills = ["Animal Handling", "Medicine", "Nature", "Survival"]
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


class Loxodon(Race):
    def __init__(self):
        super().__init__()
        self.name = "Loxodon"
        self.asi = [(2,2),(4,1)]
        self.traits = ["Powerful Build", "Loxodon Serenity", "Natural Armor", "Trunk", "Keen Smell"]
        self.langs.append("Loxodon")


class Minotaur(Race):
    def __init__(self):
        super().__init__()
        self.name = "Minotaur"
        self.asi = [(0,2),(2,1)]
        self.traits = ["Horns", "Goring Rush", "Hammering Horns"]
        self.langs.append("Minotaur")

    def choices(self):
        available_skills = ["Intimidation", "Persuasion"]
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


class Simic(Race):
    def __init__(self):
        super().__init__()
        self.name = "Simic Hybrid"
        self.asi = [(2,2),["CHOICE",1]]

    def choices(self):
        available_langs = ["Elvish", "Vedalken"]
        self.langs = ["Common"]

        print("Choose a language.")
        for i in range(len(available_langs)):
                if available_langs[i-1] in self.langs or available_langs[i-1] in PC.langs:
                    del available_langs[i-1]
        for i in range(len(available_langs)):
            print(f"[{i+1}] - {available_langs[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(available_langs) and available_langs[int(inp)-1] not in self.langs and available_langs[int(inp)-1] not in PC.langs:
                self.langs.append(available_langs[int(inp)-1])
                break
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")


        self.available_enhancements = ["Manta Glide", "Nimble Climber", "Underwater Adaptation"]
        self.enhancements = []
        self.traits = ["Darkvision"]

        print("Choose an animal enhancement.")
        for i in range(len(self.available_enhancements)):
                if self.available_enhancements[i-1] in self.enhancements:
                    del self.available_enhancements[i-1]
        for i in range(len(self.available_enhancements)):
            print(f"[{i+1}] - {self.available_enhancements[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(self.available_enhancements) and self.available_enhancements[int(inp)-1] not in self.enhancements:
                self.enhancements.append(self.available_enhancements[int(inp)-1])
                self.traits.append(self.available_enhancements[int(inp)-1])
                break
            else:
                print(f"{inp} is not a valid enhancement or your character already has it.")

    def check_lvl(self):
        if PC.lvl >= 5:
            self.available_enhancements = ["Manta Glide", "Nimble Climber", "Underwater Adaptation", "Grappling Appendages", "Carapace", "Acid Spit"]

            print("Choose an animal enhancement.")
            for i in range(len(self.available_enhancements)):
                    if self.available_enhancements[i-1] in self.enhancements:
                        del self.available_enhancements[i-1]
            for i in range(len(self.available_enhancements)):
                print(f"[{i+1}] - {self.available_enhancements[i]}")
            while True:
                inp = str.lower(input())
                if inp == "exit":
                    quit()
                if inp.isdigit() and 1 <= int(inp) <= len(self.available_enhancements) and self.available_enhancements[int(inp)-1] not in self.enhancements:
                    self.enhancements.append(self.available_enhancements[int(inp)-1])
                    self.traits.append(self.available_enhancements[int(inp)-1])
                    return
                else:
                    print(f"{inp} is not a valid enhancement or your character already has it.")


class Vedalken(Race):
    def __init__(self):
        super().__init__()
        self.name = "Vedalken"
        self.asi = [(3,2),(4,1)]
        self.traits = ["Vedalken Dispassion", "Tireless Precision", "Partially Amphibious"]

    def choices(self):
        available_skills = ["Arcana", "History", "Investigation", "Medicine", "Performance", "Sleight of Hand"]
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

        
        self.langs = ["Common", "Vedalken"]

        print("\nChoose a language other than Common or Vedalken.")
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
    