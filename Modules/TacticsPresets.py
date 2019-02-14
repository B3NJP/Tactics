from Modules import TacticsClasses

#examples
exampleRace = TacticsClasses.Race("example", 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, [], [])
exampleJob = TacticsClasses.Job("example", 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, [], [])
# exampleAbility = TacticsClasses.Ability(name = "example", type = "magic", range = 20, dmg = 4, dmgType = "mAtk", mpCost = 2)

# REMEMBER:
# health, mana, pAtk, mAtk, dfce, res, agi, skl, mov, abilities, growthRates

# Growth Rate Priority:
# Base > Race > Job

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
maxHealth = 5,
maxMana = 5,
pAtk = 3,
mAtk = 3,
dfce = 5,
res = 2,
agi = 2,
skl = 3,
mov = 2,
abilities = [punch],
growthRates = [0.2, 0.2, 0.2, 0.2, 0.3, 0.1, 0.2, 0.2]
)

# class humanTemplateUnit(TacticsClasses.Person):

# Tiles
plain = TacticsClasses.Tile("plain", "0", 0, 0, 1, "Assets/Tiles/plains.png")
hill = TacticsClasses.Tile("hill", "h", 1, 0, 2, "Assets/Tiles/hill.png")
