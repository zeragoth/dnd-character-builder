from char_values import PC
from races.phb_races import Dwarf, Gnome, Half_Elf, Tiefling


class Duergar(Dwarf):
    parent = Dwarf
    name = "Duergar"
    asi = parent.asi.copy()
    asi.append((0,1))
    traits = parent.traits.copy()
    traits[0] = "Superior Darkvision"
    langs = parent.langs.copy()
    langs.append("Undercommon")
    traits.extend(["Duergar Resilience","Sunlight Sensitivity"])

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Enlarge/Reduce*")
        if PC.lvl >= 5:
            self.spells.append("Invisibility*")

class Svirfneblin(Gnome):
    parent = Gnome
    name = "Deep Gnome"
    asi = parent.asi.copy()
    asi.append((1,1))
    traits = parent.traits.copy()
    traits[0] = "Superior Darkvision"
    traits.append("Stone Camouflage")
    langs = parent.langs.copy()
    langs.append("Undercommon")


class Half_Elf_Variant(Half_Elf):
    name = "Half-elf (Variant)"
    skill_profs = []
    drow_magic = False

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
    name = "Tiefling (Variant)"
    asi = [(1,2),(3,1)]
    devil_tongue = False
    hellfire = False
    winged = False
    infernal = False

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
