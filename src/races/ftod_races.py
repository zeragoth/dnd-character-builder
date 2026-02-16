from char_values import PC, Race


class Chromatic_Dragonborn(Race):
    def __init__(self):
        super().__init__()
        self.name = "Chromatic Dragonborn"
        self.asi = [["CHOICE",2],["CHOICE",1]]
        self.traits = ["Chromatic Ancestry", "Breath Weapon", "Draconic Resistance"]

    def choices(self):
        print("Choose a draconic ancestry.")
        print("[1] - Black (Acid)\n[2] - Blue (Lightning)\n[3] - Green (Poison)\n[4] - Red (Fire)\n"
        "[5] - White (Cold)")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            elif "1" in inp:
                self.traits[0] = "Chromatic Ancestry: Black Dragon (Acid)"
            elif "2" in inp:
                self.traits[0] = "Chromatic Ancestry: Blue Dragon (Lightning)"
            elif "3" in inp:
                self.traits[0] = "Chromatic Ancestry: Green Dragon (Poison)"
            elif "4" in inp:
                self.traits[0] = "Chromatic Ancestry: Red Dragon (Fire)"
            elif "5" in inp:
                self.traits[0] = "Chromatic Ancestry: White Dragon (Cold)"
            else:
                print(f"{inp} is not a valid input.")
            return
        
    def check_lvl(self):
        if PC.lvl >= 5 and "Chromatic Warding" not in self.traits:
            self.traits.append("Chromatic Warding")

class Gem_Dragonborn(Race):
    def __init__(self):
        super().__init__()
        self.name = "Gem Dragonborn"
        self.asi = [["CHOICE",2],["CHOICE",1]]
        self.traits = ["Gem Ancestry", "Breath Weapon", "Draconic Resistance", "Psionic Mind"]

    def choices(self):
        print("Choose a draconic ancestry.")
        print("[1] - Amethyst (Force)\n[2] - Crystal (Radiant)\n[3] - Emerald (Psychic)\n[4] - Sapphire (Thunder)\n"
        "[5] - Topaz (Necrotic)")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            elif "1" in inp:
                self.traits[0] = "Gem Ancestry: Amethyst Dragon (Force)"
            elif "2" in inp:
                self.traits[0] = "Gem Ancestry: Crystal Dragon (Radiant)"
            elif "3" in inp:
                self.traits[0] = "Gem Ancestry: Emerald Dragon (Psychic)"
            elif "4" in inp:
                self.traits[0] = "Gem Ancestry: Sapphire Dragon (Thunder)"
            elif "5" in inp:
                self.traits[0] = "Gem Ancestry: Topaz Dragon (Necrotic)"
            else:
                print(f"{inp} is not a valid input.")
            return
        
    def check_lvl(self):
        if PC.lvl >= 5 and "Gem Flight" not in self.traits:
            self.traits.append("Gem Flight")

class Metallic_Dragonborn(Race):
    def __init__(self):
        super().__init__()
        self.name = "Metallic Dragonborn"
        self.asi = [["CHOICE",2],["CHOICE",1]]
        self.traits = ["Metallic Ancestry", "Breath Weapon", "Draconic Resistance"]

    def choices(self):
        print("Choose a draconic ancestry.")
        print("[1] - Brass (Fire)\n[2] - Bronze (Lightning)\n[3] - Copper (Acid)\n[4] - Gold (Fire)\n"
        "[5] - Silver (Cold)")
        while True:
            inp = str.lower(input())
            if inp == "exit":
                quit()
            elif "1" in inp:
                self.traits[0] = "Metallic Ancestry: Brass Dragon (Fire)"
            elif "2" in inp:
                self.traits[0] = "Metallic Ancestry: Bronze Dragon (Lightning)"
            elif "3" in inp:
                self.traits[0] = "Metallic Ancestry: Copper Dragon (Acid)"
            elif "4" in inp:
                self.traits[0] = "Metallic Ancestry: Gold Dragon (Fire)"
            elif "5" in inp:
                self.traits[0] = "Metallic Ancestry: Silver Dragon (Cold)"
            else:
                print(f"{inp} is not a valid input.")
            return
        
    def check_lvl(self):
        if PC.lvl >= 5 and "Metallic Breath Weapon" not in self.traits:
            self.traits.append("Metallic Breath Weapon")
