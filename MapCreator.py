import sys, pygame, fileinput
from Modules import TacticsClasses, mapcreatorfunctions, xmlProcessing
pygame.init()
box = [100, 100]
size = [700, 700]
black = 0, 0, 0
white = 255, 255, 255

area = [0, 0]

# Creates Grid
grid = []

for line in fileinput.input():
    grid += [line.rstrip("\n").split(",")]

screen = pygame.display.set_mode(size)

all = xmlProcessing.All

# hill = pygame.transform.scale(pygame.image.load("../Assets/Tiles/hill.png"), box)
tiles = list(all["tile"].values())

# Text Font
font = pygame.font.Font(None, 25)

selectedNum = 0
selected = tiles[selectedNum]

spot = 25 # Spot from bottom to display usableAbilities
menu = pygame.Surface((300, 400)) # Creates menu surface
page = 0 # Creates menu page

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mapcreatorfunctions.end(grid)
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                if event.key == pygame.K_RIGHT:
                    page += 1
                if event.key == pygame.K_LEFT and page > 0:
                    page -= 1
                if event.key == pygame.K_UP and selectedNum > 0:
                    selectedNum -= 1
                    selected = tiles[selectedNum]
                if event.key == pygame.K_DOWN and selectedNum < len(tiles)-1:
                    selectedNum += 1
                    selected = tiles[selectedNum]
            else:
                if event.key == pygame.K_UP:
                    area[1] += .2
                if event.key == pygame.K_RIGHT:
                    area[0] -= .2
                if event.key == pygame.K_DOWN:
                    area[1] -= .2
                if event.key == pygame.K_LEFT:
                    area[0] += .2

        if event.type == pygame.MOUSEBUTTONDOWN:
            location = [(event.pos[0]-area[0]*100)//100, (event.pos[1]-area[1]*100)//100]
            grid[int(location[1])][int(location[0])] = selected.key
            # print((event.pos[0]-area[0]*100)//100)

    screen.fill(white)

    # Draws grid
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if ((i+area[1])*100 < 700 and (i+area[1])*100 > -100): # If the spot is within the selected area
                if ((j+area[0])*100 < 700 and (j+area[0])*100 > -100): # If the spot is within the selected area
                    pygame.draw.rect(screen, black, [(j+area[0])*100, (i+area[1])*100]+box, 1) # Draws grid lines

                    # Draws tile images
                    for k in tiles:
                        if grid[i][j] == k.key: # Finds correct tile
                            screen.blit(k.img, [(j+area[0])*100, (i+area[1])*100])
                            break

    menu.fill(white)
    pygame.draw.rect(menu, black, [0, 0, 300, 400], 1)

    spot = 25
    for i in tiles[page*6:(page+1)*6]:
        if i == selected:
            menu.blit(font.render(i.name, True, (255, 0, 0)), [10, spot])
        else:
            menu.blit(font.render(i.name, True, black), [10, spot])
        spot += 50

    menu.blit(selected.img, [300-110, 10])
    menu.blit(font.render(str(selected.dfce), True, black), [300-110, 110])
    menu.blit(font.render(str(selected.res), True, black), [300-110, 125])
    menu.blit(font.render(str(selected.mov), True, black), [300-110, 140])
    pygame.draw.rect(menu, black, [300-110, 10, 100, 100], 1)

    # Print menu
    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
        screen.blit(menu, [0, 700-300])

    pygame.display.flip()
