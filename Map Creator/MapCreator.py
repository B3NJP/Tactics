import sys, pygame, fileinput, mapcreatorfunctions
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

hill = pygame.transform.scale(pygame.image.load("../Assets/Tiles/hill.png"), box)

selected = "0"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mapcreatorfunctions.end(grid)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                area[1] -= .2
            if event.key == pygame.K_RIGHT:
                area[0] += .2
            if event.key == pygame.K_DOWN:
                area[1] += .2
            if event.key == pygame.K_LEFT:
                area[0] -= .2
            if event.key == pygame.K_h:
                selected = "h"
            if event.key == pygame.K_0:
                selected = "0"
        if event.type == pygame.MOUSEBUTTONDOWN:
            location = [event.pos[0]-area[0]*100)//100, event.pos[1]-area[1]*100)//100]
            grid[int(location[0])][int(location[1])] = selected
            # print((event.pos[0]-area[0]*100)//100)

    screen.fill(white)
    # screen.fill((black), box)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (i+area[1] < 700 and i+area[1] > -100):
                if (j+area[0] < 700 and j+area[0] > -100):
                    pygame.draw.rect(screen, black, [(j+area[0])*100, (i+area[1])*100]+box, 1)
                    if grid[i][j] == "h":
                        screen.blit(hill, [(j+area[0])*100, (i+area[1])*100])
    pygame.display.flip()
