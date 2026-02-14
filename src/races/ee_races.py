from char_values import PC, Race


class Aarakocra(Race):
    def __init__(self):
        super().__init__()
        self.name = "Aarakocra"
        self.asi = [(1,2),(5,1)]
        self.size = "Medium"
        self.speed["walk"] = 25
        self.speed["fly"] = 50
        self.traits = ["Flight", "Talons"]
        self.langs = ["Common","Aarakocra","Auran (Primordial)"]


class Genasi(Race):
    def __init__(self):
        super().__init__()
        self.name = "Genasi"
        self.asi = [(2,2)]
        self.size = "Medium"
        self.speed["walk"] = 30
        self.langs = ["Common","Primordial"]

class Air_Genasi(Genasi):
    def __init__(self):
        super().__init__()
        self.parent = Genasi()
        self.name = "Air Genasi"
        self.asi.append((1,1))
        self.traits = ["Unending Breath"]
        self.spells = ["Levitate"]

class Earth_Genasi(Genasi):
    def __init__(self):
        super().__init__()
        self.parent = Genasi()
        self.name = "Earth Genasi"
        self.asi.append((0,1))
        self.traits = ["Merge with Stone"]
        self.spells = ["Pass without Trace"]

class Fire_Genasi(Genasi):
    def __init__(self):
        super().__init__()
        self.parent = Genasi()
        self.name = "Fire Genasi"
        self.asi.append((3,1))
        self.traits = ["Darkvision","Fire Resistance"]
        self.spells = ["Produce Flame"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Burning Hands")

class Water_Genasi(Genasi):
    def __init__(self):
        super().__init__()
        self.parent = Genasi()
        self.name = "Water Genasi"
        self.asi.append((4,1))
        self.traits = ["Acid Resistance","Amphibious"]
        self.speed["swim"] = 30
        self.spells = ["Shape Water"]

    def check_lvl(self):
        if PC.lvl >= 3:
            self.spells.append("Create or Destroy Water")


class Goliath(Race):
    def __init__(self):
        super().__init__()
        self.name = "Goliath"
        self.asi = [(0,2),(2,1)]
        self.size = "Medium"
        self.speed["walk"] = 30
        self.traits = ["Stone's Endurance","Powerful Build","Mountain Born"]
        self.skill_profs = ["Athletics"]
        self.langs = ["Common","Giant"]
