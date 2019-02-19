import sys, pygame, fileinput, copy
from Modules import TacticsClasses, TacticsPresets, tacticsfunctions, xmlProcessing
pygame.init()

# Basic Values
box = [100, 100]
size = [700, 700]
black = 0, 0, 0
white = 255, 255, 255

area = [0, 0]

all = xmlProcessing.All
# Creates Grid
grid = []

for line in fileinput.input():
    grid += [line.rstrip("\n").split(",")]

# Creates Screen
screen = pygame.display.set_mode(size)

# Gets Tiles
tiles = []
tiles += list(all["tile"].values())

# Text Font
font = pygame.font.Font(None, 25)

# Creates Units
# name, job, race, stats, growthRates, location = [0,0], abilities = [], weapon = None, items = []
# unit1 = copy.deepcopy(TacticsClasses.Person("1", TacticsPresets.knight, TacticsPresets.human, [20, 20, 20, 20, 20, 20, 20, 20, 5], [.3, .3, .3, .3, .3, .3, .3, .3]))

units = []
units += all["unit"]
deadUnits = []

# Creates Enemies
# enemy1 = copy.deepcopy(TacticsPresets.humanKnightTemplateUnit("2", [3, 4]))

enemies = []
enemies += all["enemy"]
deadEnemies = []

# Creates Action choice
action = tacticsfunctions.Actions.SELECT
selected = None # Selected Unit

# Area selected unit can move to
moveTo = []

# Unit's abilities
usableAbilities = []
targets = []
abilityUsed = 0
usableRange = []

spot = 25 # Spot from bottom to display usableAbilities
menu = pygame.Surface((300, 400))

while True:
    # Gets events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tacticsfunctions.end() # Ends program in terminal
        if event.type == pygame.KEYDOWN:

            # Change back to SELECT
            if event.key == pygame.K_ESCAPE:
                action = tacticsfunctions.Actions.SELECT

            # Ends turn
            if event.key == pygame.K_RETURN:
                tacticsfunctions.nextTurn(units, enemies, deadUnits, deadEnemies, grid, tiles)

            # Scroll screen around
            if action != tacticsfunctions.Actions.ABILITY:
                if event.key == pygame.K_UP:
                    area[1] += .2
                if event.key == pygame.K_RIGHT:
                    area[0] -= .2
                if event.key == pygame.K_DOWN:
                    area[1] -= .2
                if event.key == pygame.K_LEFT:
                    area[0] += .2
            else:
                if event.key == pygame.K_UP and abilityUsed > 0:
                    abilityUsed -= 1
                    targets = []
                    usableRange = tacticsfunctions.usableArea(selected, usableAbilities[abilityUsed], grid, tiles)
                if event.key == pygame.K_DOWN and abilityUsed < len(usableAbilities)-1:
                    abilityUsed += 1
                    targets = []
                    usableRange = tacticsfunctions.usableArea(selected, usableAbilities[abilityUsed], grid, tiles)

            # Choose action
            if action == tacticsfunctions.Actions.CHOOSE:
                if event.key == pygame.K_s:
                    action = tacticsfunctions.Actions.SELECT

                if event.key == pygame.K_m and selected.turnStage < 1:
                    action = tacticsfunctions.Actions.MOVE
                    moveTo = tacticsfunctions.moveAble(selected, grid, enemies, tiles) # Shows where unit can be moved to

                if event.key == pygame.K_a and selected.turnStage < 2:
                    action = tacticsfunctions.Actions.ABILITY
                    usableAbilities = selected.getAbilities()
                    targets = []
                    abilityUsed = 0
                    usableRange = tacticsfunctions.usableArea(selected, usableAbilities[abilityUsed], grid, tiles)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Mouse buttons

            # Gets location of mouse (adjusted for scroll)
            location = [int((event.pos[0]-area[0]*100)//100), int((event.pos[1]-area[1]*100)//100)]
            if action == tacticsfunctions.Actions.SELECT: # Select Unit
                for i in units:
                    if (i.location == location):
                        selected = i
                        action = tacticsfunctions.Actions.CHOOSE
                        break

            elif action == tacticsfunctions.Actions.MOVE: # Move Unit
                if location in moveTo:
                    tacticsfunctions.move(selected, location, grid, enemies, tiles)
                    action = tacticsfunctions.Actions.SELECT

            elif action == tacticsfunctions.Actions.ABILITY:
                if location in usableRange:
                    targets += [location]
                    if len(targets) >= usableAbilities[abilityUsed].targets:
                        usableAbilities[abilityUsed].use(selected, targets, units, enemies, [grid, tiles])
                        tacticsfunctions.checkDead(units, enemies, deadUnits, deadEnemies)
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

    # Shows selected targets and ability range
    if action == tacticsfunctions.Actions.ABILITY:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if ((i+area[1])*100 < 700 and (i+area[1])*100 > -100): # If the spot is within the selected area
                    if ((j+area[0])*100 < 700 and (j+area[0])*100 > -100): # If the spot is within the selected area
                        if [j, i] in targets:
                            # Adjusts size of rectangle to fit in the correct spot
                            screen.fill((255, 0, 0), [max((j+area[0])*100, 0), max((i+area[1])*100, 0)] + [min((area[0] + j + 1)*100, 100), min((area[1] + i + 1)*100, 100)])
                        elif [j, i] in usableRange:
                            # Adjusts size of rectangle to fit in the correct spot
                            screen.fill((200, 0, 0), [max((j+area[0])*100, 0), max((i+area[1])*100, 0)] + [min((area[0] + j + 1)*100, 100), min((area[1] + i + 1)*100, 100)])

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
        # Shows move stage
        if i.turnStage == 1:
            screen.fill((200, 200, 200), [max((i.location[0]+area[0])*100, 0), max((i.location[1]+area[1])*100, 0)] + [min((area[0] + i.location[0] + 1)*100, 100), min((area[1] + i.location[1] + 1)*100, 100)])
        elif i.turnStage == 2:
            screen.fill((100, 100, 100), [max((i.location[0]+area[0])*100, 0), max((i.location[1]+area[1])*100, 0)] + [min((area[0] + i.location[0] + 1)*100, 100), min((area[1] + i.location[1] + 1)*100, 100)])

        # Highlights selected unit
        if action == tacticsfunctions.Actions.CHOOSE and selected == i:
            screen.fill((255, 175, 0), [max((selected.location[0]+area[0])*100, 0), max((selected.location[1]+area[1])*100, 0)] + [min((area[0] + selected.location[0] + 1)*100, 100), min((area[1] + selected.location[1] + 1)*100, 100)])

        screen.blit(i.img, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    # Draw enemies
    for i in enemies:
        screen.blit(i.img, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    # Draws available actions
    if action == tacticsfunctions.Actions.ABILITY:
        menu.fill(white)
        pygame.draw.rect(menu, black, [0, 0, 300, 400], 1)
        spot = 25
        for i in usableAbilities:
            if i == usableAbilities[abilityUsed]:
                menu.blit(font.render(i.name, True, (255, 0, 0)), [10, spot])
            else:
                menu.blit(font.render(i.name, True, black), [10, spot])
            spot += 50
        screen.blit(menu, [0, 700-300])

    # Draws everything to screen
    pygame.display.flip()
