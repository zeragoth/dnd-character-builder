from char_values import PC
from races.phb_races import Dwarf, Gnome, Halfling, Half_Elf, Tiefling
from spells import wizard_spells


class Duergar(Dwarf):
    def __init__(self):
        super().__init__()
        self.parent = Dwarf()
        self.name = "Duergar"
        self.asi.append((0,1))
        self.traits[0] = "Superior Darkvision"
        self.langs.append("Undercommon")
        self.traits.extend(["Duergar Resilience","Sunlight Sensitivity"])

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells[2] = ["Enlarge/Reduce*"]
        if PC.lvl >= 5:
            self.spells[2] = ["Enlarge/Reduce*", "Invisibility*"]

class Svirfneblin(Gnome):
    def __init__(self):
        super().__init__()
        self.parent = Gnome()
        self.name = "Deep Gnome"
        self.asi.append((1,1))
        self.traits[0] = "Superior Darkvision"
        self.traits.append("Stone Camouflage")
        self.langs.append("Undercommon")


class Ghostwise_Halfling(Halfling):
    def __init__(self):
        super().__init__()
        self.parent = Halfling()
        self.name = "Ghostwise Halfling"
        self.asi.append((4,1))
        self.traits.append("Silent Speech")


class Half_Elf_Variant(Half_Elf):
    def __init__(self):
        super().__init__()
        self.name = "Half-elf (Variant)"
        

    def choices(self):
        self.drow_magic = False
        self.spells[0] = []

        print("\nChoose a trait.")
        print("[1] - Keen Senses\n--Wood Elf Descent--\n[2] - Elf Weapon Training (Wood Elf)\n"
        "[3] - Fleet of Foot\n[4] - Mask of the Wild\n--Moon/Sun Elf Descent--\n"
        "[5] - Elf Weapon Training (High Elf)\n[6] - Cantrip\n--Drow Descent--\n"
        "[7] - Drow Magic\n--Aquatic Descent--\n[8] - 30 feet swimming speed")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            elif "1" in inp:
                self.skill_profs = ["Perception"]
            elif "2" in inp:
                self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
            elif "3" in inp:
                self.speed["walk"] = 35
            elif "4" in inp:
                self.traits.append("Mask of the Wild")
            elif "5" in inp:
                self.weapon_profs = ["longsword","shortsword","shortbow","longbow"]
            elif "6" in inp:
                print("\nChoose a cantrip from the Wizard spell list.")
                for i in range(len(wizard_spells[0])):
                    print(f"[{i+1}] - {wizard_spells[0][i]}")
                while True:
                    inp = str.lower(input())
                    if inp == "exit":
                        quit()
                    if inp.isdigit() and 1 <= int(inp) <= len(wizard_spells[0]) and wizard_spells[0][int(inp)-1] not in self.spells[0] and wizard_spells[0][int(inp)-1] not in PC.spells[0]:
                        self.spells[0].append(wizard_spells[0][int(inp)-1])
                        break
                    else:
                        print(f"{inp} is not a valid spell choice or is already known by your character.")
            elif "7" in inp:
                self.drow_magic = True
            elif "8" in inp:
                self.speed["swim"] = 30
            else:
                print(f"{inp} is not a valid input.")
            return

    def check_lvl(self):
        if self.drow_magic == True:
            if PC.lvl >= 3:
                self.spells[1] = ["Faerie Fire*"]
            if PC.lvl >= 5:
                self.spells[2] = ["Darkness*"]
 

class Tiefling_Variant(Tiefling):
    def __init__(self):
        super().__init__()
        self.name = "Tiefling (Variant)"
        self.asi = [(1,2),(3,1)]

    def choices(self):
        self.devil_tongue = False
        self.hellfire = False
        self.winged = False
        self.infernal = False

        print("\nChoose a trait.")
        print("[1] - Devil's Tongue\n[2] - Hellfire\n[3] - Winged\n[4] - None (default Infernal Legacy)")
        inp = str.lower(input())
        if inp == "exit":
            quit()
        elif "1" in inp:
            self.devil_tongue = True
        elif "2" in inp:
            self.hellfire = True
        elif "3" in inp:
            self.speed["fly"] = 30
            self.winged = True
        elif "4" in inp:
            self.infernal = True
        else:
            print(f"{inp} is not a valid input.")
            self.choices()
        return

    def check_lvl(self):

        if self.devil_tongue == True:
            self.spells[0] = ["Vicious Mockery*"]
            if PC.lvl >= 3:
                self.spells[1] = ["Charm Person*"]
            if PC.lvl >= 5:
                self.spells[2] = ["Enthrall*"]

        if self.hellfire == True:
            if PC.lvl >= 3:
                self.spells[1] = ["Burning Hands*"]
            if PC.lvl >= 5:
                self.spells[2] = ["Darkness*"]

        if self.infernal == True:
            if PC.lvl >= 3:
                self.spells[1] = ["Hellish Rebuke*"]
            if PC.lvl >= 5:
                self.spells[2] = ["Darkness*"]
