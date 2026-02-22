from races.phb_races import (Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half_Elf,
                             Half_Orc, Tiefling,
                            Hill_Dwarf, Mountain_Dwarf, High_Elf, Wood_Elf, Drow, Lightfoot_Halfling,
                            Stout_Halfling, Human_Variant, Default_Human, Default_Half_Elf, Forest_Gnome,
                            Rock_Gnome)

from races.scag_races import Duergar, Ghostwise_Halfling, Half_Elf_Variant, Svirfneblin, Tiefling_Variant

from races.ee_races import (Aarakocra, Genasi, Goliath,
                            Air_Genasi, Earth_Genasi, Fire_Genasi, Water_Genasi)

from races.vgtm_races import (Aasimar, Firbolg, Kenku, Lizardfolk, Tabaxi, Triton, Bugbear, Goblin,
                              Hobgoblin, Kobold, Orc, Yuan_Ti_Pureblood,
                              Protector_Aasimar, Scourge_Aasimar, Fallen_Aasimar)

from races.mtof_races import (Gith,
                            Asmodeus_Tiefling, Baalzebul_Tiefling, Dispater_Tiefling, Fierna_Tiefling,
                            Glasya_Tiefling, Levistus_Tiefling, Mammon_Tiefling, Mephistopheles_Tiefling,
                            Zariel_Tiefling, Eladrin, Sea_Elf, Shadar_Kai, Githyanki, Githzerai)

from races.ftod_races import (Chromatic_Dragonborn, Gem_Dragonborn, Metallic_Dragonborn)

from races.eberron_races import (Changeling, Kalashtar, Shifter, Warforged,
                                Beasthide_Shifter, Longtooth_Shifter, Swiftstride_Shifter, Wildhunt_Shifter,
                                Mark_of_Detection, Mark_of_Finding_A, Mark_of_Finding_B, Mark_of_Handling,
                                Mark_of_Healing, Mark_of_Hospitality, Mark_of_Making, Mark_of_Passage,
                                Mark_of_Scribing, Mark_of_Sentinel, Mark_of_Shadow, Mark_of_Storm,
                                Mark_of_Warding)

from races.ravnica_races import Centaur, Loxodon, Minotaur, Simic, Vedalken

from races.theros_races import Leonin, Satyr

from races.witchlight_races import Fairy, Harengon

from spells import spells, phb_spells,scag_spells, ee_spells, xgte_spells, tcoe_spells, ftod_spells, eberron_spells, strix_spells, wilde_spells
from jobs import jobs, Artificer
from char_values import PC
from weapons import martial_melee_weapons
from languages import languages


def choose_books():
    for book in PC.books:
        book.remove_misc()
    PC.books = []
    booklist = [PHB, SCAG, EE, VGtM, MToF, XGtE, TCoE, FToD, GotG, Eberron, Ravnica, Theros, Strixhaven, Wildemount, Witchlight]

    print(f'Which source books do you have available? [Choose all that apply, eg "1, 6, 7" if you want to pick the PHB, XGtE and TCoE]')
    for book in booklist:
        print(f"[{booklist.index(book)+1}] - {book.title}")
    while True:
        inp = str.lower(input())
        if inp == "exit":
            quit()

        inp = list(map(str.strip, inp.split(",")))
        
        for i in range(len(booklist)):
            if str(i+1) in inp:
                if booklist[i] not in PC.books:
                    PC.books.append(booklist[i])
        if len(PC.books) <= 0:
            print("Please select at least one book.")
        else:
            print(f"Books selected: {get_book_titles()}")
            apply_subraces(PC.books)
            for book in PC.books:
                book.apply_misc()
                book.create_spell_list()
            return

def get_book_titles():
    book_titles = []
    for i in range(len(PC.books)):
        book_titles.append(PC.books[i].title)
    return book_titles

def apply_subraces(books):
    for book in books:
        for subrace in book.subraces:
            for other_book in books:
                for race in other_book.races:
                    if subrace.parent.name == race.name:
                        if not any(s.name == subrace.name for s in race.subraces):
                            race.subraces.append(subrace)


