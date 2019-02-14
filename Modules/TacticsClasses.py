import math, random, pygame

class Person:
    def __init__(self, name, job, race, stats, growthRates, location = [0,0], abilities = [], weapon = None, items = []):
        self.name = name
        self.job = job
        self.race = race

        self.maxHealth = stats[0]
        self.health = self.maxHealth
        print(stats[0])

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

    def loseHealth(self, ability, user, gridTiles):
        hitchance = random.random()
        hitrate = ((ability.skl + user.getStat("skl", gridTiles)) * ability.sklMulti * 4) - (self.getStat("agi", gridTiles) * 4)
        if hitchance <= hitrate/100:
            damage = ability.baseDmg
            if ability.dmgType == "physical":
                damage += user.getStat("pAtk", gridTiles)
                damage *= ability.multi
                damage -= self.getStat("dfce", gridTiles)
            elif ability.dmgType == "magic":
                damage += user.getStat("mAtk", gridTiles)
                damage *= ability.multi
                damage -= self.getStat("res", gridTiles)

            self.health -= max(damage, 0)
            print(self.name)
            print(self.health)
            print(damage)
            return damage

    def getStat(self, stat, gridTiles):
        val = 0
        val += getattr(self, stat) + getattr(self.job, stat) + getattr(self.race, stat)
        if self.weapon:
            val += getattr(self.weapon, stat)
        if stat == "dfce" or stat == "res":
            for i in gridTiles[1]:
                if gridTiles[0][self.location[1]][self.location[0]] == i.key:
                    val += getattr(i, stat)
                    break

        return val

    def getAbilities(self):
        abilities = []
        for i in self.abilities:
            if not i in abilities:
                abilities += [i]

        for i in self.job.abilities:
            if not i in abilities:
                abilities += [i]

        for i in self.race.abilities:
            if not i in abilities:
                abilities += [i]

        return abilities


class Ability:
    def __init__(self, name, type, dmgType, range = 1, targets = 1, baseDmg = 0, multi = 1, skl = 0, sklMulti = 1, mpCost = 0, cooldown = 0, special = None):
        self.name = name
        self.type = type

        self.dmgType = dmgType
        self.range = range
        self.targets = 1

        self.baseDmg = baseDmg
        self.multi = multi

        self.skl = skl
        self.sklMulti = sklMulti

        self.mpCost = mpCost
        self.cooldown = cooldown
        self.special = special

    def use(self, parent, target, units, enemies, gridTiles): # gridTiles is an array of both the grid and tiles
        if self.special:
            exec(self.special)
        else:
            for i in enemies:
                if i.location in target:
                    i.loseHealth(self, parent, gridTiles)


class Job:
    def __init__(self, name, maxHealth, maxMana, pAtk, mAtk, dfce, res, agi, skl, mov, abilities, growthRates):
        self.name = name
        self.maxhealth = maxHealth
        self.maxMana = maxMana

        self.pAtk = pAtk
        self.mAtk = mAtk

        self.dfce = dfce
        self.res = res

        self.agi = agi
        self.skl = skl
        self.mov = mov

        self.abilities = abilities

        self.growthRates = growthRates

class Race:
    def __init__(self, name, maxHealth, maxMana, pAtk, mAtk, dfce, res, agi, skl, mov, abilities, growthRates):
        self.name = name
        self.maxHealth = maxHealth
        self.maxMana = maxMana

        self.pAtk = pAtk
        self.mAtk = mAtk

        self.dfce = dfce
        self.res = res

        self.agi = agi
        self.skl = skl
        self.mov = mov

        self.abilities = abilities
        self.growthRates = growthRates

class Weapon:
    def __init__(self, name, pAtk, mAtk, dfce, res, agi, skl, abilities):
        self.name = name
        self.pAtk = pAtk
        self.mAtk = mAtk

        self.dfce = dfce
        self.res = res

        self.agi = agi
        self.skl = skl

        self.abilities = abilities

class Tile:
    def __init__(self, name, key, dfce, res, mov, img):
        self.name = name
        self.key = key

        self.dfce = dfce
        self.res = res
        self.mov = mov

        self.img = pygame.transform.scale(pygame.image.load(img), [100, 100])
