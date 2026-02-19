from char_values import PC, Race
from languages import languages
from skills import skills
from spells import wizard_cantrips


class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Dwarf"
        self.asi = [(2,2)]
        self.speed["walk"] = 25
        self.weapon_profs = ["battleaxe","handaxe","light hammer","warhammer"]
        self.traits = ["Darkvision","Dwarven Resilience","Stonecunning"]
        self.langs.append("Dwarvish")
        self.subraces = []

    def choices(self):
        print("\nChoose a tool proficiency.")
        print("[1] - Smith's Tools\n[2] - Brewer's Supplies\n[3] - Mason's Tools")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if "1" in inp:
                self.tool_profs = ["Smith's Tools"]
                return
            elif "2" in inp:
                self.tool_profs = ["Brewer's Supplies"]
                return
            elif "3" in inp:
                self.tool_profs = ["Mason's Tools"]
                return
            else:
                print(f"{inp} is not a valid tool proficiency name.")

class Hill_Dwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.parent = Dwarf()
        self.asi.append((4,1))
        self.traits.append("Dwarven Toughness")
        self.name = "Hill Dwarf"
        
class Mountain_Dwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.parent = Dwarf()
        self.asi.append((0,1))
        self.armor_profs = ["light armor","medium armor"]
        self.name = "Mountain Dwarf"


class Elf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Elf"
        self.asi = [(1,2)]
        self.traits = ["Darkvision","Fey Ancestry","Trance"]
        self.skill_profs = ["Perception"]
        self.langs.append("Elvish")

