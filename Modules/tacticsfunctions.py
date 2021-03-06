import sys
from enum import Enum, auto

def move(person, location, grid, units, enemies, tiles):
    if person.turnStage <= 0.5:
        if location in moveAble(person, grid, units, enemies, tiles):
            person.turnStage = 0.9
            person.location[0] = location[0]
            person.location[1] = location[1]

class Actions(Enum):
    SELECT = auto()
    MOVE = auto()
    ABILITY = auto()

def distanceFrom(loc, loc2):
    return abs(loc[0]-loc2[0]) + abs(loc[1]-loc2[1])

def moveAble(person, grid, units, enemies, tiles):
    queue = [[person.location, person.getStat("mov", [grid, tiles])]]
    moveTo = []
    while queue:
        current = queue.pop(0)
        potential = []

        potential += [
        [current[0][0]+1, current[0][1]],
        [current[0][0]-1, current[0][1]],
        [current[0][0], current[0][1]+1],
        [current[0][0], current[0][1]-1]
        ]

        for i in potential:
            if (i[1] >= 0 and i[1] < len(grid)) and (i[0] >= 0 and i[0] < len(grid[i[1]])):
                if not i in [j.location for j in enemies]:
                    tempTile = None
                    for j in tiles:
                        if grid[i[1]][i[0]] == j.key:
                            tempTile = j
                            break
                    if current[1] - tempTile.mov >= 0:
                        if not i in [j[0] for j in moveTo]:
                            queue += [[i, current[1] - tempTile.mov]]
                            if not i in [k.location for k in units]:
                                moveTo += [[i, current[1] - tempTile.mov]]
                        elif not i in [j[0] for j in moveTo if current[1] - tempTile.mov <= j[1]]:
                            queue += [[i, current[1] - tempTile.mov]]
                            for j in moveTo:
                                if j[0] == i:
                                    if current[1] - tempTile.mov > j[1]:
                                        j[1] = current[1] - tempTile.mov

    return [i[0] for i in moveTo]

def usableArea(person, ability, grid, tiles):
    queue = [[person.location, ability.range]]
    usableRange = []
    finalRange = []
    while queue:
        current = queue.pop(0)
        usableRange += [current[0]]
        if distanceFrom(current[0], person.location) >= ability.minRange:
            finalRange += [current[0]]
        potential = []

        potential += [
        [current[0][0]+1, current[0][1]],
        [current[0][0]-1, current[0][1]],
        [current[0][0], current[0][1]+1],
        [current[0][0], current[0][1]-1]
        ]

        for i in potential:
            if not i in usableRange:
                if (i[1] >= 0 and i[1] < len(grid)) and (i[0] >= 0 and i[0] < len(grid[i[1]])):
                    if current[1] - 1 >= 0:
                        queue += [[i, current[1] - 1]]

    return finalRange

def checkDead(units, enemies, deadUnits, deadEnemies):
    for i in units:
        if i.health <= 0:
            deadUnits += [i]
    for i in enemies:
        if i.health <= 0:
            deadEnemies += [i]
    for i in deadUnits:
        if i in units:
            units.remove(i)
    for i in deadEnemies:
        if i in enemies:
            enemies.remove(i)

def nextTurn(units, enemies, deadUnits, deadEnemies, grid, tiles):
    for i in enemies:
        i.turnStage = 0
    checkDead(units, enemies, deadUnits, deadEnemies)

    if units:
        for myself in enemies:
            exec(open(myself.ai).read())

    checkDead(units, enemies, deadUnits, deadEnemies)
    for i in units:
        i.turnStage = 0

def end():
    sys.exit()
