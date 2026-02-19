from char_values import PC

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

bard_cantrips = ["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message",
                 "Minor Illusion", "Prestidigitation", "True Strike", "Vicious Mockery"]
bard_spells_1 = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic",
                 "Disguise Self", "Dissonant Whispers", "Faerie Fire", "Feather Fall", "Healing Word", "Heroism",
                 "Identify", "Illusory Script", "Longstrider", "Silent Image", "Sleep", "Speak with Animals",
                 "Tasha's Hideous Laughter", "Thunderwave", "Unseen Servant"]
bard_spells_2 = ["Animal Messenger", "Blindness/Deafness", "Calm Emotions", "Cloud of Daggers", "Crown of Madness",
                 "Detect Thoughts", "Enhance Ability", "Enthrall", "Heat Metal", "Hold Person", "Invisibility",
                 "Knock", "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Magic Mouth",
                 "Phantasmal Force", "See Invisibility", "Shatter", "Silence", "Suggestion", "Zone of Truth"]
bard_spells_3 = ["Bestow Curse", "Clairvoyance", "Dispel Magic", "Fear", "Feign Death", "Glyph of Warding",
                 "Hypnotic Pattern", "Leomund's Tiny Hut", "Major Image", "Nondetection", "Plant Growth",
                 "Sending", "Speak with Dead", "Speak with Plants", "Stinking Cloud", "Tongues"]
bard_spells_4 = ["Compulsion", "Confusion", "Dimension Door", "Freedom of Movement", "Greater Invisibility",
                 "Hallucinatory Terrain", "Locate Creature", "Polymorph"]
bard_spells_5 = ["Animate Objects", "Awaken", "Dominate Person", "Dream", "Geas", "Greater Restoration",
                 "Hold Monster", "Legend Lore", "Mass Cure Wounds", "Mislead", "Modify Memory", "Planar Binding",
                 "Raise Dead", "Scrying", "Seeming", "Teleportation Circle"]
bard_spells_6 = ["Eyebite", "Find the Path", "Guards and Wards", "Mass Suggestion", "Otto's Irresistible Dance",
                 "Programmed Illusion", "True Seeing"]
bard_spells_7 = ["Etherealness", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion",
                 "Mordenkainen's Sword", "Project Image", "Regenerate", "Resurrection", "Symbol", "Teleport"]
bard_spells_8 = ["Dominate Monster", "Feeblemind", "Glibness", "Mind Blank", "Power Word Stun"]
bard_spells_9 = ["Foresight", "Power Word Heal", "Power Word Kill", "True Polymorph"]


cleric_cantrips = ["Guidance", "Light", "Mending", "Resistance", "Sacred Flame", "Spare the Dying", "Thaumaturgy"]
cleric_spells_1 = ["Bane", "Bless", "Command", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good",
                   "Detect Magic", "Detect Poison and Disease", "Guiding Bolt", "Healing Word", "Inflict Wounds",
                   "Protection from Evil and Good", "Purify Food and Drink", "Sanctuary", "Shield of Faith"]
cleric_spells_2 = ["Aid", "Augury", "Blindness/Deafness", "Calm Emotions", "Continual Flame", "Enhance Ability",
                   "Find Traps", "Gentle Repose", "Hold Person", "Lesser Restoration", "Locate Object",
                   "Prayer of Healing", "Protection from Poison", "Silence", "Spiritual Weapon", "Warding Bond",
                   "Zone of Truth"]
cleric_spells_3 = ["Animate Dead", "Beacon of Hope", "Bestow Curse", "Clairvoyance", "Create Food and Water",
                   "Daylight", "Dispel Magic", "Feign Death", "Glyph of Warding", "Magic Circle",
                   "Mass Healing Word", "Meld into Stone", "Protection from Energy", "Remove Curse", "Revivify",
                   "Sending", "Speak with Dead", "Spirit Guardians", "Tongues", "Water Walk"]
cleric_spells_4 = ["Banishment", "Control Water", "Death Ward", "Divination", "Freedom of Movement",
                   "Guardian of Faith", "Locate Creature", "Stone Shape"]
cleric_spells_5 = ["Commune", "Contagion", "Dispel Evil and Good", "Flame Strike", "Geas", "Greater Restoration",
                   "Hallow", "Insect Plague", "Legend Lore", "Mass Cure Wounds", "Planar Binding", "Raise Dead",
                   "Scrying"]
cleric_spells_6 = ["Blade Barrier", "Create Undead", "Find the Path", "Forbiddance", "Harm", "Heal",
                   "Heroes' Feast", "Planar Ally", "True Seeing", "Word of Recall"]
