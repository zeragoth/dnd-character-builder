class Job:
    def __init__(self):
        self.name = "job"


class Barbarian(Job):
    def __init__(self):
        self.name = "Barbarian"

class Bard(Job):
    def __init__(self):
        self.name = "Bard"

class Cleric(Job):
    def __init__(self):
        self.name = "Cleric"

class Druid(Job):
    def __init__(self):
        self.name = "Druid"

class Fighter(Job):
    def __init__(self):
        self.name = "Fighter"

class Monk(Job):
    def __init__(self):
        self.name = "Monk"

class Paladin(Job):
    def __init__(self):
        self.name = "Paladin"

class Ranger(Job):
    def __init__(self):
        self.name = "Ranger"

class Rogue(Job):
    def __init__(self):
        self.name = "Rogue"

class Sorcerer(Job):
    def __init__(self):
        self.name = "Sorcerer"

class Warlock(Job):
    def __init__(self):
        self.name = "Warlock"

class Wizard(Job):
    def __init__(self):
        self.name = "Wizard"

jobs = [Barbarian(), Bard(), Cleric(), Druid(), Fighter(), Monk(), Paladin(), Ranger(), Rogue(), Sorcerer(), Warlock(), Wizard()]

class Artificer(Job):
    def __init__(self):
        self.name = "Artificer"
