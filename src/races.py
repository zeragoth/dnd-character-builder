from char_values import PC, Race


# Player's Handbook (PHB)

class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.name = "Dwarf"
        # each asi is a tuple with (ability score index, increase amount)
        # eg (0,2) is STR +2, (3,1) is INT +1
        self.asi = [(2,2)]
        self.size = "Medium"
        self.speed = "25"
        self.weapon_profs = ["battleaxe","handaxe","light hammer","warhammer"]
        self.tool_profs = ["CHOICE"]
        self.traits = ["Darkvision","Dwarven Resilience","Stonecunning"]
        self.langs = ["Common","Dwarvish"]
        self.subraces = [Hill_Dwarf, Mountain_Dwarf]

class Hill_Dwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.name = "Hill Dwarf"
        self.asi.append((4,1))
        self.traits.append("Dwarven Toughness")
        
class Mountain_Dwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.name = "Mountain Dwarf"
        self.asi.append((0,1))
        self.armor_profs = ["light armor","medium armor"]


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
        self.subraces = [High_Elf, Wood_Elf, Drow]

class High_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.name = "High Elf"
        self.asi.append((3,1))
        self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
        self.spells = ["CHOICE"]
        self.langs.append("CHOICE")

class Wood_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.name = "Wood Elf"
        self.asi.append((4,1))
        self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
        self.speed = "35"
        self.traits.append("Mask of the Wild")

class Drow(Elf):
    def __init__(self):
        super().__init__()
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
        self.subraces = [Lightfoot_Halfling, Stout_Halfling]

class Lightfoot_Halfling(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Lightfoot Halfling"
        self.asi.append((5,1))
        self.traits.append("Naturally Stealthy")

class Stout_Halfling(Halfling):
    def __init__(self):
        super().__init__()
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
        self.subraces = [Forest_Gnome, Rock_Gnome]

class Forest_Gnome(Gnome):
    def __init__(self):
        super().__init__()
        self.name = "Forest Gnome"
        self.asi.append((1,1))
        self.spells = ["Minor Illusion"]
        self.traits.append("Speak with Small Beasts")

class Rock_Gnome(Gnome):
    def __init__(self):
        super().__init__()
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
            self.spells.append("Hellish Rebuke")
        if PC.lvl >= 5:
            self.spells.append("Darkness")





# Sword Coast Adventurer's Guide (SCAG)

class Duergar(Dwarf):
    def __init__(self):
        super().__init__()
        self.name = "Duergar"
        self.asi.append((0,1))
        self.traits[0] = "Superior Darkvision"
        self.langs.append("Undercommon")
        self.traits.extend(["Duergar Resilience","Sunlight Sensitivity"])

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Enlarge/Reduce*")
        if PC.lvl >= 5:
            self.spells.append("Invisibility*")


class Svirfneblin(Gnome):
    def __init__(self):
        super().__init__()
        self.name = "Deep Gnome"
        self.asi.append((1,1))
        self.traits[0] = "Superior Darkvision"
        self.traits.append("Stone Camouflage")
        self.langs.append("Undercommon")


class Half_Elf_Variant(Half_Elf):
    def __init__(self):
        super().__init__()
        self.name = "Half-elf (Variant)"
        self.skill_profs = []
        self.drow_magic = False

    def choices(self):
        print("Choose a trait.")
        print("[1] - Keen Senses\n--Wood Elf Descent--\n[2] - Elf Weapon Training (Wood Elf)\n"
        "[3] - Fleet of Foot\n[4] - Mask of the Wild\n--Moon/Sun Elf Descent--\n"
        "[5] - Elf Weapon Training (High Elf)\n[6] - Cantrip\n--Drow Descent--\n"
        "[7] - Drow Magic\n--Aquatic Descent--\n[8] - 30 feet swimming speed")
        inp = str.lower(input())
        if inp == "exit":
            quit()
        elif "1" in inp:
            self.skill_profs = ["Perception"]
        elif "2" in inp:
            self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
        elif "3" in inp:
            self.speed = "35"
        elif "4" in inp:
            self.traits.append("Mask of the Wild")
        elif "5" in inp:
            self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
        elif "6" in inp:
            self.spells = ["CHOICE"]
        elif "7" in inp:
            self.drow_magic = True
        elif "8" in inp:
            self.speed += ", Swim 30"
        else:
            print(f"{inp} is not a valid input.")
            self.choices()
        return

    def check_lvl(self):
        if self.drow_magic == True:
            if PC.lvl >= 3:
                self.spells.append("Faerie Fire")
            if PC.lvl >= 5:
                self.spells.append("Darkness")
    

    class Tiefling_Variant(Tiefling):
        def __init__(self):
            super().__init__()
            self.name = "Tiefling (Variant)"
            self.asi = [(1,2),(3,1)]
            self.devil_tongue = False
            self.hellfire = False
            self.winged = False
            self.infernal = False

        def choices(self):
            print("Choose a trait.")
            print("[1] - Devil's Tongue\n[2] - Hellfire\n[3] - Winged\n[4] - None (default Infernal Legacy)")
            inp = str.lower(input())
            if inp == "exit":
                quit()
            elif "1" in inp:
                self.devil_tongue = True
            elif "2" in inp:
                self.hellfire = True
            elif "3" in inp:
                self.speed += ", Fly 30"
            elif "4" in inp:
                self.infernal = True
            else:
                print(f"{inp} is not a valid input.")
                self.choices()
            return

        def check_lvl(self):
            if self.devil_tongue == True:
                self.spells.append("Vicious Mockery")
                if PC.lvl >= 3:
                    self.spells.append("Charm Person")
                if PC.lvl >= 5:
                    self.spells.append("Enthrall")

            if self.hellfire == True:
                if PC.lvl >= 3:
                    self.spells.append("Burning Hands")
                if PC.lvl >= 5:
                    self.spells.append("Darkness")

            if self.infernal == True:
                if PC.lvl >= 3:
                    self.spells.append("Hellish Rebuke")
                if PC.lvl >= 5:
                    self.spells.append("Darkness")





# Elemental Evil Player's Companion (EE)

class Aarakocra(Race):
    def __init__(self):
        super().__init__()
        
