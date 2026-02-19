from char_values import PC, Race
from races.phb_races import Tiefling, Elf
from languages import languages
from skills import skills
from tools import tools


class Asmodeus_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Asmodeus Tiefling (Default)"

class Baalzebul_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Baalzebul Tiefling"
        self.spells[0] = ["Thaumaturgy*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Ray of Sickness*" not in self.spells[1]:
            self.spells[1].append("Ray of Sickness*")
        if PC.lvl >= 5 and "Crown of Madness*" not in self.spells[2]:
            self.spells[2].append("Crown of Madness*")

class Dispater_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Dispater Tiefling"
        self.asi = [(1,1),(5,2)]
        self.spells[0] = ["Thaumaturgy*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Disguise Self*" not in self.spells[1]:
            self.spells[1].append("Disguise Self*")
        if PC.lvl >= 5 and "Detect Thoughts*" not in self.spells[2]:
            self.spells[2].append("Detect Thoughts*")

class Fierna_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Fierna Tiefling"
        self.asi = [(4,1),(5,2)]
        self.spells[0] = ["Friends*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Charm Person*" not in self.spells[1]:
            self.spells[1].append("Charm Person*")
        if PC.lvl >= 5 and "Suggestion*" not in self.spells[2]:
            self.spells[2].append("Suggestion*")

class Glasya_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Glasya Tiefling"
        self.asi = [(1,1),(5,2)]
        self.spells[0] = ["Minor Illusion*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Disguise Self*" not in self.spells[1]:
            self.spells[1].append("Disguise Self*")
        if PC.lvl >= 5 and "Invisibility*" not in self.spells[2]:
            self.spells[2].append("Invisibility*")

class Levistus_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Levistus Tiefling"
        self.asi = [(2,1),(5,2)]
        self.spells[0] = ["Ray of Frost*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Armor of Agathys*" not in self.spells[1]:
            self.spells[1].append("Armor of Agathys*")
        if PC.lvl >= 5 and "Darkness*" not in self.spells[2]:
            self.spells[2].append("Darkness*")

class Mammon_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Mammon Tiefling"
        self.spells[0] = ["Mage Hand*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Tenser's Floating Disk*" not in self.spells[1]:
            self.spells[1].append("Tenser's Floating Disk*")
        if PC.lvl >= 5 and "Arcane Lock*" not in self.spells[1]:
            self.spells[1].append("Arcane Lock*")

class Mephistopheles_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Mephistopheles Tiefling"
        self.spells[0] = ["Mage Hand*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Burning Hands*" not in self.spells[1]:
            self.spells[1].append("Burning Hands*")
        if PC.lvl >= 5 and "Flame Blade*" not in self.spells[2]:
            self.spells[2].append("Flame Blade*")

class Zariel_Tiefling(Tiefling):
    def __init__(self):
        super().__init__()
        self.parent = Tiefling()
        self.name = "Zariel Tiefling"
        self.asi = [(0,1),(5,2)]
        self.spells[0] = ["Thaumaturgy*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Searing Smite*" not in self.spells[1]:
            self.spells[1].append("Searing Smite*")
        if PC.lvl >= 5 and "Branding Smite*" not in self.spells[2]:
            self.spells[2].append("Branding Smite*")


class Eladrin(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "Eladrin"
        self.asi.append((5,1))
        self.traits.append("Fey Step")

class Sea_Elf(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "Sea Elf"
        self.asi.append((2,1))
        self.weapon_profs.extend(["spear", "Trident", "Light Crossbow", "net"])
        self.speed["swim"] = 30
        self.traits.extend(["Child of the Sea", "Friend of the Sea"])
        self.langs.append("Primordial (Aquan)")

class Shadar_Kai(Elf):
    def __init__(self):
        super().__init__()
        self.parent = Elf()
        self.name = "Shadar-Kai"
        self.asi.append((2,1))
        self.traits.extend(["Necrotic Resistance", "Blessing of the Raven Queen"])


class Gith(Race):
    def __init__(self):
        super().__init__()
        self.name = "Gith"
        self.asi = [(3,1)]
        self.langs.append("Gith")

class Githyanki(Gith):
    def __init__(self):
        super().__init__()
        self.parent = Gith()
        self.name = "Githyanki"
        self.asi.append((0,2))
        self.armor_profs = ["light armor", "medium armor"]
        self.weapon_profs = ["shortsword", "longsword", "greatsword"]
        self.spells[0] = ["Mage Hand*"]

    def choices(self):
        chosen = False
        while not chosen:
            print("\nChoose a language other than Common or Gith.")
            for i in range(len(languages)):
                print(f"[{i+1}] - {languages[i]}")
            while not chosen:
                inp = str.lower(input())
                if inp == "exit":
                    quit()
                if inp.isdigit() and 1 <= int(inp) <= len(languages) and languages[int(inp)-1] not in self.langs and languages[int(inp)-1] not in PC.langs:
                    self.langs.append(languages[int(inp)-1])
                    chosen = True
                else:
                    print(f"{inp} is not a valid language name or is already known by your character.")

        while True:
            print("\nChoose a tool or skill proficiency.")
            for i in range(len(tools) + len(skills)):
                if i < len(tools):
                    print(f"[{i+1}] - {tools[i]}")
                else:
                    print(f"[{i+1}] - {skills[i-len(tools)]}")
            while True:
                inp = str.lower(input())
                if inp == "exit":
                    quit()
                if inp.isdigit() and 1 <= int(inp) <= (len(tools) + len(skills)) and ((int(inp) <= len(tools) and tools[int(inp)-1] not in self.tool_profs and tools[int(inp)-1] not in PC.tool_profs) or (int(inp) > len(tools) and skills[int(inp)-len(tools)-1] not in self.skill_profs and skills[int(inp)-len(tools)-1] not in PC.skill_profs)):
                    if int(inp) <= len(tools):
                        self.tool_profs.append(tools[int(inp)-1])
                    else:
                        self.skill_profs.append(skills[int(inp)-len(tools)-1])
                    return
                else:
                    print(f"{inp} is not a valid tool/skill name or is already known by your character.")

    def check_lvl(self):
        if PC.lvl >= 3 and "Jump*" not in self.spells[1]:
            self.spells[1].append("Jump*")
        if PC.lvl >= 5 and "Misty Step*" not in self.spells[2]:
            self.spells[2].append("Misty Step*")

class Githzerai(Gith):
    def __init__(self):
        super().__init__()
        self.parent = Gith()
        self.asi.append((4,2))
        self.name = "Githzerai"
        self.traits.append("Mental Discipline")
        self.spells[0] = ["Mage Hand*"]

    def check_lvl(self):
        if PC.lvl >= 3 and "Shield*" not in self.spells[1]:
            self.spells[1].append("Shield*")
        if PC.lvl >= 5 and "Detect Thoughts*" not in self.spells[2]:
            self.spells[2].append("Detect Thoughts*")
