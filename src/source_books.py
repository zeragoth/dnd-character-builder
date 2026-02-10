from races import (Dwarf, Elf, Halfling, Human, Human_Variant, Dragonborn, Gnome, Half_Elf, Half_Orc, 
                   Tiefling)
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
    return

def get_book_titles():
    book_titles = []
    for i in range(len(PC.books)):
        book_titles.append(PC.books[i].title)
    return book_titles



class Source_Book:
    def __init__(self):
        super().__init__()
        self.title = "none"
        self.races = []
        self.jobs = []
        self.feats = []
        self.spells = []
        self.bgrounds = []

class Player_Handbook(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Player's Handbook"
        self.races = [Dwarf(), Elf(), Halfling(), Human(), Human_Variant(), Dragonborn(), Gnome(), Half_Elf(), Half_Orc(), Tiefling()]
        self.jobs = [Barbarian()]

class Sword_Coast_Adventurer_Guide(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Sword Coast Adventurer's Guide"

class Elemental_Evil_Player_Companion(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Elemental Evil Player's Companion"

class Revised_Ranger(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Revised Ranger"

class Xanathar_Guide_to_Everything(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Xanathar's Guide to Everything"

class Tasha_Cauldron_of_Everything(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Tasha's Cauldron of Everything"

class Fizban_Treasury_of_Dragons(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Fizban's Treasury of Dragons"

class Glory_of_the_Giants(Source_Book):
    def __init__(self):
        super().__init__()
        self.title = "Bigby Presents: Glory of the Giants"

PHB = Player_Handbook()
SCAG = Sword_Coast_Adventurer_Guide()
EE = Elemental_Evil_Player_Companion()
RR = Revised_Ranger()
XGtE = Xanathar_Guide_to_Everything()
TCoE = Tasha_Cauldron_of_Everything()
FToD = Fizban_Treasury_of_Dragons()
GotG = Glory_of_the_Giants()
