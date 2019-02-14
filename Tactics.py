import sys, pygame, fileinput
from Modules import TacticsClasses, TacticsPresets, tacticsfunctions
pygame.init()
box = [100, 100]
size = [700, 700]
black = 0, 0, 0
white = 255, 255, 255

area = [0, 0]

grid = []

for line in fileinput.input():
    grid += [line.rstrip("\n").split(",")]

screen = pygame.display.set_mode(size)

tiles = [
TacticsPresets.plain,
TacticsPresets.hill
]
p1 = pygame.transform.scale(pygame.image.load("Assets/Tiles/P1.png"), box)

selected = "0"

# name, job, race, stats, growthRates, location = [0,0], abilities = [], weapon = None, items = []
unit1 = TacticsClasses.Person("1", TacticsPresets.exampleJob, TacticsPresets.exampleRace, [10, 10, 10, 10, 10, 10, 10, 10, 5], [10, 10, 10, 10, 10, 10, 10, 10])

units = []
units += [unit1]

action = tacticsfunctions.Actions.SELECT
selected = None

moveTo = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tacticsfunctions.end()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                area[1] += .2
            if event.key == pygame.K_RIGHT:
                area[0] -= .2
            if event.key == pygame.K_DOWN:
                area[1] -= .2
            if event.key == pygame.K_LEFT:
                area[0] += .2
            if event.key == pygame.K_h:
                selected = "h"
            if event.key == pygame.K_0:
                selected = "0"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            location = [int((event.pos[0]-area[0]*100)//100), int((event.pos[1]-area[1]*100)//100)]
            if action == tacticsfunctions.Actions.SELECT:
                for i in units:
                    if (i.location[0] == location[0]) and (i.location[1] == location[1]):
                        selected = i
                        action = tacticsfunctions.Actions.MOVE
                        moveTo = tacticsfunctions.moveAble(selected, grid, tiles)
                        break
            elif action == tacticsfunctions.Actions.MOVE:
                tacticsfunctions.move(selected, location)
                action = tacticsfunctions.Actions.SELECT

    screen.fill(white)
    # screen.fill((black), box)
    if action == tacticsfunctions.Actions.MOVE:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if ((i+area[1])*100 < 700 and (i+area[1])*100 > -100):
                    if ((j+area[0])*100 < 700 and (j+area[0])*100 > -100):
                        if [j, i] in moveTo:
                            screen.fill((0, 0, 255), [max((j+area[0])*100, 0), max((i+area[1])*100, 0)] + [min((area[0] + j + 1)*100, 100), min((area[1] + i + 1)*100, 100)])

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if ((i+area[1])*100 < 700 and (i+area[1])*100 > -100):
                if ((j+area[0])*100 < 700 and (j+area[0])*100 > -100):
                    pygame.draw.rect(screen, black, [(j+area[0])*100, (i+area[1])*100]+box, 1)
                    for k in tiles:
                        if grid[i][j] == k.key:
                            screen.blit(k.img, [(j+area[0])*100, (i+area[1])*100])
                            break

    for i in units:
        screen.blit(p1, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    pygame.display.flip()