cleric_spells_7 = ["Conjure Celestial", "Divine Word", "Etherealness", "Fire Storm", "Plane Shift", "Regenerate",
                   "Resurrection", "Symbol"]
cleric_spells_8 = ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura"]
cleric_spells_9 = ["Astral Projection", "Gate", "Mass Heal", "True Resurrection"]


druid_cantrips = ["Druidcraft", "Guidance", "Mending", "Poison Spray", "Produce Flame", "Resistance",
                  "Shillelagh", "Thorn Whip"]
druid_spells_1 = ["Animal Friendship", "Charm Person", "Create or Destroy Water", "Cure Wounds", "Detect Magic",
                 "Detect Poison and Disease", "Entangle", "Faerie Fire", "Fog Cloud", "Goodberry", "Healing Word",
                 "Jump", "Longstrider", "Purify Food and Drink", "Speak with Animals", "Thunderwave"]
druid_spells_2 = ["Animal Messenger", "Barkskin", "Beast Sense", "Darkvision", "Enhance Ability", "Find Traps",
                 "Flame Blade", "Flaming Sphere", "Gust of Wind", "Heat Metal", "Hold Person",
                 "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Moonbeam",
                 "Pass without Trace", "Protection from Poison", "Spike Growth"]
druid_spells_3 = ["Call Lightning", "Conjure Animals", "Daylight", "Dispel Magic", "Feign Death",
                  "Meld into Stone", "Plant Growth", "Protection from Energy", "Sleet Storm", "Speak with Plants",
                  "Water Breathing", "Water Walk", "Wind Wall"]
druid_spells_4 = ["Blight", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings", "Control Water",
                  "Dominate Beast", "Freedom of Movement", "Giant Insect", "Grasping Vine",
                  "Hallucinatory Terrain", "Ice Storm", "Locate Creature", "Polymorph", "Stone Shape",
                  "Stoneskin", "Wall of Fire"]
druid_spells_5 = ["Antilife Shell", "Awaken", "Commune with Nature", "Conjure Elemental", "Contagion", "Geas",
                  "Greater Restoration", "Insect Plague", "Mass Cure Wounds", "Planar Binding", "Reincarnate",
                  "Scrying", "Tree Stride", "Wall of Stone"]
druid_spells_6 = ["Conjure Fey", "Find the Path", "Heal", "Heroes' Feast", "Move Earth", "Sunbeam",
                  "Transport via Plants", "Wall of Thorns", "Wind Walk"]
druid_spells_7 = ["Fire Storm", "Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity"]
druid_spells_8 = ["Animal Shapes", "Antipathy/Sympathy", "Control Weather", "Earthquake", "Feeblemind",
                  "Sunburst", "Tsunami"]
druid_spells_9 = ["Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection"]


paladin_spells_1 = ["Bless", "Command", "Compelled Duel", "Cure Wounds", "Detect Evil and Good", "Detect Magic",
                    "Detect Poison and Disease", "Divine Favor", "Heroism", "Protection from Evil and Good",
                    "Purify Food and Drink", "Searing Smite", "Shield of Faith", "Thunderous Smite", "Wrathful Smite"]
paladin_spells_2 = ["Aid", "Branding Smite", "Find Steed", "Lesser Restoration", "Locae Object", "Magic Weapon",
                    "Protection from Poison", "Zone of Truth"]
paladin_spells_3 = ["Aura of Vitality", "Blinding Smite", "Create Food and Water", "Crusader's Mantle",
                    "Daylight", "Dispel Magic", "Elemental Weapon", "Magic Circle", "Remove Curse", "Revivify"]
paladin_spells_4 = ["Aura of Life", "Aura of Purity", "Banishment", "Death Ward", "Locate Creature", "Staggering Smite"]
paladin_spells_5 = ["Banishing Smite", "Circle of Power", "Destructive Wave", "Dispel Evil and Good", "Geas",
                    "Raise Dead"]


ranger_spells_1 = ["Alarm", "Animal Friendship", "Cure Wounds", "Detect Magic", "Detect Poison and Disease",
                   "Ensnaring Strike", "Fog Cloud", "Goodberry", "Hail of Thorns", "Hunter's Mark", "Jump",
                   "Longstrider", "Speak with Animals"]
ranger_spells_2 = ["Animal Messenger", "Barkskin", "Beast Sense", "Cordon of Arrows", "Darkvision", "Find Traps",
                   "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Pass without Trace",
                   "Protection from Poison", "Silence", "Spike Growth"]
