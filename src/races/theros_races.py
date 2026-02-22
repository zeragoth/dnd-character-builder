from char_values import PC, Race
from tools import musical_instruments


class Leonin(Race):
    def __init__(self):
        super().__init__()
        self.name = "Leonin"
        self.asi = [(2,2),(0,1)]
        self.speed["walk"] = 35
        self.traits = ["Darkvision", "Claws", "Daunting Roar"]
        self.langs.append("Leonin")

    def choices(self):
        available_skills = ["Athletics", "Intimidation", "Perception", "Survival"]
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
                print(f"{inp} is not a valid skill name oryour character is already proficient.")


class Satyr(Race):
    def __init__(self):
        super().__init__()
        self.name = "Satyr"
        self.asi = [(5,2),(1,1)]
        self.speed["walk"] = 35
        self.traits = ["Fey", "Ram", "Magic Resistance", "Mirthful Leaps"]
        self.skills = ["Performance", "Persuasion"]
        self.langs.append("Sylvan")

    def choices(self):
        available_tools = musical_instruments.copy()
        self.tool_profs = []

        print("Choose a musical instrument proficiency.")
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
                return
            else:
                print(f"{inp} is not a valid instrument name or your character is already proficient.")
