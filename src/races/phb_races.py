from char_values import PC, Race
from languages import languages

class Dwarf(Race):
    name = "Dwarf"
    asi = [(2,2)]
    size = "Medium"
    speed = "25"
    weapon_profs = ["battleaxe","handaxe","light hammer","warhammer"]
    tool_profs = ["CHOICE"]
    traits = ["Darkvision","Dwarven Resilience","Stonecunning"]
    langs = ["Common","Dwarvish"]
    subraces = []

class Hill_Dwarf(Dwarf):
    parent = Dwarf
    asi = [(2,2),(4,1)]
    traits = ["Darkvision","Dwarven Resilience","Stonecunning","Dwarven Toughness"]
    name = "Hill Dwarf"
        
class Mountain_Dwarf(Dwarf):
    parent = Dwarf
    asi = [(2,2),(0,1)]
    armor_profs = ["light armor","medium armor"]
    name = "Mountain Dwarf"


class Elf(Race):
    name = "Elf"
    asi = [(1,2)]
    size = "Medium"
    speed = "30"
    traits = ["Darkvision","Fey Ancestry","Trance"]
    skill_profs = ["Perception"]
    langs = ["Common","Elvish"]
    subraces = []

class High_Elf(Elf):
    parent = Elf
    name = "High Elf"
    asi = [(1,2),(3,1)]
    weapon_profs = ["longsword","shortsword","shortbow","longbow"]
    spells = []
    langs = ["Common","Elvish"]

    def choices():
        while True:
            print("Choose a cantrip from the Wizard spell list.")
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp not in PC.spells:
                PC.race.spells.append(inp)
                break
            else:
                print(f"{inp} is not a valid cantrip name or is already known by your character.")

        while True:
            print("Choose a language other than Common or Elvish (Case sensitive).")
            inp = input()
            if inp == "exit":
                quit()
            if inp in languages and inp not in PC.langs:
                PC.race.langs.append(inp)
                return
            else:
                print(f"{inp} is not a valid language name or is already known by your character.")

class Wood_Elf(Elf):
    parent = Elf
    name = "Wood Elf"
    asi = [(1,2),(4,1)]
    weapon_profs = ["longsword","shortsword","shortbow","longbow"]
    speed = "35"
    traits = ["Darkvision","Fey Ancestry","Trance","Mask of the Wild"]

class Drow(Elf):
    parent = Elf
    name = "Drow"
    asi = [(1,2),(5,1)]
    traits = ["Darkvision","Fey Ancestry","Trance","Sunlight Sensitivity"]
    spells = ["Dancing Lights"]
    weapon_profs = ["rapier","shortsword","hand crossbow"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Faerie Fire")
        if PC.lvl >= 5:
            self.spells.append("Darkness")


class Halfling(Race):
    name = "Halfling"
    asi = [(1,2)]
    size = "Small"
    speed = "25"
    traits = ["Lucky","Brave","Halfling Nimbleness"]
    langs = ["Common","Halfling"]
    subraces = []

class Lightfoot_Halfling(Halfling):
    parent = Halfling
    name = "Lightfoot Halfling"
    asi = [(1,2),(5,1)]
    traits = ["Lucky","Brave","Halfling Nimbleness","Naturally Stealthy"]

class Stout_Halfling(Halfling):
    parent = Halfling
    name = "Stout Halfling"
    asi = [(1,2),(2,1)]
    traits = ["Lucky","Brave","Halfling Nimbleness","Stout Resilience"]



class Human(Race):
    name = "Human"
    asi = [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1)]
    size = "Medium"
    speed = "30"
    langs = ["Common","CHOICE"]

class Human_Variant(Race):
    name = "Human (Variant)"
    asi = [["CHOICE",1],["CHOICE",1]]
    size = "Medium"
    speed = "30"
    langs = ["Common","CHOICE"]
    skill_profs = ["CHOICE"]
    feats = ["CHOICE"]


class Dragonborn(Race):
    name = "Dragonborn"
    asi = [(0,2),(5,1)]
    size = "Medium"
    speed = "30"
    traits = ["Draconic Ancestry","Breath Weapon","Damage Resistance"]
    langs = ["Common","Draconic"]


class Gnome(Race):
    name = "Gnome"
    asi = [(3,2)]
    size = "Small"
    speed = "25"
    traits = ["Darkvision","Gnome Cunning"]
    langs = ["Common","Gnomish"]
    subraces = []

class Forest_Gnome(Gnome):
    parent = Gnome
    name = "Forest Gnome"
    asi = [(3,2),(1,1)]
    spells = ["Minor Illusion"]
    traits = ["Darkvision","Gnome Cunning","Speak with Small Beasts"]

class Rock_Gnome(Gnome):
    parent = Gnome
    name = "Rock Gnome"
    asi = [(3,2),(2,1)]
    traits = ["Darkvision","Gnome Cunning","Artificer's Lore","Tinker"]



class Half_Elf(Race):
    name = "Half-Elf"
    asi = [(5,2),["CHOICE",1],["CHOICE",1]]
    size = "Medium"
    speed = "30"
    traits = ["Darkvision","Fey Ancestry"]
    skill_profs = ["CHOICE1","CHOICE2"]
    langs = ["Common","Elvish","CHOICE"]


class Half_Orc(Race):
    name = "Half-Orc"
    asi = [(0,2),(2,1)]
    size = "Medium"
    speed = "30"
    traits = ["Darkvision","Relentless Endurance","Savage Attacks"]
    skill_profs = ["Intimidation"]
    langs = ["Common","Orc"]


class Tiefling(Race):
    name = "Tiefling"
    asi = [(3,1),(5,2)]
    size = "Medium"
    speed = "30"
    traits = ["Darkvision","Hellish Resistance"]
    spells = ["Thaumaturgy"]
    langs = ["Common","Infernal"]

    def check_lvl():
        if PC.lvl >= 3:
            if "Hellish Rebuke" not in PC.race.spells:
                PC.race.spells.append("Hellish Rebuke")
        if PC.lvl >= 5:
            if "Darkness" not in PC.race.spells:
                PC.race.spells.append("Darkness")