class Source_Book:
    def __init__(self):
        self.title = "none"
        self.races = []
        self.subraces = []
        self.jobs = []
        self.subclasses = []
        self.feats = []
        self.spells = []
        self.bgrounds = []

    def apply_misc(self):
        pass

    def remove_misc(self):
        pass

    def create_spell_list(self):
        pass

class PHB(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Player's Handbook"
        self.races = [Dwarf(), Elf(), Halfling(), Human(), Human_Variant(), Dragonborn(), Gnome(),
                      Half_Elf(), Half_Orc(), Tiefling()]
        self.subraces = [Hill_Dwarf(), Mountain_Dwarf(), High_Elf(), Wood_Elf(), Drow(),
                         Lightfoot_Halfling(), Stout_Halfling(), Default_Human(), Default_Half_Elf(), Forest_Gnome(), Rock_Gnome()]
        self.jobs = jobs
        
    def create_spell_list(self):
        for i in range(len(phb_spells)):
            if len(phb_spells[i]) > 0:
                for j in range(len(phb_spells[i])):
                    spells[i][j].extend(phb_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

class SCAG(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Sword Coast Adventurer's Guide"
        self.races = [Dwarf(), Halfling(), Half_Elf_Variant(), Gnome(), Tiefling_Variant()]
        self.subraces = [Duergar(), Ghostwise_Halfling(), Svirfneblin()]

    def create_spell_list(self):
        for i in range(len(scag_spells)):
            if len(scag_spells[i]) > 0:
                for j in range(len(scag_spells[i])):
                    spells[i][j].extend(scag_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()


class EE(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Elemental Evil Player's Companion"
        self.races = [Aarakocra(), Genasi(), Goliath()]
        self.subraces = [Svirfneblin(), Air_Genasi(), Earth_Genasi(), Fire_Genasi(), Water_Genasi()]

    def create_spell_list(self):
        for i in range(len(ee_spells)):
            if len(ee_spells[i]) > 0:
                for j in range(len(ee_spells[i])):
                    spells[i][j].extend(ee_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

    def apply_misc(self):
        if "Aarakocra" not in languages:
            languages.append("Aarakocra")

    def remove_misc(self):
        if "Aarakocra" in languages:
            languages.remove("Aarakocra")

class VGtM(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Volo's Guide to Monsters"
        self.races = [Aasimar(), Firbolg(), Goliath(), Kenku(), Lizardfolk(), Tabaxi(), Triton(), Bugbear(),
                      Goblin(), Hobgoblin(), Kobold(), Orc(), Yuan_Ti_Pureblood()]
        self.subraces = [Protector_Aasimar(), Scourge_Aasimar(), Fallen_Aasimar()]

class MToF(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Mordenkainen's Tome of Foes"
        self.races = [Gith()]
        self.subraces = [Asmodeus_Tiefling(), Baalzebul_Tiefling(), Dispater_Tiefling(), Fierna_Tiefling(),
                         Glasya_Tiefling(), Levistus_Tiefling(), Mammon_Tiefling(),
                         Mephistopheles_Tiefling(), Zariel_Tiefling(), Eladrin(), Sea_Elf(), Shadar_Kai(),
                         Duergar(), Githyanki(), Githzerai(), Svirfneblin()]
        
    def apply_misc(self):
        if "Gith" not in languages:
            languages.append("Gith")

    def remove_misc(self):
        if "Gith" in languages:
            languages.remove("Gith")

class XGtE(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Xanathar's Guide to Everything"

    def create_spell_list(self):
        for i in range(len(xgte_spells)):
            if len(xgte_spells[i]) > 0:
                for j in range(len(xgte_spells[i])):
                    spells[i][j].extend(xgte_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

class TCoE(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Tasha's Cauldron of Everything"
        self.jobs = [Artificer()]

    def create_spell_list(self):
        for i in range(len(tcoe_spells)):
            if len(tcoe_spells[i]) > 0:
                for j in range(len(tcoe_spells[i])):
                    spells[i][j].extend(tcoe_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

class FToD(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Fizban's Treasury of Dragons"
        self.races = [Chromatic_Dragonborn(), Gem_Dragonborn(), Metallic_Dragonborn()]

    def create_spell_list(self):
        for i in range(len(ftod_spells)):
            if len(ftod_spells[i]) > 0:
                for j in range(len(ftod_spells[i])):
                    spells[i][j].extend(ftod_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

class GotG(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Bigby Presents: Glory of the Giants"

class Eberron(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Eberron: Rising from the Last War"
        self.races = [Changeling(), Bugbear(), Goblin(), Hobgoblin(), Kalashtar(), Orc(), Shifter(), Warforged()]
        self.subraces = [Beasthide_Shifter(), Longtooth_Shifter(), Swiftstride_Shifter(), Wildhunt_Shifter(),
                         Mark_of_Detection(), Mark_of_Finding_A(), Mark_of_Finding_B(), Mark_of_Handling(),
                         Mark_of_Healing(), Mark_of_Hospitality(), Mark_of_Making(), Mark_of_Passage(),
                         Mark_of_Scribing(), Mark_of_Sentinel(), Mark_of_Shadow(), Mark_of_Storm(),
                         Mark_of_Warding()]
        self.jobs = [Artificer()]

    def create_spell_list(self):
        for i in range(len(eberron_spells)):
            if len(eberron_spells[i]) > 0:
                for j in range(len(eberron_spells[i])):
                    spells[i][j].extend(eberron_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

    def apply_misc(self):
        if "double-bladed scimitar" not in martial_melee_weapons:
            martial_melee_weapons.append("double-bladed scimitar")
        if "Quori" not in languages:
            languages.append("Quori")

    def remove_misc(self):
        if "double-bladed scimitar" in martial_melee_weapons:
            martial_melee_weapons.remove("double-bladed scimitar")
        if "Quori" in languages:
            languages.remove("Quori")

class Ravnica(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Guildmaster's Guide to Ravnica"
        self.races = [Centaur(), Goblin(), Loxodon(), Minotaur(), Simic(), Vedalken()]

    def apply_misc(self):
        if "Loxodon" not in languages:
            languages.append("Loxodon")
        if "Minotaur" not in languages:
            languages.append("Minotaur")
        if "Vedalken" not in languages:
            languages.append("Vedalken")

    def remove_misc(self):
        if "Loxodon" in languages:
            languages.remove("Loxodon")
        if "Minotaur" in languages:
            languages.remove("Minotaur")
        if "Vedalken" in languages:
            languages.remove("Vedalken")

class Theros(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Mythic Odysseys of Theros"
        self.races = [Centaur(), Leonin(), Minotaur(), Satyr(), Triton()]

    def apply_misc(self):
        if "Leonin" not in languages:
            languages.append("Leonin")
        if "Minotaur" not in languages:
            languages.append("Minotaur")

    def remove_misc(self):
        if "Leonin" in languages:
            languages.remove("Leonin")
        if "Minotaur" in languages:
            languages.remove("Minotaur")

class Strixhaven(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Strixhaven: A Curriculum of Chaos"

    def create_spell_list(self):
        for i in range(len(strix_spells)):
            if len(strix_spells[i]) > 0:
                for j in range(len(strix_spells[i])):
                    spells[i][j].extend(strix_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

class Wildemount(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Explorer's Guide to Wildemount"

    def create_spell_list(self):
        for i in range(len(wilde_spells)):
            if len(wilde_spells[i]) > 0:
                for j in range(len(wilde_spells[i])):
                    spells[i][j].extend(wilde_spells[i][j])
                    spells[i][j] = list(set(spells[i][j]))
                    spells[i][j].sort()

class Witchlight(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "The Wild Beyond the Witchlight"
        self.races = [Fairy(), Harengon()]

PHB = PHB()
SCAG = SCAG()
EE = EE()
VGtM = VGtM()
MToF = MToF()
XGtE = XGtE()
TCoE = TCoE()
FToD = FToD()
GotG = GotG()
Eberron = Eberron()
Ravnica = Ravnica()
Theros = Theros()
Strixhaven = Strixhaven()
Wildemount = Wildemount()
Witchlight = Witchlight()
