import random
from Modules import TacticsClasses

#examples
exampleRace = TacticsClasses.Race("example", 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, [], [])
exampleJob = TacticsClasses.Job("example", 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, [], [])
# exampleAbility = TacticsClasses.Ability(name = "example", type = "magic", range = 20, dmg = 4, dmgType = "mAtk", mpCost = 2)

# REMEMBER:
# health, mana, pAtk, mAtk, dfce, res, agi, skl, mov, abilities, growthRates
# Only special jobs (mounted) should have a mov stat above 0

# Base Stat Priority:
# Base > Job > Race

# Growth Rate Priority:
# Base > Job = Race

# Abilities
# Physical
punch = TacticsClasses.Ability(
name = "Punch",
type = "punch",
dmgType = "physical",
range = 1
)
# Spells
# fireball = TacticsClasses.Ability(name = "fireball", type = "magic", range = 20, dmg = 3, dmgType = "mAtk", mpCost = 1)
# lightning = TacticsClasses.Ability(name = "lightning", type = "magic", range = 30, dmg = 5, dmgType = "mAtk", mpCost = 3)

# Races
human = TacticsClasses.Race(
name = "Human",
maxHealth = 3,
maxMana = 3,
pAtk = 2,
mAtk = 2,
dfce = 4,
res = 1,
agi = 1,
skl = 2,
mov = 2,
abilities = [punch],
growthRates = [0.2, 0.2, 0.2, 0.2, 0.3, 0.1, 0.2, 0.2]
)

# Jobs
knight = TacticsClasses.Job(
name = "Knight",
maxHealth = 5,
maxMana = 5,
pAtk = 3,
mAtk = 3,
dfce = 5,
res = 2,
agi = 2,
skl = 3,
mov = -1,
abilities = [punch],
growthRates = [0.2, 0.2, 0.2, 0.2, 0.3, 0.1, 0.2, 0.2]
)

class humanKnightTemplateUnit(TacticsClasses.Person):
    def __init__(self, name, location = [0,0], abilities = [], weapon = None, items = []):
        super().__init__(name, knight, human, [floor(random.random * 10) for i in range(0,8)], [(floor(random.random * 4)/10) for i in range(0,8)], location, abilities, weapon, items)


# Tiles
plain = TacticsClasses.Tile("plain", "0", 0, 0, 1, "Assets/Tiles/plains.png")
hill = TacticsClasses.Tile("hill", "h", 1, 0, 2, "Assets/Tiles/hill.png")
