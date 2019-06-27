import sys, pygame, fileinput, copy
from Modules import TacticsClasses, tacticsfunctions, xmlProcessing, battleProcessing, Draw
pygame.init()

# Basic Values
box = [100, 100]
size = [1000, 800]
black = 0, 0, 0
white = 255, 255, 255

area = [0, 0]

all = xmlProcessing.All
battles = battleProcessing.start(all)
cBattleN = 0
cBattle = battles[cBattleN]

# Creates Grid
grid = copy.deepcopy(cBattle[0])

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
enemies += cBattle[1]
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

# Menu
menuSize = [300, 400]
spot = 25 # Spot from bottom to display usableAbilities
menu = pygame.Surface(menuSize) # Creates menu surface
page = 0 # Creates menu page
menu.set_alpha(200) # Makes menu transparent

# Transparent Surface - For things that need to be transparent like areas things need to move to
transparentSurface = pygame.Surface(size) # Creates surface with same dimensions as screen
transparentSurface.fill(white) # Completely fills it as white
transparentSurface.set_colorkey(white) # Makes white completely transparent
transparentSurface.set_alpha(150) # Makes it transparent

# Sets up units and enemies
for i in units + enemies:
    i.health = i.getStat("maxHealth", [grid,tiles])
    i.mana = i.getStat("maxMana", [grid,tiles])

def start():
    global cBattle, cBattleN, battles, grid, enemies, deadEnemies, action, selected, moveTo, units, usableAbilities, targets, abilityUsed, usableRange
    if cBattleN < len(battles)-1:
        cBattleN += 1
    else:
        cBattleN = 0
    cBattle = battles[cBattleN]

    # Creates Grid
    grid = copy.deepcopy(cBattle[0])

    # Creates Enemies
    for i in cBattle[1]:
        i.health = i.getStat("maxHealth", [grid, tiles])
        i.mana = i.getStat("maxMana", [grid, tiles])
    enemies = []
    enemies += cBattle[1]
    deadEnemies = []

    # Creates Action choice
    action = tacticsfunctions.Actions.SELECT
    selected = None # Selected Unit

    # Area selected unit can move to
    moveTo = []

    # Unit locations
    tx = 0
    for i in units:
        i.health = i.getStat("maxHealth", [grid, tiles])
        i.mana = i.getStat("maxMana", [grid, tiles])
        i.location = [tx, 0]
        tx += 1

    # Unit's abilities
    usableAbilities = []
    targets = []
    abilityUsed = 0
    usableRange = []