class High_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "High Elf"
        self.asi.append((3,1))
        self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]

    def choices(self):
        print("\nChoose a cantrip from the Wizard spell list.")
        for i in range(len(wizard_cantrips)):
            print(f"[{i+1}] - {wizard_cantrips[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(wizard_cantrips) and wizard_cantrips[int(inp)-1] not in self.spells[0] and wizard_cantrips[int(inp)-1] not in PC.spells[0]:
                self.spells[0].append(wizard_cantrips[int(inp)-1])
                break
            else:
                print(f"{inp} is not a valid spell choice or is already known by your character.")

        print("\nChoose a language other than Common or Elvish.")
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

class Wood_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "Wood Elf"
        self.asi.append((4,1))
        self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
        self.speed["walk"] = 35
        self.traits.append("Mask of the Wild")

class Drow(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "Drow"
        self.asi.append((5,1))
        self.traits.append("Sunlight Sensitivity")
        self.spells = ["Dancing Lights*"]
        self.weapon_profs = ["rapier","shortsword","hand crossbow"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Faerie Fire*" not in self.spells[1]:
            self.spells[1].append("Faerie Fire*")
        if PC.lvl >= 5 and "Darkness*" not in self.spells[2]:
            self.spells[2].append("Darkness*")


class Halfling(Race):
    def __init__(self):
        super().__init__()
        self.name = "Halfling"
        self.asi = [(1,2)]
        self.size = "Small"
        self.speed["walk"] = 25
        self.traits = ["Lucky","Brave","Halfling Nimbleness"]
        self.langs.append("Halfling")
        self.subraces = []

class Lightfoot_Halfling(Halfling):
    def __init__(self):
        super().__init__()
        self.parent = Halfling()
        self.name = "Lightfoot Halfling"
        self.asi.append((5,1))
        self.traits.append("Naturally Stealthy")

class Stout_Halfling(Halfling):
    def __init__(self):
        super().__init__()
        self.parent = Halfling()
        self.name = "Stout Halfling"
        self.asi.append((2,1))
        self.traits.append("Stout Resilience")


class Human(Race):
    def __init__(self):
        super().__init__()
        self.name = "Human"
        self.asi = [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1)]

    def choices(self):
        print("\nChoose a language other than Common.")
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

class Default_Human(Human):
    def __init__(self):
        super().__init__()
        self.parent = Human()

class Human_Variant(Human):
    def __init__(self):
        super().__init__()
        self.parent = Human()
        self.name = "Human (Variant)"
        self.asi = [["CHOICE",1],["CHOICE",1]]

    def choices(self):
        print("\nChoose a skill proficiency.")
        for i in range(len(skills)):
            print(f"[{i+1}] - {skills[i]}")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(skills) and skills[int(inp)-1] not in self.skill_profs and skills[int(inp)-1] not in PC.skill_profs:
                self.skill_profs.append(skills[int(inp)-1])
                break
            else:
                print(f"{inp} is not a valid skill name or is already known by your character.")

        print("\nChoose a feat.")
        while True:
            inp = input()
            if str.lower(inp) == "exit":
                quit()
            if inp not in self.feats and inp not in PC.feats:
                self.feats.append(inp)
                break
            else:
                print(f"{inp} is not a valid feat name or is already known by your character.")

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


class Dragonborn(Race):
    def __init__(self):
        super().__init__()
        self.name = "Dragonborn"
        self.asi = [(0,2),(5,1)]
        self.traits = ["Draconic Ancestry","Breath Weapon","Damage Resistance"]
        self.langs.append("Draconic")

    def choices(self):
        print("\nChoose a draconic ancestry.")
        print("[1] - Black (Acid)\n[2] - Blue (Lightning)\n[3] - Brass (Fire)\n[4] - Bronze (Lightning)\n"
        "[5] - Copper (Acid)\n[6] - Gold (Fire)\n[7] - Green (Poison)\n[8] - Red (Fire)\n"
        "[9] - Silver (Cold)\n[10] - White (Cold)")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            elif "2" in inp:
                self.traits[0] = "Draconic Ancestry: Blue Dragon (Lightning)"
            elif "3" in inp:
                self.traits[0] = "Draconic Ancestry: Brass Dragon (Fire)"
            elif "4" in inp:
                self.traits[0] = "Draconic Ancestry: Bronze Dragon (Lightning)"
            elif "5" in inp:
                self.traits[0] = "Draconic Ancestry: Copper Dragon (Acid)"
            elif "6" in inp:
                self.traits[0] = "Draconic Ancestry: Gold Dragon (Fire)"
            elif "7" in inp:
                self.traits[0] = "Draconic Ancestry: Green Dragon (Poison)"
            elif "8" in inp:
                self.traits[0] = "Draconic Ancestry: Red Dragon (Fire)"
            elif "9" in inp:
                self.traits[0] = "Draconic Ancestry: Silver Dragon (Cold)"
            elif "10" in inp:
                self.traits[0] = "Draconic Ancestry: White Dragon (Cold)"
            elif "1" in inp:
                self.traits[0] = "Draconic Ancestry: Black Dragon (Acid)"
            else:
                print(f"{inp} is not a valid input.")
            return


class Gnome(Race):
    def __init__(self):
        super().__init__()
        self.name = "Gnome"
        self.asi = [(3,2)]
        self.size = "Small"
        self.speed["walk"] = 25
        self.traits = ["Darkvision","Gnome Cunning"]
        self.langs.append("Gnomish")

class Forest_Gnome(Gnome):
    def __init__(self):
        super().__init__()
        self.parent = Gnome()
        self.name = "Forest Gnome"
        self.asi.append((1,1))
        self.spells[0] = ["Minor Illusion*"]
        self.traits.append("Speak with Small Beasts")

class Rock_Gnome(Gnome):
    def __init__(self):
        super().__init__()
        self.parent = Gnome()
        self.name = "Rock Gnome"
        self.asi.append((2,1))
        self.traits.extend(["Artificer's Lore","Tinker"])


class Half_Elf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Half-Elf"
        self.asi = [(5,2),["CHOICE",1],["CHOICE",1]]
        self.traits = ["Darkvision","Fey Ancestry"]
        self.langs.append("Elvish")

    def choices(self):
        counter = 0
        available_skills = skills.copy()

        print("\nChoose 2 skill proficiencies.")
        
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

        while True:
            print("\nChoose a language other than Common or Elvish.")
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

class Default_Half_Elf(Half_Elf):
    def __init__(self):
        super().__init__()
        self.parent = Half_Elf()


class Half_Orc(Race):
    def __init__(self):
        super().__init__()
        self.name = "Half-Orc"
        self.asi = [(0,2),(2,1)]
        self.traits = ["Darkvision","Relentless Endurance","Savage Attacks"]
        self.skill_profs = ["Intimidation"]
        self.langs.append("Orc")


class Tiefling(Race):
    def __init__(self):
        super().__init__()
        self.name = "Tiefling"
        self.asi = [(3,1),(5,2)]
        self.traits = ["Darkvision","Hellish Resistance"]
        self.spells[0] = ["Thaumaturgy*"]
        self.langs.append("Infernal")

    def check_lvl(self):
        if PC.lvl >= 3 and "Hellish Rebuke*" not in self.spells[1]:
            self.spells[1].append("Hellish Rebuke*")
        if PC.lvl >= 5 and "Darkness*" not in self.spells[2]:
            self.spells[2].append("Darkness*")
