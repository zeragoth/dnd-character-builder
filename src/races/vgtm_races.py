from char_values import PC, Race
from languages import languages
from weapons import martial_melee_weapons, martial_ranged_weapons


class Aasimar(Race):
    def __init__(self):
        super().__init__()
        self.name = "Aasimar"
        self.asi = [(5,2)]
        self.traits = ["Darkvision", "Celestial Resistance", "Healing Hands"]
        self.spells = ["Light*"]
        self.langs.append("Celestial")

class Protector_Aasimar(Aasimar):
    def __init__(self):
        super().__init__()
        self.parent = Aasimar()
        self.name = "Protector Aasimar"
        self.asi.append((4,1))
        self.traits.append("Radiant Soul")

class Scourge_Aasimar(Aasimar):
    def __init__(self):
        super().__init__()
        self.parent = Aasimar()
        self.name = "Scourge Aasimar"
        self.asi.append((2,1))
        self.traits.append("Radiant Consumption")

class Fallen_Aasimar(Aasimar):
    def __init__(self):
        super().__init__()
        self.parent = Aasimar()
        self.name = "Fallen Aasimar"
        self.asi.append((0,1))
        self.traits.append("Necrotic Shroud")


class Firbolg(Race):
    def __init__(self):
        super().__init__()
        self.name = "Firbolg"
        self.asi = [(4,2),(0,1)]
        self.traits = ["Hidden Step", "Powerful Build", "Speech of Beast and Leaf"]
        self.spells = ["Detect Magic*", "Disguise Self*"]
        self.langs.extend(["Elvish", "Giant"])


class Kenku(Race):
    def __init__(self):
        super().__init__()
        self.name = "Kenku"
        self.asi = [(1,2),(4,1)]
        self.traits = ["Expert Forgery","Mimicry"]
        self.langs.append("Primordial (Auran)")

    def choices(self):
        counter = 0
        available_skills = ["Acrobatics", "Deception", "Stealth", "Sleight of Hand"]

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
                print(f"{inp} is not a valid skill name or is already known by your character.")


class Lizardfolk(Race):
    def __init__(self):
        super().__init__()
        self.name = "Lizardfolk"
        self.asi = [(2,2),(4,1)]
        self.speed["swim"] = 30
        self.traits = ["Bite", "Cunning Artisan", "Hold Breath", "Natural Armor", "Hungry Jaws"]
        self.langs.append("Draconic")

    def choices(self):
        counter = 0
        available_skills = ["Animal Handling", "Nature", "Perception", "Stealth", "Survival"]

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
                print(f"{inp} is not a valid skill name or is already known by your character.")


class Tabaxi(Race):
    def __init__(self):
        super().__init__()
        self.name = "Tabaxi"
        self.asi = [(1,2),(5,1)]
        self.speed["climb"] = 20
        self.traits = ["Darkvision", "Feline Agility", "Cat's Claws"]
        self.skill_profs = ["Perception", "Stealth"]

    def choices(self):
        print("Choose a language other than Common.")
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


class Triton(Race):
    def __init__(self):
        super().__init__()
        self.name = "Triton"
        self.asi = [(0,1),(2,1),(5,1)]
        self.speed["swim"] = 30
        self.traits = ["Amphibious", "Emissary of the Sea", "Guardians of the Depths"]
        self.spells = ["Fog Cloud*"]
        self.langs.append("Primordial (Aquan)")

    def check_lvl(self):
        if PC.lvl >= 3 and "Gust of Wind*" not in self.spells:
            self.spells.append("Gust of Wind*")
        if PC.lvl >= 5 and "Wall of Water*" not in self.spells:
            self.spells.append("Wall of Water*")


class Bugbear(Race):
    def __init__(self):
        super().__init__()
        self.name = "Bugbear"
        self.asi = [(0,2),(1,1)]
        self.traits = ["Darkvision", "Long-Limbed", "Powerful Build", "Surprise Attack"]
        self.skill_profs = ["Stealth"]
        self.langs.append("Goblin")


class Goblin(Race):
    def __init__(self):
        super().__init__()
        self.name = "Goblin"
        self.asi = [(1,2),(2,1)]
        self.size = "Small"
        self.traits = ["Darkvision", "Fury of the Small", "Nimble Escape"]
        self.langs.append("Goblin")


class Hobgoblin(Race):
    def __init__(self):
        super().__init__()
        self.name = "Hobgoblin"
        self.asi = [(2,2),(3,1)]
        self.traits = ["Darkvision", "Saving Face"]
        self.armor_profs = ["Light Armor"]
        self.langs.append("Goblin")

    def choices(self):
        counter = 0
        available_weapons = martial_melee_weapons + martial_ranged_weapons

        print("Choose 2 weapon proficiencies.")
        
        while counter < 2:
            for i in range(len(available_weapons)):
                if available_weapons[i-1] in self.weapon_profs or available_weapons[i-1] in PC.weapon_profs:
                    del available_weapons[i-1]
            for i in range(len(available_weapons)):
                print(f"[{i+1}] - {available_weapons[i]}")
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(available_weapons) and available_weapons[int(inp)-1] not in self.weapon_profs and available_weapons[int(inp)-1] not in PC.weapon_profs:
                self.weapon_profs.append(available_weapons[int(inp)-1])
                counter += 1
            else:
                print(f"{inp} is not a valid weapon name or your character is already proficient.")


class Kobold(Race):
    def __init__(self):
        super().__init__()
        self.name = "Kobold"
        self.asi = [(1,2),(0,-2)]
        self.size = "Small"
        self.traits = ["Darkvision", "Grovel, Cower, and Beg", "Pack Tactics", "Sunlight Sensitivity"]
        self.langs.append("Draconic")


class Orc(Race):
    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.asi = [(0,2),(2,1)]
        self.traits = ["Darkvision", "Aggressive", "Powerful Build"]
        self.langs.append("Orc")

    def choices(self):
        available_skills = ["Animal Handling", "Insight", "Intimidation", "Medicine", "Nature", "Perception","Survival"]

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
                return
            else:
                print(f"{inp} is not a valid skill name or is already known by your character.")


class Yuan_Ti_Pureblood(Race):
    def __init__(self):
        super().__init__()
        self.name = "Yuan-Ti Pureblood"
        self.asi = [(5,2),(3,1)]
        self.traits = ["Darkvision", "Magic Resistance", "Poison Immunity"]
        self.spells = ["Poison Spray*","Animal Friendship (snakes)*"]
        self.langs.extend(["Abyssal", "Draconic"])

    def check_lvl(self):
        if PC.lvl >= 3 and "Suggestion*" not in self.spells:
            self.spells.append("Suggestion*")
