import sys
from enum import Enum, auto

def move(person, location):
    person.location[0] = location[0]
    person.location[1] = location[1]

class Actions(Enum):
    CHOOSE = auto()
    SELECT = auto()
    MOVE = auto()
    ABILITY = auto()

def moveAble(person, grid, enemies, tiles):
    queue = [[person.location, person.mov]]
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
    while queue:
        current = queue.pop(0)
        usableRange += [current[0]]
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

    return usableRange

def nextTurn(units, enemies, deadUnits, deadEnemies):
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

def end():
    sys.exit()
