from char_values import PC, Race
from languages import languages


class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Dwarf"
        self.asi = [(2,2)]
        self.size = "Medium"
        self.speed = "25"
        self.weapon_profs = ["battleaxe","handaxe","light hammer","warhammer"]
        self.tool_profs = ["CHOICE"]
        self.traits = ["Darkvision","Dwarven Resilience","Stonecunning"]
        self.langs = ["Common","Dwarvish"]
        self.subraces = []

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
        self.size = "Medium"
        self.speed = "30"
        self.traits = ["Darkvision","Fey Ancestry","Trance"]
        self.skill_profs = ["Perception"]
        self.langs = ["Common","Elvish"]

class High_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "High Elf"
        self.asi.append((3,1))
        self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]

    def choices(self):
        while True:
            print("Choose a cantrip from the Wizard spell list.")
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp not in self.spells:
                self.spells.append(inp)
                break
            else:
                print(f"{inp} is not a valid cantrip name or is already known by your character.")

        while True:
            print("Choose a language other than Common or Elvish (Case sensitive).")
            inp = input()
            if inp == "exit":
                quit()
            if inp in languages and inp not in self.langs:
                self.langs.append(inp)
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
        self.speed = "35"
        self.traits.append("Mask of the Wild")

class Drow(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "Drow"
        self.asi.append((5,1))
        self.traits.append("Sunlight Sensitivity")
        self.spells = ["Dancing Lights"]
        self.weapon_profs = ["rapier","shortsword","hand crossbow"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Faerie Fire")
        if PC.lvl >= 5:
            self.spells.append("Darkness")


class Halfling(Race):
    def __init__(self):
        super().__init__()
        self.name = "Halfling"
        self.asi = [(1,2)]
        self.size = "Small"
        self.speed = "25"
        self.traits = ["Lucky","Brave","Halfling Nimbleness"]
        self.langs = ["Common","Halfling"]
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
        self.size = "Medium"
        self.speed = "30"
        self.langs = ["Common","CHOICE"]

class Human_Variant(Race):
    def __init__(self):
        super().__init__()
        self.name = "Human (Variant)"
        self.asi = [["CHOICE",1],["CHOICE",1]]
        self.size = "Medium"
        self.speed = "30"
        self.langs = ["Common","CHOICE"]
        self.skill_profs = ["CHOICE"]
        self.feats = ["CHOICE"]


class Dragonborn(Race):
    def __init__(self):
        super().__init__()
        self.name = "Dragonborn"
        self.asi = [(0,2),(5,1)]
        self.size = "Medium"
        self.speed = "30"
        self.traits = ["Draconic Ancestry","Breath Weapon","Damage Resistance"]
        self.langs = ["Common","Draconic"]


class Gnome(Race):
    def __init__(self):
        super().__init__()
        self.name = "Gnome"
        self.asi = [(3,2)]
        self.size = "Small"
        self.speed = "25"
        self.traits = ["Darkvision","Gnome Cunning"]
        self.langs = ["Common","Gnomish"]

class Forest_Gnome(Gnome):
    def __init__(self):
        super().__init__()
        self.parent = Gnome()
        self.name = "Forest Gnome"
        self.asi.append((1,1))
        self.spells = ["Minor Illusion"]
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
        self.size = "Medium"
        self.speed = "30"
        self.traits = ["Darkvision","Fey Ancestry"]
        self.skill_profs = ["CHOICE1","CHOICE2"]
        self.langs = ["Common","Elvish","CHOICE"]


class Half_Orc(Race):
    def __init__(self):
        super().__init__()
        self.name = "Half-Orc"
        self.asi = [(0,2),(2,1)]
        self.size = "Medium"
        self.speed = "30"
        self.traits = ["Darkvision","Relentless Endurance","Savage Attacks"]
        self.skill_profs = ["Intimidation"]
        self.langs = ["Common","Orc"]


class Tiefling(Race):
    def __init__(self):
        super().__init__()
        self.name = "Tiefling"
        self.asi = [(3,1),(5,2)]
        self.size = "Medium"
        self.speed = "30"
        self.traits = ["Darkvision","Hellish Resistance"]
        self.spells = ["Thaumaturgy"]
        self.langs = ["Common","Infernal"]

    def check_lvl(self):
        if PC.lvl >= 3:
            if "Hellish Rebuke" not in self.spells:
                self.spells.append("Hellish Rebuke")
        if PC.lvl >= 5:
            if "Darkness" not in self.spells:
                self.spells.append("Darkness")
