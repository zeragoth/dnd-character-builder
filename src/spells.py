# Contains class spell lists from every source book,
# as well as combined lists of the spells from every source book selected by the user via source_books.choose_books().
# This generally shouldn't be tampered with, unless adding a new source book,
# or undertaking the monstrous task of converting all spells from strings into classes.

from char_values import PC


artificer_spells = [[],[],[],[],[],[]]
bard_spells = [[],[],[],[],[],[],[],[],[],[]]
cleric_spells = [[],[],[],[],[],[],[],[],[],[]]
druid_spells = [[],[],[],[],[],[],[],[],[],[]]
paladin_spells = [[],[],[],[],[],[]]
ranger_spells = [[],[],[],[],[],[]]
sorcerer_spells = [[],[],[],[],[],[],[],[],[],[]]
warlock_spells = [[],[],[],[],[],[],[],[],[],[]]
wizard_spells = [[],[],[],[],[],[],[],[],[],[]]

spells = [artificer_spells, bard_spells, cleric_spells, druid_spells, paladin_spells, ranger_spells, sorcerer_spells, warlock_spells, wizard_spells]


def spellbook():
    if len(PC.spells[0]) == 0 and len(PC.spells[1]) == 0 and len(PC.race.spells[0]) == 0 and len(PC.race.spells[1]) == 0 and len(PC.race.spells[2]) == 0:
        print("\nYou don't know any spells!\n\n[Enter] - return to menu")
        if input() == "exit":
            quit()
        else:
            return

    print("\nKnown Spells:")
    for i in range(len(PC.spells)):
        spells = list(set(PC.spells[i].copy() + PC.race.spells[i].copy()))
        spells.sort()
        if len(spells) > 0:
            if i == 0:
                print("--- Cantrips ---")
            elif i == 1:
                print("\n--- 1st Level ---")
            elif i == 2:
                print("\n--- 2nd Level ---")
            elif i == 3:
                print("\n--- 3rd Level ---")
            else:
                print(f"\n--- {i}th Level ---")
            for spell in spells:
                print(f"- {spell}")
    print("\n[Enter] - return to menu")
    if input() == "exit":
        quit()
    else:
        return
    



# Player's Handbook

