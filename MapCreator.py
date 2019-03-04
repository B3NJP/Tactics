import sys, pygame, fileinput
from Modules import TacticsClasses, mapcreatorfunctions, xmlProcessing
pygame.init()
box = [100, 100]
size = [700, 700]
black = 0, 0, 0
white = 255, 255, 255

area = [0, 0]

grid = []

for line in fileinput.input():
    grid += [line.split(",")]

screen = pygame.display.set_mode(size)

all = xmlProcessing.All

# hill = pygame.transform.scale(pygame.image.load("../Assets/Tiles/hill.png"), box)
tiles = list(all["tile"].values())

selected = tiles[0]

spot = 25 # Spot from bottom to display usableAbilities
menu = pygame.Surface((300, 400)) # Creates menu surface
page = 0 # Creates menu page

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mapcreatorfunctions.end(grid)
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
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
    # screen.fill((black), box)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (i+area[1] < 700 and i+area[1] > -100):
                if (j+area[0] < 700 and j+area[0] > -100):
                    pygame.draw.rect(screen, black, [(j+area[0])*100, (i+area[1])*100]+box, 1)
                    for k in tiles:
                        if grid[i][j] == k.key:
                            screen.blit(k.img, [(j+area[0])*100, (i+area[1])*100])
                            break

    # Print menu
    screen.blit(menu, [0, 700-300])

    pygame.display.flip()
