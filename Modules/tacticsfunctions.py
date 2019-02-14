import sys
from enum import Enum, auto

def move(person, location):
    person.location[0] = location[0]
    person.location[1] = location[1]

class Actions(Enum):
    MOVE = auto()
    SELECT = auto()
    CHOOSE = auto()

def moveAble(person, grid, tiles):
    queue = [[person.location, person.mov]]
    moveTo = []
    while queue:
        current = queue.pop(0)
        moveTo += [current[0]]
        potential = []

        potential += [
        [current[0][0]+1, current[0][1]],
        [current[0][0]-1, current[0][1]],
        [current[0][0], current[0][1]+1],
        [current[0][0], current[0][1]-1]
        ]

        for i in potential:
            if not i in moveTo:
                if (i[1] >= 0 and i[1] < len(grid)) and (i[0] >= 0 and i[0] < len(grid[i[1]])):
                    tempTile = None
                    for j in tiles:
                        if grid[i[1]][i[0]] == j.key:
                            tempTile = j
                            break
                    if current[1] - tempTile.mov >= 0:
                        queue += [[i, current[1] - tempTile.mov]]

    return moveTo

def end():
    sys.exit()
