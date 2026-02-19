class Race:
    def __init__(self):
        self.name = "race"
        self.asi = []
        self.size = "Medium"
        self.speed = {"walk": 30}
        self.armor_profs = []
        self.weapon_profs = []
        self.tool_profs = []
        self.skill_profs = []
        self.traits = []
        self.langs = ["Common"]
        self.parent = None
        self.subraces = []
        self.spells = [[],[],[],[],[],[],[],[],[],[]]
        self.feats = []

    def check_lvl(self):
        pass

    def choices(self):
        pass



PCRace = Race()


class Character:
    def __init__(self):
        self.lvl = 1
        self.scores = [10,10,10,10,10,10]
        self.racial_scores = [0,0,0,0,0,0]
        self.race = PCRace
        self.job = "none"
        self.name = "nameless"
        self.bground = "none"
        self.feats = []
        self.armor_profs = []
        self.weapon_profs = []
        self.tool_profs = []
        self.skill_profs = []
        self.langs = []
        self.spells = [[],[],[],[],[],[],[],[],[],[]]
        self.books = []


PC = Character()
