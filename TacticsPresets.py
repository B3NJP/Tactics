import MagicClasses

#examples
exampleRace = MagicClasses.Race("example", 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, [])
exampleJob = MagicClasses.Job("example", 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, [])
exampleAbility = MagicClasses.Ability(name = "example", type = "magic", range = 20, dmg = 4, dmgType = "mAtk", mpCost = 2)

# REMEMBER:
# health, mana, pAtk, mAtk, dfce, res, agi, skl, abilities

# Growth Rate Priority:
# Race > Job > Base

# Abilities
# Spells
fireball = MagicClasses.Ability(name = "fireball", type = "magic", range = 20, dmg = 3, dmgType = "mAtk", mpCost = 1)
lightning = MagicClasses.Ability(name = "lightning", type = "magic", range = 30, dmg = 5, dmgType = "mAtk", mpCost = 3)

death = MagicClasses.Ability(name = "death", type = "magic", range = 40, dmg = 100, dmgType = "mAtk", mpCost = 100)

def tele(values, targets):
    values[0] = values[1]
teleport = MagicClasses.Ability(name = "teleport", type = "magic", range = 40, dodgeable = False, dmgType = "special", mpCost = 3, special = tele)


# Racial
firebreath = MagicClasses.Ability(name = "firebreath", type = "racial", range = 5, dmg = 7, dmgType = "mAtk", cooldown = 10)

def eatsoul (values, target):
    if (target.health <= 0):
        values[0].health = min(values[0].health + values[0].maxHealth*0.1, values[0].maxHealth)
eatSoul = MagicClasses.Ability(name = "eatSoul", type = "racial", range = 1, multi = 2, dmgType = "unresistable", cooldown = 10, special = eatsoul)

# Races
human = MagicClasses.Race("human", 0.6, 0.1, 0.6, 0.2, 0.5, 0.4, 0.4, 0.4, [])
elf = MagicClasses.Race("elf", 0.3, 0.5, 0.3, 0.5, 0.2, 0.5, 0.5, 0.5, [])

dragon = MagicClasses.Race("dragon", 0.6, 0.6, 0.6, 0.6, 0.6, 0.5, 0.2, 0.3, [firebreath])
nidhogg = MagicClasses.Race("nidhogg", 1, 1, 1, 1, 1, 1, 1, 1, [eatSoul])

# Jobs
knight = MagicClasses.Job("knight", 0.4, 0, 0.3, 0, 0.5, 0.1, 0.2, 0.2, [])
mage = MagicClasses.Job("mage", 0.1, 0.4, 0.1, 0.3, 0.1, 0.2, 0.1, 0.2, [fireball, teleport])

def person(job, race):
    pass