ranger_spells_3 = ["Conjure Animals", "Conjure Barrage", "Daylight", "Lightning Arrow", "Nondetection",
                   "Plant Growth", "Protection from Energy", "Speak with Plants", "Water Breathing", "Water Walk",
                   "Wind Wall"]
ranger_spells_4 = ["Conjure Woodland Beings", "Freedom of Movement", "Grasping Vine", "Locate Creature", "Stoneskin"]
ranger_spells_5 = ["Commune with Nature", "Conjure Volley", "Swift Quiver", "Tree Stride"]


sorcerer_cantrips = ["Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights", "Fire Bolt", "Friends",
                     "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray",
                     "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
sorcerer_spells_1 = ["Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages",
                     "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall",
                     "Fog Cloud", "Jump", "Mage Armor", "Magic Missile", "Ray of Sickness", "Shield",
                     "Silent Image", "Sleep", "Thunderwave", "Witch Bolt"]
sorcerer_spells_2 = ["Alter Self", "Blindness/Deafness", "Blur", "Cloud of Daggers", "Crown of Madness",
                     "Darkness", "Darkvision", "Detect Thoughts", "Enhance Ability", "Enlarge/Reduce",
                     "Gust of Wind", "Hold Person", "Invisibility", "Knock", "Levitate", "Mirror Image",
                     "Misty Step", "Phantasmal Force", "Scorching Ray", "See Invisibility", "Shatter",
                     "Spider Climb", "Suggestion", "Web"]
sorcerer_spells_3 = ["Blink", "Clairvoyance", "Counterspell", "Daylight", "Dispel Magic", "Fear", "Fireball",
                     "Fly", "Gaseous Form", "Haste", "Hypnotic Pattern", "Lightning Bolt", "Major Image",
                     "Protection from Energy", "Sleet Storm", "Slow", "Stinking Cloud", "Tongues",
                     "Water Breathing", "Water Walk"]
sorcerer_spells_4 = ["Banishment", "Blight", "Confusion", "Dimension Door", "Dominate Beast", "Greater Invisibility",
                     "Ice Storm", "Polymorph", "Stoneskin", "Wall of Fire"]
sorcerer_spells_5 = ["Animate Objects", "Cloudkill", "Cone of Cold", "Creation", "Dominate Person", "Hold Monster",
                     "Insect Plague", "Seeming", "Telekinesis", "Teleportation Circle", "Wall of Stone"]
sorcerer_spells_6 = ["Arcane Gate", "Chain Lightning", "Circle of Death", "Disintegrate", "Eyebite",
                     "Globe of Invulnerability", "Mass Suggestion", "Move Earth", "Sunbeam", "True Seeing"]
sorcerer_spells_7 = ["Delayed Blast Fireball", "Etherealness", "Finger of Death", "Fire Storm", "Plane Shift",
                     "Prismatic Spray", "Reverse Gravity", "Teleport"]
sorcerer_spells_8 = ["Dominate Monster", "Earthquake", "Incendiary Cloud", "Power Word Stun", "Sunburst"]
sorcerer_spells_9 = ["Gate", "Meteor Swarm", "Power Word Kill", "Time Stop", "Wish"]


warlock_cantrips = ["Blade Ward", "Chill Touch", "Eldritch Blast", "Friends", "Mage Hand", "Minor Illusion",
                    "Poison Spray", "Prestidigitation", "True Strike"]
warlock_spells_1 = ["Armor of Agathys", "Arms of Hadar", "Charm Person", "Comprehend Languages",
                    "Expeditious Retreat", "Hellish Rebuke", "Hex", "Illusory Script",
                    "Protection from Evil and Good", "Unseen Servant", "Witch Bolt"]
warlock_spells_2 = ["Cloud of Daggers", "Crown of Madness", "Darkness", "Enthrall", "Hold Person", "Invisibility",
                    "Mirror Image", "Misty Step", "Ray of Enfeeblement", "Shatter", "Spider Climb", "Suggestion"]
warlock_spells_3 = ["Counterspell", "Dispel Magic", "Fear", "Fly", "Gaseous Form", "Hunger of Hadar",
                    "Hypnotic Pattern", "Magic Circle", "Major Image", "Remove Curse", "Tongues", "Vampiric Touch"]
warlock_spells_4 = ["Banishment", "Blight", "Dimension Door", "Hallucinatory Terrain"]
warlock_spells_5 = ["Contact Other Plane", "Dream", "Hold Monster", "Scrying"]
warlock_spells_6 = ["Arcane Gate", "Circle of Death", "Conjure Fey", "Create Undead", "Eyebite", "Flesh to Stone",
                    "Mass Suggestion", "True Seeing"]
warlock_spells_7 = ["Etherealness", "Finger of Death", "Forcecage", "Plane Shift"]
warlock_spells_8 = ["Demiplane", "Dominate Monster", "Feeblemind", "Glibness", "Power Word Stun"]
warlock_spells_9 = ["Astral Projection", "Foresight", "Imprisonment", "Power Word Kill", "True Polymorph"]


wizard_cantrips = ["Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights", "Fire Bolt", "Friends", "Light",
                   "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation",
                   "Ray of Frost", "Shocking Grasp", "True Strike"]
wizard_spells_1 = ["Alarm", "Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages",
                   "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall",
                   "Find Familiar", "Fog Cloud", "Grease", "Identify", "Illusory Script", "Jump", "Longstrider",
                   "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Ray of Sickness", "Shield",
                   "Silent Image", "Sleep", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderwave",
                   "Unseen Servant", "Witch Bolt"]
wizard_spells_2 = ["Alter Self", "Arcane Lock", "Blindness/Deafness", "Blur", "Cloud of Daggers", "Continual Flame",
                   "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Enlarge/Reduce",
                   "Flaming Sphere", "Gentle Repose", "Gust of Wind", "Hold Person", "Invisibility", "Knock",
                   "Levitate", "Locate Object", "Magic Mouth", "Magic Weapon", "Melf's Acid Arrow", "Mirror Image",
                   "Misty Step", "Nystul's Magic Aura", "Phantasmal Force", "Ray of Enfeeblement", "Rope Trick",
                   "Scorching Ray", "See Invisibility", "Shatter", "Spider Climb", "Suggestion", "Web"]
wizard_spells_3 = ["Animate Dead", "Bestow Curse", "Blink", "Clairvoyance", "Counterspell", "Dispel Magic", "Fear",
                   "Feign Death", "Fireball", "Fly", "Gaseous Form", "Glyph of Warding", "Haste", "Hypnotic Pattern",
                   "Leomund's Tiny Hut", "Lightning Bolt", "Magic Circle", "Major Image", "Nondetection",
                   "Phantom Steed", "Protection from Energy", "Remove Curse", "Sending", "Sleet Storm", "Slow",
                   "Stinking Cloud", "Tongues", "Vampiric Touch", "Water Breathing"]
wizard_spells_4 = ["Arcane Eye", "Banishment", "Blight", "Confusion", "Conjure Minor Elementals", "Control Water",
                   "Dimension Door", "Evard's Black Tentacles", "Fabricate", "Fire Shield", "Greater Invisibility",
                   "Hallucinatory Terrain", "Ice Storm", "Leomund's Secret Chest", "Locate Creature",
                   "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere",
                   "Phantasmal Killer", "Polymorph", "Stone Shape", "Stoneskin", "Wall of Fire"]
wizard_spells_5 = ["Animate Objects", "Bigby's Hand", "Cloudkill", "Cone of Cold", "Conjure Elemental",
                   "Contact Other Plane", "Creation", "Dominate Person", "Dream", "Geas", "Hold Monster",
                   "Legend Lore", "Mislead", "Modify Memory", "Passwall", "Planar Binding", "Rary's Telepathic Bond",
                   "Scrying", "Seeming", "Telekinesis", "Teleportation Circle", "Wall of Force", "Wall of Stone"]
wizard_spells_6 = ["Arcane Gate", "Chain Lightning", "Circle of Death", "Contingency", "Create Undead",
                   "Disintegrate", "Drawmij's Instant Summon", "Eyebite", "Flesh to Stone", "Globe of Invulnerability",
                   "Guards and Wards", "Magic Jar", "Mass Suggestion", "Move Earth", "Otiluke's Freezing Sphere",
                   "Otto's Irresistable Dance", "Programmed Illusion", "Sunbeam", "True Seeing", "Wall of Ice"]
wizard_spells_7 = ["Delayed Blast Fireball", "Etherealness", "Finger of Death", "Forcecage", "Mirage Arcane",
                   "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", "Plane Shift", "Prismatic Spray",
                   "Project Image", "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport"]
wizard_spells_8 = ["Antimagic Field", "Anitpathy/Sympathy", "Clone", "Control Weather", "Demiplane",
                   "Dominate Monster", "Feeblemind", "Incendiary Cloud", "Maze", "Mind Blank", "Power Word Stun",
                   "Sunburst", "Telepathy"]
wizard_spells_9 = ["Astral Projection", "Foresight", "Gate", "Imprisonment", "Meteor Swarm", "Power Word Kill",
                   "Prismatic Wall", "Shapechange", "Time Stop", "True Polymorph", "Weird", "Wish"]


# Sword Coast Adventurer's Guide

scag_sorcerer_cantrips = ["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Sword Burst"]
scag_warlock_cantrips = ["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Sword Burst"]
scag_wizard_cantrips = ["Booming Blade", "Green-Flame Blade", "Lightning Lure", "Sword Burst"]


# Elemental Evil Player's Companion

ee_artificer_cantrips = ["Create Bonfire", "Frostbite", "Magic Stone", "Thunderclap"]
ee_artificer_spells_1 = ["Absorb Elements", "Catapult"]
ee_artificer_spells_2 = ["Pyrotechnics", "Skywrite"]
ee_artificer_spells_3 = ["Flame Arrows"]
ee_artificer_spells_4 = ["Elemental Bane"]
ee_artificer_spells_5 = ["Transmute Rock"]

ee_bard_cantrips = ["Thunderclap"]
ee_bard_spells_1 = ["Earth Tremor"]
ee_bard_spells_2 = ["Pyrotechnics", "Skywrite", "Warding Wind"]


ee_druid_cantrips = ["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Magic Stone", "Mold Earth",
                     "Shape Water", "Thunderclap"]
ee_druid_spells_1 = ["Absorb Elements", "Beast Bond", "Ice Knife", "Earth Tremor"]
ee_druid_spells_2 = ["Dust Devil", "Earthbind", "Skywrite", "Warding Wind"]
ee_druid_spells_3 = ["Erupting Earth", "Flame Arrows", "Tidal Wave", "Wall of Water"]
ee_druid_spells_4 = ["Elemental Bane", "Watery Sphere"]
ee_druid_spells_5 = ["Control Winds", "Maelstrom", "Transmute Rock"]
ee_druid_spells_6 = ["Bones of the Earth", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                     "Investiture of Wind", "Primordial Ward"]
ee_druid_spells_7 = ["Whirlwind"]


ee_ranger_spells_1 = ["Absorb Elements", "Beast Bond"]
ee_ranger_spells_3 = ["Flame Arrows"]


ee_sorcerer_cantrips = ["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Mold Earth", "Shape Water",
                        "Thunderclap"]
ee_sorcerer_spells_1 = ["Catapult", "Ice Knife", "Earth Tremor"]
ee_sorcerer_spells_2 = ["Aganazzar's Scorcher", "Dust Devil", "Earthbind", "Maximilian's Earthen Grasp",
                        "Pyrotechnics", "Snilloc's Snowball Swarm", "Warding Wind"]
ee_sorcerer_spells_3 = ["Erupting Earth", "Flame Arrows", "Melf's Minute Meteors", "Wall of Water"]
ee_sorcerer_spells_4 = ["Storm Sphere", "Vitriolic Sphere", "Watery Sphere"]
ee_sorcerer_spells_5 = ["Control Winds", "Immolation"]
ee_sorcerer_spells_6 = ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                        "Investiture of Wind"]
ee_sorcerer_spells_8 = ["Abi-Dalzim's Horrid Wilting"]


