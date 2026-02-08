from char_values import PC, Race


class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Dwarf"
        self.asi["CON"] = 2
        self.size = "Medium"
        self.speed = 25
        self.weapon_profs = ["battleaxe","handaxe","light hammer","warhammer"]
        self.tool_profs = ["CHOICE"]
        self.traits = ["Darkvision","Dwarven Resilience","Stonecunning"]
        self.langs = ["Common","Dwarvish"]
        self.subraces = [Hill_Dwarf, Mountain_Dwarf]


class Hill_Dwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.name = "Hill Dwarf"
        self.asi["WIS"] = 1
        self.traits.append("Dwarven Toughness")
        
class Mountain_Dwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.name = "Mountain Dwarf"
        self.asi["STR"] = 1
        self.armor_profs = ["light armor","medium armor"]



class Elf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Elf"
        self.asi["DEX"] = 2
        self.size = "Medium"
        self.speed = 30
        self.traits = ["Darkvision","Fey Ancestry","Trance"]
        self.skill_profs = ["Perception"]
        self.langs = ["Common","Elvish"]
        self.subraces = [High_Elf, Wood_Elf, Drow]

class High_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.name = "High Elf"
        self.asi["INT"] = 1
        self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
        self.spells = ["CHOICE"]
        self.langs.append("CHOICE")

class Wood_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.name = "Wood Elf"
        self.asi["WIS"] = 1
        self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
        self.speed = 35
        self.traits.append("Mask of the Wild")

class Drow(Elf):
    def __init__(self):
        super().__init__()
        self.name = "Drow"
        self.asi["CHA"] = 1
        self.traits.append("Sunlight Sensitivity")
        self.spells = ["Dancing Lights"]
        self.weapon_profs = ["rapier","shortsword","hand crossbow"]

    def race_check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Faerie Fire")
        if PC.lvl >= 5:
            self.spells.append("Darkness")



class Halfling(Race):
    def __init__(self):
        super().__init__()
        self.name = "Halfling"
        self.asi["DEX"] = 2
        self.size = "Small"
        self.speed = 25
        self.traits = ["Lucky","Brave","Halfling Nimbleness"]
        self.langs = ["Common","Halfling"]
        self.subraces = [Lightfoot_Halfling, Stout_Halfling]

class Lightfoot_Halfling(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Lightfoot Halfling"
        self.asi["CHA"] = 1
        self.traits.append("Naturally Stealthy")

class Stout_Halfling(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Stout Halfling"
        self.asi["CON"] = 1
        self.traits.append("Stout Resilience")



class Human(Race):
    def __init__(self):
        super().__init__()
        self.name = "Human"
        self.asi["STR"] = 1
        self.asi["DEX"] = 1
        self.asi["CON"] = 1
        self.asi["INT"] = 1
        self.asi["WIS"] = 1
        self.asi["CHA"] = 1
        self.size = "Medium"
        self.speed = 30
        self.langs = ["Common","CHOICE"]

class Human_Variant(Race):
    def __init__(self):
        super().__init__()
        self.name = "Human (Variant)"
        self.asi["CHOICE1"] = 1
        self.asi["CHOICE2"] = 1
        self.size = "Medium"
        self.speed = 30
        self.langs = ["Common","CHOICE"]
        self.skill_profs = ["CHOICE"]
        self.feats = ["CHOICE"]



class Dragonborn(Race):
    def __init__(self):
        super().__init__()
        self.name = "Dragonborn"
        self.asi["STR"] = 2
        self.asi["CHA"] = 1
        self.size = "Medium"
        self.speed = 30
        self.traits = ["Draconic Ancestry","Breath Weapon","Damage Resistance"]
        self.langs = ["Common","Draconic"]



class Gnome(Race):
    def __init__(self):
        super().__init__()
        self.name = "Gnome"
        self.asi["INT"] = 2
        self.size = "Small"
        self.speed = 25
        self.traits = ["Darkvision","Gnome Cunning"]
        self.langs = ["Common","Gnomish"]
        self.subraces = [Forest_Gnome, Rock_Gnome]

class Forest_Gnome(Gnome):
    def __init__(self):
        super().__init__()
        self.name = "Forest Gnome"
        self.asi["DEX"] = 1
        self.spells = ["Minor Illusion"]
        self.traits.append("Speak with Small Beasts")

class Rock_Gnome(Gnome):
    def __init__(self):
        super().__init__()
        self.name = "Rock Gnome"
        self.asi["CON"] = 1
        self.traits.extend(["Artificer's Lore","Tinker"])



class Half_Elf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Half-Elf"
        self.asi["CHA"] = 2
        self.asi["CHOICE1"] = 1
        self.asi["CHOICE2"] = 1
        self.size = "Medium"
        self.speed = 30
        self.traits = ["Darkvision","Fey Ancestry"]
        self.skill_profs = ["CHOICE1","CHOICE2"]
        self.langs = ["Common","Elvish","CHOICE"]



class Half_Orc(Race):
    def __init__(self):
        super().__init__()
        self.name = "Half-Orc"
        self.asi["STR"] = 2
        self.asi["CON"] = 1
        self.size = "Medium"
        self.speed = 30
        self.traits = ["Darkvision","Relentless Endurance","Savage Attacks"]
        self.skill_profs = ["Intimidation"]
        self.langs = ["Common","Orc"]



class Tiefling(Race):
    def __init__(self):
        super().__init__()
        self.name = "Tiefling"
        self.asi["INT"] = 1
        self.asi["CHA"] = 2
        self.size = "Medium"
        self.speed = 30
        self.traits = ["Darkvision","Hellish Resistance"]
        self.spells = ["Thaumaturgy"]
        self.langs = ["Common","Infernal"]

    def race_check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Hellish Rebuke")
        if PC.lvl >= 5:
            self.spells.append("Darkness")
