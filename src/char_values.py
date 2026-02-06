class Character:
    def __init__(self, lvl=1, ability_scores=[10,10,10,10,10,10], race="none", job="none", name="nameless", background="none", feats=[], proficiencies=[], languages=["Common"], spells=[]):
        self.lvl = lvl
        self.scores = ability_scores
        self.race = race
        self.job = job
        self.name = name
        self.bground = background
        self.feats = feats
        self.profs = proficiencies
        self.langs = languages
        self.spells = spells


PC = Character()