ee_warlock_cantrips = ["Create Bonfire", "Frostbite", "Magic Stone", "Thunderclap"]
ee_warlock_spells_2 = ["Earthbind"]
ee_warlock_spells_4 = ["Elemental Bane"]
ee_warlock_spells_6 = ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                       "Investiture of Wind"]


ee_wizard_cantrips = ["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Mold Earth", "Shape Water",
                      "Thunderclap"]
ee_wizard_spells_1 = ["Absorb Elements", "Catapult", "Ice Knife", "Earth Tremor"]
ee_wizard_spells_2 = ["Aganazzar's Scorcher", "Dust Devil", "Earthbind", "Maximilian's Earthen Grasp",
                      "Pyrotechnics", "Skywrite", "Snilloc's Snowball Swarm"]
ee_wizard_spells_3 = ["Erupting Earth", "Flame Arrows", "Melf's Minute Meteors", "Tidal Wave", "Wall of Sand",
                      "Wall of Water"]
ee_wizard_spells_4 = ["Elemental Bane", "Storm Sphere", "Vitriolic Sphere", "Watery Sphere"]
ee_wizard_spells_5 = ["Control Winds", "Immolation", "Transmute Rock"]
ee_wizard_spells_6 = ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                      "Investiture of Wind"]
ee_wizard_spells_7 = ["Whirlwind"]
ee_wizard_spells_8 = ["Abi-Dalzim's Horrid Wilting"]


