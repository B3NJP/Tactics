import sys, pygame
pygame.init()
box = [100, 100]
size = [700, 700]
black = 0, 0, 0
white = 255, 255, 255

area = [0, 0]

grid = [
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]
]

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                area[1] -= .2
            if event.key == pygame.K_RIGHT:
                area[0] += .2
            if event.key == pygame.K_DOWN:
                area[1] += .2
            if event.key == pygame.K_LEFT:
                area[0] -= .2
        if event.type == pygame.MOUSEBUTTONDOWN:
            grid[int((event.pos[1]-area[1]*100)//100)][int((event.pos[0]-area[0]*100)//100)] = 1
            # print((event.pos[0]-area[0]*100)//100)

    screen.fill(white)
    # screen.fill((black), box)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (i+area[1] < 700 and i+area[1] > -100):
                if (j+area[0] < 700 and j+area[0] > -100):
                    if grid[i][j] == 0:
                        pygame.draw.rect(screen, black, [(j+area[0])*100, (i+area[1])*100]+box, 1)
                    # else:
                        # pygame.draw.rect(screen, (50, 0, 0), [(j+area[0])*100, (i+area[1])*100]+box, 1)
    pygame.display.flip()
