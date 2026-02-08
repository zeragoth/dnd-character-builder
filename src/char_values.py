class Race:
    def __init__(self):
        self.name = "race"
        self.asi = {}
        self.size = "size"
        self.speed = 30
        self.armor_profs = []
        self.weapon_profs = []
        self.tool_profs = []
        self.skill_profs = []
        self.traits = []
        self.langs = []
        self.subraces = []
        self.spells = []
        self.feats = []

    def race_check_lvl():
        pass


class Character:
    def __init__(self):
        self.lvl = 1
        self.scores = [10,10,10,10,10,10]
        self.race = Race()
        self.job = "none"
        self.name = "nameless"
        self.bground = "none"
        self.feats = []
        self.armor_profs = []
        self.weapon_profs = []
        self.tool_profs = []
        self.skill_profs = []
        self.langs = []
        self.spells = []
        self.books = []


PC = Character()