# Xanathar's Guide to Everything

xgte_artificer_cantrips = ["Create Bonfire", "Frostbite", "Magic Stone", "Thunderclap"]
xgte_artificer_spells_1 = ["Absorb Elements", "Catapult", "Snare"]
xgte_artificer_spells_2 = ["Pyrotechnics", "Skywrite"]
xgte_artificer_spells_3 = ["Catnap", "Flame Arrows", "Tiny Servant"]
xgte_artificer_spells_4 = ["Elemental Bane"]
xgte_artificer_spells_5 = ["Skill Empowerment", "Transmute Rock"]

xgte_bard_cantrips = ["Thunderclap"]
xgte_bard_spells_1 = ["Earth Tremor"]
xgte_bard_spells_2 = ["Pyrotechnics", "Skywrite", "Warding Wind"]
xgte_bard_spells_3 = ["Catnap", "Enemies Abound"]
xgte_bard_spells_4 = ["Charm Monster"]
xgte_bard_spells_5 = ["Skill Empowerment", "Synaptic Static"]
xgte_bard_spells_9 = ["Mass Polymorph", "Psychic Scream"]


xgte_cleric_cantrips = ["Toll the Dead", "Word of Radiance"]
xgte_cleric_spells_1 = ["Ceremony"]
xgte_cleric_spells_3 = ["Life Transference"]
xgte_cleric_spells_5 = ["Dawn", "Holy Weapon"]
xgte_cleric_spells_7 = ["Temple of the Gods"]