while True:
    # Gets events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tacticsfunctions.end() # Ends program in terminal
        if event.type == pygame.KEYDOWN:

            # Change back to SELECT
            if event.key == pygame.K_ESCAPE:
                action = tacticsfunctions.Actions.SELECT
                selected = None

            # Ends turn
            if event.key == pygame.K_RETURN:
                tacticsfunctions.nextTurn(units, enemies, deadUnits, deadEnemies, grid, tiles)
                if len(enemies) == 0:
                    start()

            # Scroll screen around
            if not pygame.key.get_mods() & pygame.KMOD_SHIFT:
                if event.key == pygame.K_UP:
                    area[1] += .5
                if event.key == pygame.K_RIGHT:
                    area[0] -= .5
                if event.key == pygame.K_DOWN:
                    area[1] -= .5
                if event.key == pygame.K_LEFT:
                    area[0] += .5
            else:
                if event.key == pygame.K_RIGHT:
                    page += 1
                if event.key == pygame.K_LEFT and page > 0:
                    page -= 1
                if action == tacticsfunctions.Actions.ABILITY:
                    if event.key == pygame.K_UP and abilityUsed > 0:
                        abilityUsed -= 1
                        targets = []
                        usableRange = tacticsfunctions.usableArea(selected, usableAbilities[abilityUsed], grid, tiles)
                    if event.key == pygame.K_DOWN and abilityUsed < len(usableAbilities)-1:
                        abilityUsed += 1
                        targets = []
                        usableRange = tacticsfunctions.usableArea(selected, usableAbilities[abilityUsed], grid, tiles)

            # Choose action
            if selected:
                if event.key == pygame.K_m and selected.turnStage <= 0.5:
                    action = tacticsfunctions.Actions.MOVE
                    moveTo = tacticsfunctions.moveAble(selected, grid, units, enemies, tiles) # Shows where unit can be moved to

                if event.key == pygame.K_a and selected.turnStage < 2:
                    usableAbilities = selected.getAbilities([grid, tiles])
                    if usableAbilities:
                        action = tacticsfunctions.Actions.ABILITY
                        targets = []
                        abilityUsed = 0
                        usableRange = tacticsfunctions.usableArea(selected, usableAbilities[abilityUsed], grid, tiles)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Mouse buttons

            # Gets location of mouse (adjusted for scroll)
            location = [int((event.pos[0]-area[0]*100)//100), int((event.pos[1]-area[1]*100)//100)]

            # Selects a unit
            if action == tacticsfunctions.Actions.SELECT:
                selected = None
                action = tacticsfunctions.Actions.SELECT
                for i in units + enemies:
                    if (i.location == location):
                        selected = i
                        break
            elif selected in units: # If a player unit has been selected
                if action == tacticsfunctions.Actions.MOVE: # Move Unit
                    if location in moveTo:
                        tacticsfunctions.move(selected, location, grid, units, enemies, tiles)
                        action = tacticsfunctions.Actions.SELECT
                        selected = None

                elif action == tacticsfunctions.Actions.ABILITY: # Use ability
                    if location in usableRange:
                        targets += [location]
                        if len(targets) >= usableAbilities[abilityUsed].targets:
                            usableAbilities[abilityUsed].use(selected, targets, units, enemies, [grid, tiles])
                            tacticsfunctions.checkDead(units, enemies, deadUnits, deadEnemies)
                            action = tacticsfunctions.Actions.SELECT
                            selected = None



    screen.fill(white) # Makes the screen white
    transparentSurface.fill(white) # Makes transparentSurface white

    # Draws grid
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if ((i+area[1])*100 < size[1] and (i+area[1])*100 > -100): # If the spot is within the selected area
                if ((j+area[0])*100 < size[0] and (j+area[0])*100 > -100): # If the spot is within the selected area

                    # Draws tile images
                    for k in tiles:
                        if grid[i][j] == k.key: # Finds correct tile
                            screen.blit(k.img, [(j+area[0])*100, (i+area[1])*100])
                            break

    # Shows where unit can be moved to
    if action == tacticsfunctions.Actions.MOVE:
        Draw.drawMoveArea(transparentSurface, size, area, grid, moveTo)

    # Shows selected targets and ability range
    if action == tacticsfunctions.Actions.ABILITY:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if ((i+area[1])*100 < size[1] and (i+area[1])*100 > -100): # If the spot is within the selected area
                    if ((j+area[0])*100 < size[0] and (j+area[0])*100 > -100): # If the spot is within the selected area
                        if [j, i] in targets:
                            # Adjusts size of rectangle to fit in the correct spot
                            transparentSurface.fill((255, 0, 0), [max((j+area[0])*100, 0), max((i+area[1])*100, 0)] + [min((area[0] + j + 1)*100, 100), min((area[1] + i + 1)*100, 100)])
                        elif [j, i] in usableRange:
                            # Adjusts size of rectangle to fit in the correct spot
                            transparentSurface.fill((200, 0, 0), [max((j+area[0])*100, 0), max((i+area[1])*100, 0)] + [min((area[0] + j + 1)*100, 100), min((area[1] + i + 1)*100, 100)])

    # Grid lines
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if ((i+area[1])*100 < size[1] and (i+area[1])*100 > -100): # If the spot is within the selected area
                if ((j+area[0])*100 < size[0] and (j+area[0])*100 > -100): # If the spot is within the selected area
                    pygame.draw.rect(screen, black, [(j+area[0])*100, (i+area[1])*100]+box, 1) # Draws grid lines

    Draw.drawUnits(units, enemies, screen, transparentSurface, area, selected)

    # Prepares menu
    menu.fill(white)
    pygame.draw.rect(menu, black, [0, 0] + menuSize, 1)

    # Draws available actions
    if action == tacticsfunctions.Actions.ABILITY:
        spot = 25
        for i in usableAbilities[page*6:(page+1)*6]:
            if i == usableAbilities[abilityUsed]:
                menu.blit(font.render(i.name, True, (255, 0, 0)), [10, spot])
            else:
                menu.blit(font.render(i.name, True, black), [10, spot])
            spot += 50

        # Shows mpCost, turnCost and
        menu.blit(font.render("MP: " + str(usableAbilities[abilityUsed].mpCost), True, black), [menuSize[0]-110, 10])
        menu.blit(font.render("TURN: " + str(usableAbilities[abilityUsed].turnCost), True, black), [menuSize[0]-110, 25])
        damage = usableAbilities[abilityUsed].baseDmg
        if usableAbilities[abilityUsed].dmgType == "physical":
            damage += selected.getStat("pAtk", [grid, tiles])
            damage *= usableAbilities[abilityUsed].multi
        elif usableAbilities[abilityUsed].dmgType == "magic":
            damage += selected.getStat("mAtk", [grid, tiles])
            damage *= usableAbilities[abilityUsed].multi
        else:
            damage *= usableAbilities[abilityUsed].multi
        menu.blit(font.render("DMG: " +  str(damage), True, black), [menuSize[0]-110, 40])

    # Shows stats
    if selected and action != tacticsfunctions.Actions.ABILITY:
        spot = 25
        if page == 0:
            menu.blit(font.render(str(selected.name), True, black), [10, spot])
            spot += 50
            menu.blit(font.render(str(selected.job.name), True, black), [10, spot])
            spot += 50
            menu.blit(font.render(str(selected.race.name), True, black), [10, spot])
            spot += 50
            menu.blit(font.render("HP: " + str(selected.health) + "/" + str(selected.getStat("maxHealth", [grid, tiles])), True, black), [10, spot])
            spot += 50
            menu.blit(font.render("MP: " + str(selected.mana) + "/" + str(selected.getStat("maxMana", [grid, tiles])), True, black), [10, spot])
            spot += 50
        for i in [None, None, None, None, None, "pAtk", "mAtk", "dfce", "res", "agi", "skl", "mov", "TURN", "weapon"][page*6:(page+1)*6]:
            if i == "TURN":
                menu.blit(font.render(i + ": " + str(selected.turnStage), True, black), [10, spot])
            elif i == "weapon":
                if selected.weapon:
                    menu.blit(font.render(i + ": " + str(selected.weapon.name), True, black), [10, spot])
                else:
                    menu.blit(font.render(i + ": None", True, black), [10, spot])
            elif i:
                menu.blit(font.render(i + ": " + str(selected.getStat(i, [grid, tiles])), True, black), [10, spot])
            if i:
                spot += 50

    # Draws menu
    # if pygame.key.get_mods() & pygame.KMOD_SHIFT:
    screen.blit(menu, [0, size[1]-menuSize[0]])

    #Draws transparentSurface
    screen.blit(transparentSurface, [0, 0])

    # Draws everything to screen
    pygame.display.flip()