phb_bard_spells = [["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigitation", "True Strike", "Vicious Mockery"],
                   ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic", "Disguise Self", "Dissonant Whispers", "Faerie Fire", "Feather Fall", "Healing Word", "Heroism", "Tasha's Hideous Laughter", "Thunderwave", "Unseen Servant"],
                   ["Animal Messenger", "Blindness/Deafness", "Calm Emotions", "Cloud of Daggers", "Crown of Madness", "Detect Thoughts", "Enhance Ability", "Enthrall", "Heat Metal", "Hold Person", "Invisibility", "Knock", "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Magic Mouth", "Phantasmal Force", "See Invisibility", "Shatter", "Silence", "Suggestion", "Zone of Truth"],
                   ["Bestow Curse", "Clairvoyance", "Dispel Magic", "Fear", "Feign Death", "Glyph of Warding", "Hypnotic Pattern", "Leomund's Tiny Hut", "Major Image", "Nondetection", "Plant Growth", "Sending", "Speak with Dead", "Speak with Plants", "Stinking Cloud", "Tongues"],
                   ["Compulsion", "Confusion", "Dimension Door", "Freedom of Movement", "Greater Invisibility", "Hallucinatory Terrain", "Locate Creature", "Polymorph"],
                   ["Animate Objects", "Awaken", "Dominate Person", "Dream", "Geas", "Greater Restoration", "Hold Monster", "Legend Lore", "Mass Cure Wounds", "Mislead", "Modify Memory", "Planar Binding", "Raise Dead", "Scrying", "Seeming", "Teleportation Circle"],
                   ["Eyebite", "Find the Path", "Guards and Wards", "Mass Suggestion", "Otto's Irresistible Dance", "Programmed Illusion", "True Seeing"],
                   ["Etherealness", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", "Project Image", "Regenerate", "Resurrection", "Symbol", "Teleport"],
                   ["Dominate Monster", "Feeblemind", "Glibness", "Mind Blank", "Power Word Stun"],
                   ["Foresight", "Power Word Heal", "Power Word Kill", "True Polymorph"]]

phb_cleric_spells = [["Guidance", "Light", "Mending", "Resistance", "Sacred Flame", "Spare the Dying", "Thaumaturgy"],
                     ["Bane", "Bless", "Command", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Guiding Bolt", "Healing Word", "Inflict Wounds",  "Protection from Evil and Good", "Purify Food and Drink", "Sanctuary", "Shield of Faith"],
                     ["Aid", "Augury", "Blindness/Deafness", "Calm Emotions", "Continual Flame", "Enhance Ability", "Find Traps", "Gentle Repose", "Hold Person", "Lesser Restoration", "Locate Object", "Prayer of Healing", "Protection from Poison", "Silence", "Spiritual Weapon", "Warding Bond", "Zone of Truth"],
                     ["Animate Dead", "Beacon of Hope", "Bestow Curse", "Clairvoyance", "Create Food and Water", "Daylight", "Dispel Magic", "Feign Death", "Glyph of Warding", "Magic Circle", "Mass Healing Word", "Meld into Stone", "Protection from Energy", "Remove Curse", "Revivify", "Sending", "Speak with Dead", "Spirit Guardians", "Tongues", "Water Walk"],
                     ["Banishment", "Control Water", "Death Ward", "Divination", "Freedom of Movement", "Guardian of Faith", "Locate Creature", "Stone Shape"],
                     ["Commune", "Contagion", "Dispel Evil and Good", "Flame Strike", "Geas", "Greater Restoration", "Hallow", "Insect Plague", "Legend Lore", "Mass Cure Wounds", "Planar Binding", "Raise Dead", "Scrying"],
                     ["Blade Barrier", "Create Undead", "Find the Path", "Forbiddance", "Harm", "Heal", "Heroes' Feast", "Planar Ally", "True Seeing", "Word of Recall"],
                     ["Conjure Celestial", "Divine Word", "Etherealness", "Fire Storm", "Plane Shift", "Regenerate", "Resurrection", "Symbol"],
                     ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura"],
                     ["Astral Projection", "Gate", "Mass Heal", "True Resurrection"]]

phb_druid_spells = [["Druidcraft", "Guidance", "Mending", "Poison Spray", "Produce Flame", "Resistance", "Shillelagh", "Thorn Whip"],
                    ["Animal Friendship", "Charm Person", "Create or Destroy Water", "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Entangle", "Faerie Fire", "Fog Cloud", "Goodberry", "Healing Word", "Jump", "Longstrider", "Purify Food and Drink", "Speak with Animals", "Thunderwave"],
                    ["Animal Messenger", "Barkskin", "Beast Sense", "Darkvision", "Enhance Ability", "Find Traps", "Flame Blade", "Flaming Sphere", "Gust of Wind", "Heat Metal", "Hold Person", "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Moonbeam", "Pass without Trace", "Protection from Poison", "Spike Growth"],
                    ["Call Lightning", "Conjure Animals", "Daylight", "Dispel Magic", "Feign Death", "Meld into Stone", "Plant Growth", "Protection from Energy", "Sleet Storm", "Speak with Plants", "Water Breathing", "Water Walk", "Wind Wall"],
                    ["Blight", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings", "Control Water", "Dominate Beast", "Freedom of Movement", "Giant Insect", "Grasping Vine", "Hallucinatory Terrain", "Ice Storm", "Locate Creature", "Polymorph", "Stone Shape", "Stoneskin", "Wall of Fire"],
                    ["Antilife Shell", "Awaken", "Commune with Nature", "Conjure Elemental", "Contagion", "Geas", "Greater Restoration", "Insect Plague", "Mass Cure Wounds", "Planar Binding", "Reincarnate", "Scrying", "Tree Stride", "Wall of Stone"],
                    ["Conjure Fey", "Find the Path", "Heal", "Heroes' Feast", "Move Earth", "Sunbeam", "Transport via Plants", "Wall of Thorns", "Wind Walk"],
                    ["Fire Storm", "Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity"],
                    ["Animal Shapes", "Antipathy/Sympathy", "Control Weather", "Earthquake", "Feeblemind", "Sunburst", "Tsunami"],
                    ["Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection"]]

phb_paladin_spells = [[],
                      ["Bless", "Command", "Compelled Duel", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Divine Favor", "Heroism", "Protection from Evil and Good", "Purify Food and Drink", "Searing Smite", "Shield of Faith", "Thunderous Smite", "Wrathful Smite"],
                      ["Aid", "Branding Smite", "Find Steed", "Lesser Restoration", "Locae Object", "Magic Weapon", "Protection from Poison", "Zone of Truth"],
                      ["Aura of Vitality", "Blinding Smite", "Create Food and Water", "Crusader's Mantle", "Daylight", "Dispel Magic", "Elemental Weapon", "Magic Circle", "Remove Curse", "Revivify"],
                      ["Aura of Life", "Aura of Purity", "Banishment", "Death Ward", "Locate Creature", "Staggering Smite"],
                      ["Banishing Smite", "Circle of Power", "Destructive Wave", "Dispel Evil and Good", "Geas", "Raise Dead"]]

phb_ranger_spells = [[],
                     ["Alarm", "Animal Friendship", "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Ensnaring Strike", "Fog Cloud", "Goodberry", "Hail of Thorns", "Hunter's Mark", "Jump", "Longstrider", "Speak with Animals"],
                     ["Animal Messenger", "Barkskin", "Beast Sense", "Cordon of Arrows", "Darkvision", "Find Traps", "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Pass without Trace", "Protection from Poison", "Silence", "Spike Growth"],
                     ["Conjure Animals", "Conjure Barrage", "Daylight", "Lightning Arrow", "Nondetection", "Plant Growth", "Protection from Energy", "Speak with Plants", "Water Breathing", "Water Walk", "Wind Wall"],
                     ["Conjure Woodland Beings", "Freedom of Movement", "Grasping Vine", "Locate Creature", "Stoneskin"],
                     ["Commune with Nature", "Conjure Volley", "Swift Quiver", "Tree Stride"]]

phb_sorcerer_spells = [["Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights", "Fire Bolt", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"],
                       ["Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", "Fog Cloud", "Jump", "Mage Armor", "Magic Missile", "Ray of Sickness", "Shield", "Silent Image", "Sleep", "Thunderwave", "Witch Bolt"],
                       ["Alter Self", "Blindness/Deafness", "Blur", "Cloud of Daggers", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Enhance Ability", "Enlarge/Reduce", "Gust of Wind", "Hold Person", "Invisibility", "Knock", "Levitate", "Mirror Image", "Misty Step", "Phantasmal Force", "Scorching Ray", "See Invisibility", "Shatter", "Spider Climb", "Suggestion", "Web"],
                       ["Blink", "Clairvoyance", "Counterspell", "Daylight", "Dispel Magic", "Fear", "Fireball", "Fly", "Gaseous Form", "Haste", "Hypnotic Pattern", "Lightning Bolt", "Major Image", "Protection from Energy", "Sleet Storm", "Slow", "Stinking Cloud", "Tongues", "Water Breathing", "Water Walk"],
                       ["Banishment", "Blight", "Confusion", "Dimension Door", "Dominate Beast", "Greater Invisibility", "Ice Storm", "Polymorph", "Stoneskin", "Wall of Fire"],
                       ["Animate Objects", "Cloudkill", "Cone of Cold", "Creation", "Dominate Person", "Hold Monster", "Insect Plague", "Seeming", "Telekinesis", "Teleportation Circle", "Wall of Stone"],
                       ["Arcane Gate", "Chain Lightning", "Circle of Death", "Disintegrate", "Eyebite", "Globe of Invulnerability", "Mass Suggestion", "Move Earth", "Sunbeam", "True Seeing"],
                       ["Delayed Blast Fireball", "Etherealness", "Finger of Death", "Fire Storm", "Plane Shift", "Prismatic Spray", "Reverse Gravity", "Teleport"],
                       ["Dominate Monster", "Earthquake", "Incendiary Cloud", "Power Word Stun", "Sunburst"],
                       ["Gate", "Meteor Swarm", "Power Word Kill", "Time Stop", "Wish"]]

phb_warlock_spells = [["Blade Ward", "Chill Touch", "Eldritch Blast", "Friends", "Mage Hand", "Minor Illusion", "Poison Spray", "Prestidigitation", "True Strike"],
                      ["Armor of Agathys", "Arms of Hadar", "Charm Person", "Comprehend Languages", "Expeditious Retreat", "Hellish Rebuke", "Hex", "Illusory Script", "Protection from Evil and Good", "Unseen Servant", "Witch Bolt"],
                      ["Cloud of Daggers", "Crown of Madness", "Darkness", "Enthrall", "Hold Person", "Invisibility", "Mirror Image", "Misty Step", "Ray of Enfeeblement", "Shatter", "Spider Climb", "Suggestion"],
                      ["Counterspell", "Dispel Magic", "Fear", "Fly", "Gaseous Form", "Hunger of Hadar", "Hypnotic Pattern", "Magic Circle", "Major Image", "Remove Curse", "Tongues", "Vampiric Touch"],
                      ["Banishment", "Blight", "Dimension Door", "Hallucinatory Terrain"],
                      ["Contact Other Plane", "Dream", "Hold Monster", "Scrying"],
                      ["Arcane Gate", "Circle of Death", "Conjure Fey", "Create Undead", "Eyebite", "Flesh to Stone", "Mass Suggestion", "True Seeing"],
                      ["Etherealness", "Finger of Death", "Forcecage", "Plane Shift"],
                      ["Demiplane", "Dominate Monster", "Feeblemind", "Glibness", "Power Word Stun"],
                      ["Astral Projection", "Foresight", "Imprisonment", "Power Word Kill", "True Polymorph"]]

phb_wizard_spells = [["Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights", "Fire Bolt", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"],
                     ["Alarm", "Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Grease", "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Ray of Sickness", "Shield", "Silent Image", "Sleep", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"],
                     ["Alter Self", "Arcane Lock", "Blindness/Deafness", "Blur", "Cloud of Daggers", "Continual Flame", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Enlarge/Reduce", "Flaming Sphere", "Gentle Repose", "Gust of Wind", "Hold Person", "Invisibility", "Knock", "Levitate", "Locate Object", "Magic Mouth", "Magic Weapon", "Melf's Acid Arrow", "Mirror Image", "Misty Step", "Nystul's Magic Aura", "Phantasmal Force", "Ray of Enfeeblement", "Rope Trick", "Scorching Ray", "See Invisibility", "Shatter", "Spider Climb", "Suggestion", "Web"],
                     ["Animate Dead", "Bestow Curse", "Blink", "Clairvoyance", "Counterspell", "Dispel Magic", "Fear", "Feign Death", "Fireball", "Fly", "Gaseous Form", "Glyph of Warding", "Haste", "Hypnotic Pattern", "Leomund's Tiny Hut", "Lightning Bolt", "Magic Circle", "Major Image", "Nondetection", "Phantom Steed", "Protection from Energy", "Remove Curse", "Sending", "Sleet Storm", "Slow", "Stinking Cloud", "Tongues", "Vampiric Touch", "Water Breathing"],
                     ["Arcane Eye", "Banishment", "Blight", "Confusion", "Conjure Minor Elementals", "Control Water", "Dimension Door", "Evard's Black Tentacles", "Fabricate", "Fire Shield", "Greater Invisibility", "Hallucinatory Terrain", "Ice Storm", "Leomund's Secret Chest", "Locate Creature", "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Phantasmal Killer", "Polymorph", "Stone Shape", "Stoneskin", "Wall of Fire"],
                     ["Animate Objects", "Bigby's Hand", "Cloudkill", "Cone of Cold", "Conjure Elemental", "Contact Other Plane", "Creation", "Dominate Person", "Dream", "Geas", "Hold Monster", "Legend Lore", "Mislead", "Modify Memory", "Passwall", "Planar Binding", "Rary's Telepathic Bond", "Scrying", "Seeming", "Telekinesis", "Teleportation Circle", "Wall of Force", "Wall of Stone"],
                     ["Arcane Gate", "Chain Lightning", "Circle of Death", "Contingency", "Create Undead", "Disintegrate", "Drawmij's Instant Summon", "Eyebite", "Flesh to Stone", "Globe of Invulnerability", "Guards and Wards", "Magic Jar", "Mass Suggestion", "Move Earth", "Otiluke's Freezing Sphere", "Otto's Irresistable Dance", "Programmed Illusion", "Sunbeam", "True Seeing", "Wall of Ice"],
                     ["Delayed Blast Fireball", "Etherealness", "Finger of Death", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", "Plane Shift", "Prismatic Spray", "Project Image", "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport"],
                     ["Antimagic Field", "Anitpathy/Sympathy", "Clone", "Control Weather", "Demiplane", "Dominate Monster", "Feeblemind", "Incendiary Cloud", "Maze", "Mind Blank", "Power Word Stun", "Sunburst", "Telepathy"],
                     ["Astral Projection", "Foresight", "Gate", "Imprisonment", "Meteor Swarm", "Power Word Kill", "Prismatic Wall", "Shapechange", "Time Stop", "True Polymorph", "Weird", "Wish"]]


phb_spells = [[], phb_bard_spells, phb_cleric_spells, phb_druid_spells, phb_paladin_spells, phb_ranger_spells, phb_sorcerer_spells, phb_warlock_spells, phb_wizard_spells]


# Sword Coast Adventurer's Guide

scag_sorcerer_spells = [["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Sword Burst"]]
scag_warlock_spells = [["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Sword Burst"]]
scag_wizard_spells = [["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Sword Burst"]]


scag_spells = [[],[],[],[],[],[], scag_sorcerer_spells, scag_warlock_spells, scag_wizard_spells]


# Elemental Evil Player's Companion

ee_artificer_spells = [["Create Bonfire", "Frostbite", "Magic Stone", "Thunderclap"],
                       ["Absorb Elements", "Catapult"],
                       ["Pyrotechnics", "Skywrite"],
                       ["Flame Arrows"],
                       ["Elemental Bane"],
                       ["Transmute Rock"]]

ee_bard_spells = [["Thunderclap"],
                  ["Earth Tremor"],
                  ["Pyrotechnics", "Skywrite", "Warding Wind"]]

ee_druid_spells = [["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Magic Stone", "Mold Earth", "Shape Water", "Thunderclap"],
                   ["Absorb Elements", "Beast Bond", "Ice Knife", "Earth Tremor"],
                   ["Dust Devil", "Earthbind", "Skywrite", "Warding Wind"],
                   ["Erupting Earth", "Flame Arrows", "Tidal Wave", "Wall of Water"],
                   ["Elemental Bane", "Watery Sphere"],
                   ["Control Winds", "Maelstrom", "Transmute Rock"],
                   ["Bones of the Earth", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Primordial Ward"],
                   ["Whirlwind"]]

ee_ranger_spells = [[],
                    ["Absorb Elements", "Beast Bond"],
                    [],
                    ["Flame Arrows"]]

ee_sorcerer_spells = [["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Mold Earth", "Shape Water", "Thunderclap"],
                      ["Catapult", "Ice Knife", "Earth Tremor"],
                      ["Aganazzar's Scorcher", "Dust Devil", "Earthbind", "Maximilian's Earthen Grasp", "Pyrotechnics", "Snilloc's Snowball Swarm", "Warding Wind"],
                      ["Erupting Earth", "Flame Arrows", "Melf's Minute Meteors", "Wall of Water"],
                      ["Storm Sphere", "Vitriolic Sphere", "Watery Sphere"],
                      ["Control Winds", "Immolation"],
                      ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind"],
                      [],
                      ["Abi-Dalzim's Horrid Wilting"]]

ee_warlock_spells = [["Create Bonfire", "Frostbite", "Magic Stone", "Thunderclap"],
                     [],
                     ["Earthbind"],
                     [],
                     ["Elemental Bane"],
                     [],
                     ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind"]]

ee_wizard_spells = [["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Mold Earth", "Shape Water", "Thunderclap"],
                    ["Absorb Elements", "Catapult", "Ice Knife", "Earth Tremor"],
                    ["Aganazzar's Scorcher", "Dust Devil", "Earthbind", "Maximilian's Earthen Grasp", "Pyrotechnics", "Skywrite", "Snilloc's Snowball Swarm"],
                    ["Erupting Earth", "Flame Arrows", "Melf's Minute Meteors", "Tidal Wave", "Wall of Sand", "Wall of Water"],
                    ["Elemental Bane", "Storm Sphere", "Vitriolic Sphere", "Watery Sphere"],
                    ["Control Winds", "Immolation", "Transmute Rock"],
                    ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind"],
                    ["Whirlwind"],
                    ["Abi-Dalzim's Horrid Wilting"]]


ee_spells = [ee_artificer_spells, ee_bard_spells, [], ee_druid_spells, [], ee_ranger_spells, ee_sorcerer_spells, ee_warlock_spells, ee_wizard_spells]


# Xanathar's Guide to Everything

xgte_artificer_spells = [["Create Bonfire", "Frostbite", "Magic Stone", "Thunderclap"],
                         ["Absorb Elements", "Catapult", "Snare"],
                         ["Pyrotechnics", "Skywrite"],
                         ["Catnap", "Flame Arrows", "Tiny Servant"],
                         ["Elemental Bane"],
                         ["Skill Empowerment", "Transmute Rock"]]

xgte_bard_spells = [["Thunderclap"],
                    ["Earth Tremor"],
                    ["Pyrotechnics", "Skywrite", "Warding Wind"],
                    ["Catnap", "Enemies Abound"],
                    ["Charm Monster"],
                    ["Skill Empowerment", "Synaptic Static"],
                    [],
                    [],
                    [],
                    ["Mass Polymorph", "Psychic Scream"]]

xgte_cleric_spells = [["Toll the Dead", "Word of Radiance"],
                      ["Ceremony"],
                      [],
                      ["Life Transference"],
                      [],
                      ["Dawn", "Holy Weapon"],
                      [],
                      ["Temple of the Gods"]]

xgte_druid_spells = [["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Infestation", "Magic Stone", "Mold Earth", "Primal Savagery", "Shape Water", "Thunderclap"],
                     ["Absorb Elements", "Beast Bond", "Earth Tremor", "Ice Knife", "Snare"],
                     ["Dust Devil", "Earthbind", "Healing Spirit", "Skywrite", "Warding Wind"],
                     ["Erupting Earth", "Flame Arrows", "Tidal Wave", "Wall of Water"],
                     ["Charm Monster", "Elemental Bane", "Guardian of Nature", "Watery Sphere"],
                     ["Control Winds", "Maelstrom", "Transmute Rock", "Wrath of Nature"],
                     ["Bones of the Earth", "Druid Grove", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Primordial Ward"],
                     ["Whirlwind"]]

xgte_paladin_spells = [[],
                       ["Ceremony"],
                       [],
                       [],
                       ["Find Greater Steed"],
                       ["Holy Weapon"]]

xgte_ranger_spells = [[],
                      ["Absorb Elements", "Beast Bond", "Snare", "Zephyr Strike"],
                      ["Healing Spirit"],
                      ["Flame Arrows"],
                      ["Guardian of Nature"],
                      ["Steel Wind Strike", "Wrath of Nature"]]

xgte_sorcerer_spells = [["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Infestation", "Mold Earth", "Shape Water", "Thunderclap"],
                        ["Absorb Elements", "Catapult", "Chaos Bolt", "Earth Tremor", "Ice Knife"],
                        ["Aganazzar's Scorcher", "Dragon's Breath", "Dust Devil", "Earthbind", "Maximilian's Earthen Grasp", "Mind Spike", "Pyrotechnics", "Shadow Blade", "Snilloc's Snowball Swarm", "Warding Wind"],
                        ["Catnap", "Enemies Abound", "Erupting Earth", "Flame Arrows", "Melf's Minute Meteors", "Thunder Step", "Tidal Wave", "Wall of Water"],
                        ["Charm Monster", "Sickening Radiance", "Storm Sphere", "Vitriolic Sphere", "Watery Sphere"],
                        ["Control Winds", "Enervation", "Far Step", "Immolation", "Skill Empowerment", "Synaptic Static", "Wall of Light"],
                        ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Mental Prison", "Scatter"],
                        ["Crown of Stars", "Power Word Pain", "Whirlwind"],
                        ["Abi-Dalzim's Horrid Wilting"],
                        ["Mass Polymorph", "Psychic Scream"]]

xgte_warlock_spells = [["Create Bonfire", "Frostbite", "Infestation", "Magic Stone", "Thunderclap", "Toll the Dead"],
                       ["Cause Fear"],
                       ["Earthbind", "Mind Spike", "Shadow Blade"],
                       ["Enemies Abound", "Thunder Step", "Summon Lesser Demons"],
                       ["Charm Monster", "Elemental Bane", "Shadow of Moil", "Sickening Radiance", "Summon Greater Demon"],
                       ["Danse Macabre", "Enervation", "Far Step", "Infernal Calling", "Negative Energy Flood", "Synaptic Static", "Wall of Light"],
                       ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Mental Prison", "Scatter", "Soul Cage"],
                       ["Crown of Stars", "Power Word Pain"],
                       ["Maddening Darkness"],
                       ["Psychic Scream"]]

xgte_wizard_spells = [["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Infestation", "Mold Earth", "Shape Water", "Thunderclap", "Toll the Dead"],
                      ["Absorb Elements", "Catapult", "Cause Fear", "Earth Tremor", "Ice Knife", "Snare"],
                      ["Aganazzar's Scorcher", "Dragon's Breath", "Dust Devil", "Earthbind", "Maximilian's Earthen Grasp", "Mind Spike", "Pyrotechnics", "Shadow Blade", "Skywrite", "Snilloc's Snowball Swarm", "Warding Wind"],
                      ["Catnap", "Enemies Abound", "Erupting Earth", "Flame Arrows", "Life Transference", "Melf's Minute Meteors", "Summon Lesser Demons", "Thunder Step", "Tidal Wave", "Tiny Servant", "Wall of Sand", "Wall of Water"],
                      ["Charm Monster", "Elemental Bane", "Sickening Radiance", "Storm Sphere", "Summon Greater Demon", "Vitriolic Sphere", "Watery Sphere"],
                      ["Control Winds", "Danse Macabre", "Dawn", "Enervation", "Far Step", "Immolation", "Infernal Calling", "Negative Energy Flood", "Skill Empowerment", "Steel Wind Strike", "Synaptic Static", "Transmute Rock", "Wall of Light"],
                      ["Create Homunculus", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Mental Prison", "Scatter", "Soul Cage", "Tenser's Transformation"],
                      ["Crown of Stars", "Power Word Pain", "Whirlwind"],
                      ["Abi-Dalzim's Horrid Wilting", "Illusory Dragon", "Maddening Darkness", "Mighty Fortress"],
                      ["Invulnerability", "Mass Polymorph", "Psychic Scream"]]


xgte_spells = [xgte_artificer_spells, xgte_bard_spells, xgte_cleric_spells, xgte_druid_spells, xgte_paladin_spells, xgte_ranger_spells, xgte_sorcerer_spells, xgte_warlock_spells, xgte_wizard_spells]


# Tasha's Cauldron of Everything

tcoe_artificer_spells = [["Acid Splash", "Booming Blade", "Dancing Lights", "Fire Bolt", "Green-Flame Blade", "Guidance", "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Poison Spray", "Prestidigitation", "Ray of Frost", "Resistance", "Shocking Grasp", "Spare the Dying", "Sword Burst", "Thorn Whip"],
                         ["Alarm", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Grease", "Identify", "Jump", "Longstrider", "Purify Food and Drink", "Sanctuary", "Tasha's Caustic Brew"],
                         ["Aid", "Alter Self", "Arcane Lock", "Blur", "Continual Flame", "Darkvision", "Enhance Ability", "Enlarge/Reduce", "Heat Metal", "Invisibility", "Lesser Restoration", "Levitate", "Magic Mouth", "Magic Weapon", "Protection from Poison", "Rope Trick", "See Invisibility", "Spider Climb", "Web"],
                         ["Blink", "Create Food and Water", "Dispel Magic", "Elemental Weapon", "Fly", "Glyph of Warding", "Haste", "Intellect Fortress", "Protection from Energy", "Revivify", "Water Breathing", "Water Walk"],
                         ["Arcane Eye", "Fabricate", "Freedom of Movement", "Leomund's Secret Chest", "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Stone Shape", "Stoneskin", "Summon Construct"],
                         ["Animate Objects", "Bigby's Hand", "Creation", "Greater Restoration", "Wall of Stone"]]

tcoe_bard_spells = [[],
                    ["Color Spray", "Command"],
                    ["Aid", "Enlarge/Reduce", "Mirror Image"],
                    ["Intellect Fortress", "Mass Healing Word", "Slow"],
                    ["Phantasmal Killer"],
                    ["Rary's Telepathic Bond"],
                    ["Heroes' Feast"],
                    ["Dream of the Blue Veil", "Prismatic Spray"],
                    ["Antipathy/Sympathy"],
                    ["Prismatic Wall"]]

tcoe_cleric_spells = [[],
                      [],
                      [],
                      ["Aura of Vitality", "Spirit Shroud"],
                      ["Aura of Life", "Aura of Purity"],
                      ["Summon Celestial"],
                      ["Sunbeam"],
                      [],
                      ["Sunburst"],
                      ["Power Word Heal"]]

tcoe_druid_spells = [[],
                     ["Protection from Evil and Good"],
                     ["Augury", "Continual Flame", "Enlarge/Reduce", "Summon Beast"],
                     ["Aura of Vitality", "Elemental Weapon", "Revivify", "Summon Fey"],
                     ["Divination", "Fire Shield", "Summon Elemental"],
                     ["Cone of Cold"],
                     ["Flesh to Stone"],
                     ["Symbol"],
                     ["Incendiary Cloud"]
                     ]

tcoe_paladin_spells = [[],
                       [],
                       ["Gentle Repose", "Prayer of Healing", "Warding Bond"],
                       ["Spirit Shroud"],
                       [],
                       ["Summon Celestial"]]

tcoe_ranger_spells = [[],
                      ["Entangle", "Searing Smite"],
                      ["Aid", "Enhance Ability", "Gust of Wind", "Magic Weapon", "Summon Beast"],
                      ["Elemental Weapon", "Meld into Stone", "Revivify", "Summon Fey"],
                      ["Dominate Beast", "Summon Elemental"],
                      ["Greater Restoration"]]

tcoe_sorcerer_spells = [["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Mind Sliver", "Sword Burst"],
                        ["Grease", "Tasha's Caustic Brew"],
                        ["Flame Blade", "Flaming Sphere", "Magic Weapon", "Tasha's Mind Whip"],
                        ["Intellect Fortress", "Vampiric Touch"],
                        ["Fire Shield"],
                        ["Bigby's Hand"],
                        ["Flesh to Stone", "Otiluke's Freezing Sphere", "Tasha's Otherworldly Guise"],
                        ["Dream of the Blue Veil"],
                        ["Demiplane"],
                        ["Blade of Disaster"]]

tcoe_warlock_spells = [["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Mind Sliver", "Sword Burst"],
                       [],
                       [],
                       ["Intellect Fortress", "Spirit Shroud", "Summon Fey", "Summon Shadowspawn", "Summon Undead"],
                       ["Summon Aberration"],
                       ["Mislead", "Planar Binding", "Teleportation Circle"],
                       ["Summon Fiend", "Tasha's Otherworldly Guise"],
                       ["Dream of the Blue Veil"],
                       [],
                       ["Blade of Disaster", "Gate", "Weird"]]

tcoe_wizard_spells = [["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Mind Sliver", "Sword Burst"],
                      ["Tasha's Caustic Brew"],
                      ["Augury", "Enhance Ability", "Tasha's Mind Whip"],
                      ["Intellect Fortress", "Speak with Dead", "Spirit Shroud", "Summon Fey", "Summon Shadowspawn", "Summon Undead"],
                      ["Divination", "Summon Aberration", "Summon Construct", "Summon Elemental"],
                      [],
                      ["Summon Fiend", "Tasha's Otherworldly Guise"],
                      ["Dream of the Blue Veil"],
                      [],
                      ["Blade of Disaster"]]


tcoe_spells = [tcoe_artificer_spells, tcoe_bard_spells, tcoe_cleric_spells, tcoe_druid_spells, tcoe_paladin_spells, tcoe_ranger_spells, tcoe_sorcerer_spells, tcoe_warlock_spells, tcoe_wizard_spells]


# Fizban's Treasury of Dragons

ftod_artificer_spells = [[],
                         [],
                         [],
                         ["Ashardalon's Stride"]]

ftod_bard_spells = [[],
                    [],
                    ["Nathair's Mischief"],
                    [],
                    ["Raulothim's Psychic Lance"]]

ftod_druid_spells = [[],
                     [],
                     [],
                     [],
                     [],
                     ["Summon Draconic Spirit"],
                     [],
                     ["Draconic Transformation"]]

ftod_ranger_spells = [[],
                      [],
                      [],
                      ["Ashardalon's Stride"]]

ftod_sorcerer_spells = [[],
                        [],
                        ["Nathair's Mischief", "Rime's Binding Ice"],
                        ["Ashardalon's Stride"],
                        ["Raulothim's Psychic Lance"],
                        ["Summon Draconic Spirit"],
                        ["Fizban's Platinum Shield"],
                        ["Draconic Transformation"]]

ftod_warlock_spells = [[],
                       [],
                       [],
                       [],
                       ["Raulothim's Psychic Lance"]]

ftod_wizard_spells = [[],
                      [],
                      ["Nathair's Mischief", "Rime's Binding Ice"],
                      ["Ashardalon's Stride"],
                      ["Raulothim's Psychic Lance"],
                      ["Summon Draconic Spirit"],
                      ["Fizban's Platinum Shield"],
                      ["Draconic Transformation"]]


ftod_spells = [ftod_artificer_spells, ftod_bard_spells, [], ftod_druid_spells, [], ftod_ranger_spells, ftod_sorcerer_spells, ftod_warlock_spells, ftod_wizard_spells]


# Eberron: Rising from the Last War

eberron_artificer_spells = [["Acid Splash", "Dancing Lights", "Fire Bolt", "Guidance", "Light", "Mage Hand", "Mending", "Message", "Poison Spray", "Prestidigitation", "Ray of Frost", "Resistance", "Shocking Grasp", "Spare the Dying", "Thorn Whip"],
                            ["Alarm", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Grease", "Identify", "Jump", "Longstrider", "Purify Food and Drink", "Sanctuary"],
                            ["Aid", "Alter Self", "Arcane Lock", "Blur", "Continual Flame", "Darkvision", "Enhance Ability", "Enlarge/Reduce", "Heat Metal", "Invisibility", "Lesser Restoration", "Levitate", "Magic Mouth", "Magic Weapon", "Protection from Poison", "Rope Trick", "See Invisibility", "Spider Climb", "Web"],
                            ["Blink", "Create Food and Water", "Dispel Magic", "Elemental Weapon", "Fly", "Glyph of Warding", "Haste", "Protection from Energy", "Revivify", "Water Breathing", "Water Walk"],
                            ["Arcane Eye", "Fabricate", "Freedom of Movement", "Leomund's Secret Chest", "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Stone Shape", "Stoneskin"],
                            ["Animate Objects", "Bigby's Hand", "Creation", "Greater Restoration", "Wall of Stone"]]


eberron_spells = [eberron_artificer_spells, [],[],[],[],[],[],[],[]]


# Strixhaven: A Curriculum of Chaos

strix_artificer_spells = [[],
                          [],
                          ["Kinetic Jaunt", "Vortex Warp"]]

strix_bard_spells = [[],
                     ["Silvery Barbs"],
                     ["Borrowed Knowledge", "Kinetic Jaunt"]]

strix_cleric_spells = [[],
                       [],
                       ["Borrowed Knowledge"]]

strix_druid_spells = [[],
                      [],
                      ["Wither and Bloom"]]

strix_sorcerer_spells = [[],
                         ["Silvery Barbs"],
                         ["Kinetic Jaunt", "Vortex Warp", "Wither and Bloom"]]

strix_warlock_spells = [[],
                        [],
                        ["Borrowed Knoeledge"]]

strix_wizard_spells = [[],
                       ["Silvery Barbs"],
                       ["Borrowed Knowledge", "Kinetic Jaunt", "Vortex Warp", "Wither and Bloom"]]


strix_spells = [strix_artificer_spells, strix_bard_spells, strix_cleric_spells, strix_druid_spells, [],[], strix_sorcerer_spells, strix_warlock_spells, strix_wizard_spells]


# Explorer's Guide to Wildemount

wilde_wizard_spells = [["Sapping Sting"],
                       ["Gift of Alacrity", "Magnify Gravity"],
                       ["Fortune's Favor", "Immovable Object", "Wristpocket"],
                       ["Pulse Wave"],
                       ["Gravity Sinkhole"],
                       ["Temporal Shunt"],
                       ["Gravity Fissure"],
                       ["Tether Essence"],
                       ["Dark Star", "Reality Break"],
                       ["Ravenous Void", "Time Ravage"]]


wilde_spells = [[],[],[],[],[],[],[],[], wilde_wizard_spells]
