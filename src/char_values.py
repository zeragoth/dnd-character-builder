# Do not import files
# Contains default/base Race. Job, and Character classes.

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

class Job:
    def __init__(self):
        self.name = "job"
        self.asi_count = 0
        self.hp = 0
        self.armor_profs = []
        self.weapon_profs = []
        self.tool_profs = []
        self.save_profs = []
        self.skill_profs = []
        self.features = []
        self.parent = None
        self.subclasses = []
        self.spells = [[],[],[],[],[],[],[],[],[],[]]

    def check_lvl(self):
        pass

    def choices(self):
        pass

    def ability_score_increase(self):
        print(f"\nChoose 2 ability scores to increase by 1.")
        counter = 0
        while counter < 2:
            print("[1] - Strength\n[2] - Dexterity\n[3] - Constitution\n[4] - Intelligence\n[5] - Wisdom\n[6] - Charisma")

            inp = str.lower(input())
            if inp == "exit":
                quit()

            if "1" in inp and PC.job_scores[0] < 20:
                PC.job_scores[0] += 1
            elif "2" in inp and PC.job_scores[1] < 20:
                PC.job_scores[1] += 1
            elif "3" in inp and PC.job_scores[2] < 20:
                PC.job_scores[2] += 1
            elif "4" in inp and PC.job_scores[3] < 20:
                PC.job_scores[3] += 1
            elif "5" in inp and PC.job_scores[4] < 20:
                PC.job_scores[4] += 1
            elif "6" in inp and PC.job_scores[5] < 20:
                PC.job_scores[5] += 1
            else:
                print(f"{inp} is not a valid choice.")
            counter += 1
        self.asi_count += 1
        PC.update_modifiers()


PCJob = Job()


class Character:
    def __init__(self):
        self.lvl = 1
        self.scores = [10,10,10,10,10,10]
        self.racial_scores = [0,0,0,0,0,0]
        self.job_scores = [0,0,0,0,0,0]
        self.hp = 0
        self.modifiers = [0,0,0,0,0,0]
        self.race = PCRace
        self.speed = PCRace.speed
        self.job = PCJob
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

    def update_modifiers(self):
        for i in range(len(self.scores)):
            self.modifiers[i] = (self.scores[i] + self.racial_scores[i] + self.job_scores - 10) // 2


PC = Character()
