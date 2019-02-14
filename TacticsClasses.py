import math, random

class Person:
    def __init__(self, name, job, race, stats, growthRates, location = [0,0], abilities = [], weapon = None, items = []):
        self.name = name
        self.job = job
        self.race = race

        self.maxHealth = stats[0]
        self.health = self.maxHealth

        self.maxMana = stats[1]
        self.mana = self.maxMana

        self.pAtk = stats[2]
        self.mAtk = stats[3]

        self.dfce = stats[4]
        self.res = stats[5]

        self.agi = stats[6]
        self.skl = stats[7]

        self.mov = stats[8]

        self.location = location

        self.level = 1
        self.exp = 0

        self.growthRates = growthRates

        self.abilities = abilities

        self.weapon = weapon

        self.items = items

    def levelUp(self):
        self.level += 1
        self.maxHealth += math.floor(random.random() + self.growthRates[0] + self.race.growthRates[0] + self.job.growthRates[0])
        self.maxMana += math.floor(random.random() + self.growthRates[1] + self.race.growthRates[1] + self.job.growthRates[1])
        self.pAtk += math.floor(random.random() + self.growthRates[2] + self.race.growthRates[2] + self.job.growthRates[2])
        self.mAtk += math.floor(random.random() + self.growthRates[3] + self.race.growthRates[3] + self.job.growthRates[3])
        self.dfce += math.floor(random.random() + self.growthRates[4] + self.race.growthRates[4] + self.job.growthRates[4])
        self.res += math.floor(random.random() + self.growthRates[5] + self.race.growthRates[5] + self.job.growthRates[5])
        self.agi += math.floor(random.random() + self.growthRates[6] + self.race.growthRates[6] + self.job.growthRates[6])
        self.skl += math.floor(random.random() + self.growthRates[7] + self.race.growthRates[7] + self.job.growthRates[7])


class Ability:
    def __init__(self, name, type, dmgType, range = 0, dmg = 0, multi = 1, target = "single", sklMulti = 1, mpCost = 0, cooldown = 0, special = None):
        self.name = name
        self.type = type
        self.range = range

        self.dmg = dmg
        self.multi = multi
        self.target = target

        self.sklMulti = sklMulti

        self.dmgType = dmgType
        self.mpCost = mpCost
        self.special = special

    def __call__(self, atk, location, people, skl, mana, specialValues = []):
        if mana-self.mpCost >= 0:
            targets = [i for i in people if i.location == location]
            if self.dmgType == "special":
                self.special(specialValues, targets)
            else:
                damage = self.dmg + atk * self.multi
                for i in targets:
                    i.hpLoss(damage, self.dmgType, skl*self.sklMulti)
                    if self.special:
                        self.special(specialValues, i)
            return mana-self.mpCost
        else:
            return mana

class Job:
    def __init__(self, name, health, mana, pAtk, mAtk, dfce, res, agi, skl, abilities, growthRates):
        self.name = name
        self.health = health
        self.mana = mana

        self.pAtk = pAtk
        self.mAtk = mAtk

        self.dfce = dfce
        self.res = res

        self.agi = agi
        self.skl = skl

        self.abilities = abilities

        self.growthRates = growthRates

class Race:
    def __init__(self, name, health, mana, pAtk, mAtk, dfce, res, agi, skl, abilities, growthRates):
        self.name = name
        self.health = health
        self.mana = mana

        self.pAtk = pAtk
        self.mAtk = mAtk

        self.dfce = dfce
        self.res = res

        self.agi = agi
        self.skl = skl

        self.abilities = abilities
        self.growthRates = growthRates

class Weapon:
    def __init__(self, name, pAtk, mAtk, def, res, agi, skl, abilities):
        self.name = name
        self.pAtk = pAtk
        self.mAtk = mAtk

        self.agi = agi
        self.skl = skl

        self.abilities = abilities

class Tile:
    def __init__(self, name, def, res, mov, img):
        self.name = name
        self.def = def
        self.res = res
        self.mov = mov

        self.img = pygame.transform.scale(pygame.image.load(img), box)