xgte_druid_cantrips = ["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Infestation", "Magic Stone",
                       "Mold Earth", "Primal Savagery", "Shape Water", "Thunderclap"]
xgte_druid_spells_1 = ["Absorb Elements", "Beast Bond", "Earth Tremor", "Ice Knife", "Snare"]
xgte_druid_spells_2 = ["Dust Devil", "Earthbind", "Healing Spirit", "Skywrite", "Warding Wind"]
xgte_druid_spells_3 = ["Erupting Earth", "Flame Arrows", "Tidal Wave", "Wall of Water"]
xgte_druid_spells_4 = ["Charm Monster", "Elemental Bane", "Guardian of Nature", "Watery Sphere"]
xgte_druid_spells_5 = ["Control Winds", "Maelstrom", "Transmute Rock", "Wrath of Nature"]
xgte_druid_spells_6 = ["Bones of the Earth", "Druid Grove", "Investiture of Flame", "Investiture of Ice",
                       "Investiture of Stone", "Investiture of Wind", "Primordial Ward"]
xgte_druid_spells_7 = ["Whirlwind"]


xgte_paladin_spells_1 = ["Ceremony"]
xgte_paladin_spells_4 = ["Find Greater Steed"]
xgte_paladin_spells_5 = ["Holy Weapon"]


xgte_ranger_spells_1 = ["Absorb Elements", "Beast Bond", "Snare", "Zephyr Strike"]
xgte_ranger_spells_2 = ["Healing Spirit"]
xgte_ranger_spells_3 = ["Flame Arrows"]
xgte_ranger_spells_4 = ["Guardian of Nature"]
xgte_ranger_spells_5 = ["Steel Wind Strike", "Wrath of Nature"]


xgte_sorcerer_cantrips = ["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Infestation", "Mold Earth",
                          "Shape Water", "Thunderclap"]
xgte_sorcerer_spells_1 = ["Absorb Elements", "Catapult", "Chaos Bolt", "Earth Tremor", "Ice Knife"]
xgte_sorcerer_spells_2 = ["Aganazzar's Scorcher", "Dragon's Breath", "Dust Devil", "Earthbind",
                          "Maximilian's Earthen Grasp", "Mind Spike", "Pyrotechnics", "Shadow Blade",
                          "Snilloc's Snowball Swarm", "Warding Wind"]
xgte_sorcerer_spells_3 = ["Catnap", "Enemies Abound", "Erupting Earth", "Flame Arrows", "Melf's Minute Meteors",
                          "Thunder Step", "Tidal Wave", "Wall of Water"]
xgte_sorcerer_spells_4 = ["Charm Monster", "Sickening Radiance", "Storm Sphere", "Vitriolic Sphere",
                          "Watery Sphere"]
