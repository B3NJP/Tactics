from Modules import TacticsClasses

#examples
exampleRace = TacticsClasses.Race("example", 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, [], [])
exampleJob = TacticsClasses.Job("example", 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, [], [])
# exampleAbility = TacticsClasses.Ability(name = "example", type = "magic", range = 20, dmg = 4, dmgType = "mAtk", mpCost = 2)

# REMEMBER:
# health, mana, pAtk, mAtk, dfce, res, agi, skl, abilities

# Growth Rate Priority:
# Base > Race > Job

# Abilities
# Physical
# Spells
fireball = TacticsClasses.Ability(name = "fireball", type = "magic", range = 20, dmg = 3, dmgType = "mAtk", mpCost = 1)
lightning = TacticsClasses.Ability(name = "lightning", type = "magic", range = 30, dmg = 5, dmgType = "mAtk", mpCost = 3)

# Races

# class humanTemplateUnit(TacticsClasses.Person):

# Tiles
plain = TacticsClasses.Tile("plain", "0", 0, 0, 1, "Assets/Tiles/plains.png")
hill = TacticsClasses.Tile("hill", "h", 1, 0, 2, "Assets/Tiles/hill.png")
