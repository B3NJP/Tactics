import sys, pygame, fileinput
from Modules import TacticsClasses, TacticsPresets, tacticsfunctions
pygame.init()

# Basic Values
box = [100, 100]
size = [700, 700]
black = 0, 0, 0
white = 255, 255, 255

area = [0, 0]


# Creates Grid
grid = []

for line in fileinput.input():
    grid += [line.rstrip("\n").split(",")]

# Creates Screen
screen = pygame.display.set_mode(size)

# Gets Tiles
tiles = [
TacticsPresets.plain,
TacticsPresets.hill
]

# Gets Unit Image
p1 = pygame.transform.scale(pygame.image.load("Assets/Tiles/P1.png"), box)
p2 = pygame.transform.scale(pygame.image.load("Assets/Tiles/P2.png"), box)

# Creates Units
# name, job, race, stats, growthRates, location = [0,0], abilities = [], weapon = None, items = []
unit1 = TacticsClasses.Person("1", TacticsPresets.knight, TacticsPresets.human, [10, 10, 10, 10, 10, 10, 10, 10, 5], [.3, .3, .3, .3, .3, .3, .3, .3])

units = []
units += [unit1]

enemy1 = TacticsPresets.humanKnightTemplateUnit("2", [3, 4])

enemies = []
enemies += [enemy1]

# Creates Action choice
action = tacticsfunctions.Actions.SELECT
selected = None # Selected Unit

# Area selected unit can move to
moveTo = []

while True:
    # Gets events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tacticsfunctions.end() # Ends program in terminal
        if event.type == pygame.KEYDOWN:

            # Scroll screen around
            if event.key == pygame.K_UP:
                area[1] += .2
            if event.key == pygame.K_RIGHT:
                area[0] -= .2
            if event.key == pygame.K_DOWN:
                area[1] -= .2
            if event.key == pygame.K_LEFT:
                area[0] += .2

            # Choose action
            if action == tacticsfunctions.Actions.CHOOSE:
                if event.key == pygame.K_m:
                    action = tacticsfunctions.Actions.MOVE
                    moveTo = tacticsfunctions.moveAble(selected, grid, tiles) # Shows where unit can be moved to

                if event.key == pygame.K_s:
                    action = tacticsfunctions.Actions.SELECT

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Mouse buttons

            # Gets location of mouse (adjusted for scroll)
            location = [int((event.pos[0]-area[0]*100)//100), int((event.pos[1]-area[1]*100)//100)]
            if action == tacticsfunctions.Actions.SELECT: # Select Unit
                for i in units:
                    if (i.location[0] == location[0]) and (i.location[1] == location[1]):
                        selected = i
                        action = tacticsfunctions.Actions.CHOOSE
                        break
            elif action == tacticsfunctions.Actions.MOVE: # Move Unit
                if location in moveTo:
                    tacticsfunctions.move(selected, location)
                    action = tacticsfunctions.Actions.SELECT

    screen.fill(white) # Makes the screen white

    # Shows where unit can be moved to
    if action == tacticsfunctions.Actions.MOVE:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if ((i+area[1])*100 < 700 and (i+area[1])*100 > -100): # If the spot is within the selected area
                    if ((j+area[0])*100 < 700 and (j+area[0])*100 > -100): # If the spot is within the selected area
                        if [j, i] in moveTo:
                            # Adjusts size of rectangle to fit in the correct spot
                            screen.fill((0, 0, 255), [max((j+area[0])*100, 0), max((i+area[1])*100, 0)] + [min((area[0] + j + 1)*100, 100), min((area[1] + i + 1)*100, 100)])

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

    # Draws units
    for i in units:
        screen.blit(p1, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    for i in enemies:
        screen.blit(p2, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    # Draws everything to screen
    pygame.display.flip()