xgte_sorcerer_spells_5 = ["Control Winds", "Enervation", "Far Step", "Immolation", "Skill Empowerment",
                          "Synaptic Static", "Wall of Light"]
xgte_sorcerer_spells_6 = ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                          "Investiture of Wind", "Mental Prison", "Scatter"]
xgte_sorcerer_spells_7 = ["Crown of Stars", "Power Word Pain", "Whirlwind"]
xgte_sorcerer_spells_8 = ["Abi-Dalzim's Horrid Wilting"]
xgte_sorcerer_spells_9 = ["Mass Polymorph", "Psychic Scream"]


xgte_warlock_cantrips = ["Create Bonfire", "Frostbite", "Infestation", "Magic Stone", "Thunderclap", "Toll the Dead"]
xgte_warlock_spells_1 = ["Cause Fear"]
xgte_warlock_spells_2 = ["Earthbind", "Mind Spike", "Shadow Blade"]
xgte_warlock_spells_3 = ["Enemies Abound", "Thunder Step", "Summon Lesser Demons"]
xgte_warlock_spells_4 = ["Charm Monster", "Elemental Bane", "Shadow of Moil", "Sickening Radiance",
                         "Summon Greater Demon"]
xgte_warlock_spells_5 = ["Danse Macabre", "Enervation", "Far Step", "Infernal Calling", "Negative Energy Flood",
                         "Synaptic Static", "Wall of Light"]
