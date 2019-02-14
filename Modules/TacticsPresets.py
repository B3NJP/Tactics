from Modules import TacticsClasses

#examples
exampleRace = TacticsClasses.Race("example", 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, [], [])
exampleJob = TacticsClasses.Job("example", 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, [], [])
exampleAbility = TacticsClasses.Ability(name = "example", type = "magic", range = 20, dmg = 4, dmgType = "mAtk", mpCost = 2)

# REMEMBER:
# health, mana, pAtk, mAtk, dfce, res, agi, skl, abilities



# Growth Rate Priority:
# Race > Job > Base

# Abilities
# Spells
fireball = TacticsClasses.Ability(name = "fireball", type = "magic", range = 20, dmg = 3, dmgType = "mAtk", mpCost = 1)
lightning = TacticsClasses.Ability(name = "lightning", type = "magic", range = 30, dmg = 5, dmgType = "mAtk", mpCost = 3)

# Races
# human = TacticsClasses.Race("human", 0.6, 0.1, 0.6, 0.2, 0.5, 0.4, 0.4, 0.4, [])
# elf = TacticsClasses.Race("elf", 0.3, 0.5, 0.3, 0.5, 0.2, 0.5, 0.5, 0.5, [])
#
# dragon = TacticsClasses.Race("dragon", 0.6, 0.6, 0.6, 0.6, 0.6, 0.5, 0.2, 0.3, [firebreath])
# nidhogg = TacticsClasses.Race("nidhogg", 1, 1, 1, 1, 1, 1, 1, 1, [eatSoul])
#
# # Jobs
# knight = TacticsClasses.Job("knight", 0.4, 0, 0.3, 0, 0.5, 0.1, 0.2, 0.2, [])
# mage = TacticsClasses.Job("mage", 0.1, 0.4, 0.1, 0.3, 0.1, 0.2, 0.1, 0.2, [fireball, teleport])

# Tiles
plain = TacticsClasses.Tile("plain", "0", 0, 0, 1, "Assets/Tiles/plains.png")
hill = TacticsClasses.Tile("hill", "h", 1, 0, 2, "Assets/Tiles/hill.png")
