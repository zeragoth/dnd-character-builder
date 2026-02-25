# Contains the class for every job in the Player's Handbook.
# A job's class handles choices that need to be made when selected,
# and features that are added when leveling up.

from char_values import Job, PC


class Barbarian(Job):
    def __init__(self):
        super().__init__()
        self.name = "Barbarian"
        self.armor_profs = ["light armor", "medium armor", "shields"]
        self.weapon_profs = ["simple weapons", "martial weapons"]
        self.save_profs = [0,2]
        self.path_chosen = False
        self.fast_movement = False

    def choices(self):
        counter = 0
        available_skills = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
        self.skill_profs = []
        self.features = ["Rage", "Unarmored Defense"]

        print("Choose 2 skill proficiencies.")
        
        while counter < 2:
            for i in range(len(available_skills)):
                if available_skills[i-1] in self.skill_profs or available_skills[i-1] in PC.skill_profs:
                    del available_skills[i-1]
            for i in range(len(available_skills)):
                print(f"[{i+1}] - {available_skills[i]}")
            inp = str.lower(input())
            if inp == "exit":
                quit()
            if inp.isdigit() and 1 <= int(inp) <= len(available_skills) and available_skills[int(inp)-1] not in self.skill_profs and available_skills[int(inp)-1] not in PC.skill_profs:
                self.skill_profs.append(available_skills[int(inp)-1])
                counter += 1
            else:
                print(f"{inp} is not a valid skill name or your character is already proficient.")
        
    def check_lvl(self):
        self.hp = (12 + PC.modifiers[2]) + ((7 + PC.modifiers[2]) * (PC.lvl - 1))

        if PC.lvl >= 2 and "Reckless Attack" not in self.features:
            self.features.extend(["Reckless Attack", "Danger Sense"])
        if PC.lvl >= 3 and self.path_chosen == False:
            pass
        if PC.lvl >= 4 and self.asi_count == 0:
            self.ability_score_increase()
        if PC.lvl >= 5 and "Extra Attack" not in self.features:
            self.features.append("Extra Attack")
            if self.fast_movement == False:
                for value in PC.speed.values():
                    value += 10
                self.fast_movement = True
        if PC.lvl >= 7 and "Feral Instinct" not in self.features:
            self.features.append("Feral Instinct")
        if PC.lvl >= 9 and "Extra Attack" not in self.features:
            self.features.append("Brutal Critical")
        if PC.lvl >= 11 and "Relentless Rage" not in self.features:
            self.features.append("Relentless Rage")
        if PC.lvl >= 15 and "Persistent Rage" not in self.features:
            self.features.append("Persistent Rage")
        if PC.lvl >= 18 and "Indomitable Might" not in self.features:
            self.features.append("Indomitable Might")
        if PC.lvl == 20 and "Primal Champion" not in self.features:
            self.features.append("Primal Champion")
            PC.job_scores[0] += 4
            PC.job_scores[2] += 4
            PC.update_modifiers()
        


class Bard(Job):
    def __init__(self):
        super().__init__()
        self.name = "Bard"


class Cleric(Job):
    def __init__(self):
        super().__init__()
        self.name = "Cleric"


class Druid(Job):
    def __init__(self):
        super().__init__()
        self.name = "Druid"


class Fighter(Job):
    def __init__(self):
        super().__init__()
        self.name = "Fighter"


class Monk(Job):
    def __init__(self):
        super().__init__()
        self.name = "Monk"


class Paladin(Job):
    def __init__(self):
        super().__init__()
        self.name = "Paladin"


class Ranger(Job):
    def __init__(self):
        super().__init__()
        self.name = "Ranger"


class Rogue(Job):
    def __init__(self):
        super().__init__()
        self.name = "Rogue"


class Sorcerer(Job):
    def __init__(self):
        super().__init__()
        self.name = "Sorcerer"


class Warlock(Job):
    def __init__(self):
        super().__init__()
        self.name = "Warlock"


class Wizard(Job):
    def __init__(self):
        super().__init__()
        self.name = "Wizard"


jobs = [Barbarian(), Bard(), Cleric(), Druid(), Fighter(), Monk(), Paladin(), Ranger(), Rogue(), Sorcerer(), Warlock(), Wizard()]
