from races.phb_races import (Dwarf, Elf, Halfling, Human, Human_Variant, Dragonborn, Gnome, Half_Elf, Half_Orc, Tiefling,
                   Hill_Dwarf, Mountain_Dwarf, High_Elf, Wood_Elf, Drow, Lightfoot_Halfling, Stout_Halfling, Forest_Gnome, Rock_Gnome)
from races.scag_races import Duergar, Svirfneblin, Half_Elf_Variant, Tiefling_Variant
from races.ee_races import (Aarakocra, Genasi, Goliath,
                            Air_Genasi, Earth_Genasi, Fire_Genasi, Water_Genasi)
from jobs import Barbarian
from char_values import PC


def choose_books():
    print('Which source books do you have available? [Choose all that apply, eg "1, 5, 6" if you want to pick the PHB, XGtE and TCoE]')
    print(f"[1] - {PHB.title}\n[2] - {SCAG.title}\n[3] - {EE.title}\n[4] - {RR.title}\n[5] - {XGtE.title}\n[6] - {TCoE.title}\n[7] - {FToD.title}\n[8] - {GotG.title}")
    
    PC.books = []

    inp = str.lower(input())
    if "1" in inp:
        PC.books.append(PHB)
    if "2" in inp:
        PC.books.append(SCAG)
    if "3" in inp:
        PC.books.append(EE)
    if "4" in inp:
        PC.books.append(RR)
    if "5" in inp:
        PC.books.append(XGtE)
    if "6" in inp:
        PC.books.append(TCoE)
    if "7" in inp:
        PC.books.append(FToD)
    if "8" in inp:
        PC.books.append(GotG)

    print(f"Books selected: {get_book_titles()}")
    apply_subraces(PC.books)
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
        self.feats = []
        self.spells = []
        self.bgrounds = []

class PHB(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Player's Handbook"
        self.races = [Dwarf(), Elf(), Halfling(), Human(), Human_Variant(), Dragonborn(), Gnome(), Half_Elf(), Half_Orc(), Tiefling()]
        self.subraces = [Hill_Dwarf(), Mountain_Dwarf(), High_Elf(), Wood_Elf(), Drow(), Lightfoot_Halfling(), Stout_Halfling(), Forest_Gnome(), Rock_Gnome()]
        self.jobs = [Barbarian()]

class SCAG(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Sword Coast Adventurer's Guide"
        self.races = [Dwarf(), Gnome(), Half_Elf_Variant(), Tiefling_Variant()]
        self.subraces = [Duergar(), Svirfneblin()]
        self.jobs = []

class EE(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Elemental Evil Player's Companion"
        self.races = [Aarakocra(), Genasi(), Goliath()]
        self.subraces = [Svirfneblin(), Air_Genasi(), Earth_Genasi(), Fire_Genasi(), Water_Genasi()]

class RR(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Revised Ranger"

class XGtE(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Xanathar's Guide to Everything"

class TCoE(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Tasha's Cauldron of Everything"

class FToD(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Fizban's Treasury of Dragons"

class GotG(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Bigby Presents: Glory of the Giants"

PHB = PHB()
SCAG = SCAG()
EE = EE()
RR = RR()
XGtE = XGtE()
TCoE = TCoE()
FToD = FToD()
GotG = GotG()
