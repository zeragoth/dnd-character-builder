class Race:
    def __init__(self):
        pass
    name = "race"
    asi = []
    size = "size"
    speed = "30"
    armor_profs = []
    weapon_profs = []
    tool_profs = []
    skill_profs = []
    traits = []
    langs = []
    parent = None
    subraces = []
    spells = []
    feats = []

    def check_lvl():
        pass

    def choices():
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
        self.spells = []
        self.books = []


PC = Character()