xgte_warlock_spells_6 = ["Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                         "Investiture of Wind", "Mental Prison", "Scatter", "Soul Cage"]
xgte_warlock_spells_7 = ["Crown of Stars", "Power Word Pain"]
xgte_warlock_spells_8 = ["Maddening Darkness"]
xgte_warlock_spells_9 = ["Psychic Scream"]


xgte_wizard_cantrips = ["Control Flames", "Create Bonfire", "Frostbite", "Gust", "Infestation", "Mold Earth",
                        "Shape Water", "Thunderclap", "Toll the Dead"]
xgte_wizard_spells_1 = ["Absorb Elements", "Catapult", "Cause Fear", "Earth Tremor", "Ice Knife", "Snare"]
xgte_wizard_spells_2 = ["Aganazzar's Scorcher", "Dragon's Breath", "Dust Devil", "Earthbind",
                        "Maximilian's Earthen Grasp", "Mind Spike", "Pyrotechnics", "Shadow Blade", "Skywrite",
                        "Snilloc's Snowball Swarm", "Warding Wind"]
xgte_wizard_spells_3 = ["Catnap", "Enemies Abound", "Erupting Earth", "Flame Arrows", "Life Transference",
                        "Melf's Minute Meteors", "Summon Lesser Demons", "Thunder Step", "Tidal Wave",
                        "Tiny Servant", "Wall of Sand", "Wall of Water"]
xgte_wizard_spells_4 = ["Charm Monster", "Elemental Bane", "Sickening Radiance", "Storm Sphere",
                        "Summon Greater Demon", "Vitriolic Sphere", "Watery Sphere"]
xgte_wizard_spells_5 = ["Control Winds", "Danse Macabre", "Dawn", "Enervation", "Far Step", "Immolation",
                        "Infernal Calling", "Negative Energy Flood", "Skill Empowerment", "Steel Wind Strike",
                        "Synaptic Static", "Transmute Rock", "Wall of Light"]
xgte_wizard_spells_6 = ["Create Homunculus", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                        "Investiture of Wind", "Mental Prison", "Scatter", "Soul Cage", "Tenser's Transformation"]
xgte_wizard_spells_7 = ["Crown of Stars", "Power Word Pain", "Whirlwind"]
xgte_wizard_spells_8 = ["Abi-Dalzim's Horrid Wilting", "Illusory Dragon", "Maddening Darkness", "Mighty Fortress"]
xgte_wizard_spells_9 = ["Invulnerability", "Mass Polymorph", "Psychic Scream"]


# Tasha's Cauldron of Everything

tcoe_artificer_cantrips = ["Acid Splash", "Booming Blade", "Dancing Lights", "Fire Bolt", "Green-Flame Blade",
                           "Guidance", "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Poison Spray",
                           "Prestidigitation", "Ray of Frost", "Resistance", "Shocking Grasp", "Spare the Dying",
                           "Sword Burst", "Thorn Whip"]
tcoe_artificer_spells_1 = ["Alarm", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat",
                           "Faerie Fire", "False Life", "Feather Fall", "Grease", "Identify", "Jump",
                           "Longstrider", "Purify Food and Drink", "Sanctuary", "Tasha's Caustic Brew"]
tcoe_artificer_spells_2 = ["Aid", "Alter Self", "Arcane Lock", "Blur", "Continual Flame", "Darkvision",
                           "Enhance Ability", "Enlarge/Reduce", "Heat Metal", "Invisibility", "Lesser Restoration",
                           "Levitate", "Magic Mouth", "Magic Weapon", "Protection from Poison", "Rope Trick",
                           "See Invisibility", "Spider Climb", "Web"]
tcoe_artificer_spells_3 = ["Blink", "Create Food and Water", "Dispel Magic", "Elemental Weapon", "Fly",
                           "Glyph of Warding", "Haste", "Intellect Fortress", "Protection from Energy",
                           "Revivify", "Water Breathing", "Water Walk"]
tcoe_artificer_spells_4 = ["Arcane Eye", "Fabricate", "Freedom of Movement", "Leomund's Secret Chest",
                           "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum",
                           "Otiluke's Resilient Sphere", "Stone Shape", "Stoneskin", "Summon Construct"]
tcoe_artificer_spells_5 = ["Animate Objects", "Bigby's Hand", "Creation", "Greater Restoration", "Wall of Stone"]


# Fizban's Treasury of Dragons

ftod_artificer_spells_3 = ["Ashardalon's Stride"]


ftod_bard_spells_2 = ["Nathair's Mischief"]
ftod_bard_spells_4 = ["Raulothim's Psychic Lance"]


ftod_druid_spells_5 = ["Summon Draconic Spirit"]
ftod_druid_spells_7 = ["Draconic Transformation"]


ftod_ranger_spells_3 = ["Ashardalon's Stride"]


ftod_sorcerer_spells_2 = ["Nathair's Mischief", "Rime's Binding Ice"]
ftod_sorcerer_spells_3 = ["Ashardalon's Stride"]
ftod_sorcerer_spells_4 = ["Raulothim's Psychic Lance"]
ftod_sorcerer_spells_5 = ["Summon Draconic Spirit"]
ftod_sorcerer_spells_6 = ["Fizban's Platinum Shield"]
ftod_sorcerer_spells_7 = ["Draconic Transformation"]


ftod_warlock_spells_4 = ["Raulothim's Psychic Lance"]


ftod_wizard_spells_2 = ["Nathair's Mischief", "Rime's Binding Ice"]
ftod_wizard_spells_3 = ["Ashardalon's Stride"]
ftod_wizard_spells_4 = ["Raulothim's Psychic Lance"]
ftod_wizard_spells_5 = ["Summon Draconic Spirit"]
ftod_wizard_spells_6 = ["Fizban's Platinum Shield"]
ftod_wizard_spells_7 = ["Draconic Transformation"]


# Eberron: Rising from the Last War

eberron_artificer_cantrips = ["Acid Splash", "Dancing Lights", "Fire Bolt", "Guidance", "Light", "Mage Hand",
                           "Mending", "Message", "Poison Spray", "Prestidigitation", "Ray of Frost", "Resistance",
                           "Shocking Grasp", "Spare the Dying", "Thorn Whip"]
eberron_artificer_spells_1 = ["Alarm", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat",
                           "Faerie Fire", "False Life", "Feather Fall", "Grease", "Identify", "Jump",
                           "Longstrider", "Purify Food and Drink", "Sanctuary"]
eberron_artificer_spells_2 = ["Aid", "Alter Self", "Arcane Lock", "Blur", "Continual Flame", "Darkvision",
                           "Enhance Ability", "Enlarge/Reduce", "Heat Metal", "Invisibility", "Lesser Restoration",
                           "Levitate", "Magic Mouth", "Magic Weapon", "Protection from Poison", "Rope Trick",
                           "See Invisibility", "Spider Climb", "Web"]
eberron_artificer_spells_3 = ["Blink", "Create Food and Water", "Dispel Magic", "Elemental Weapon", "Fly",
                           "Glyph of Warding", "Haste", "Protection from Energy", "Revivify", "Water Breathing",
                           "Water Walk"]
eberron_artificer_spells_4 = ["Arcane Eye", "Fabricate", "Freedom of Movement", "Leomund's Secret Chest",
                           "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum",
                           "Otiluke's Resilient Sphere", "Stone Shape", "Stoneskin"]
eberron_artificer_spells_5 = ["Animate Objects", "Bigby's Hand", "Creation", "Greater Restoration", "Wall of Stone"]
