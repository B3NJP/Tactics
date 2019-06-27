import pygame

def drawUnits(units, enemies, screen, transparentSurface, area, selected):
    # Draws units
    for i in units:
        # Shows move stage
        if i.turnStage >= 1:
            screen.fill((200, 200, 200), [max((i.location[0]+area[0])*100, 0), max((i.location[1]+area[1])*100, 0)] + [min((area[0] + i.location[0] + 1)*100, 100), min((area[1] + i.location[1] + 1)*100, 100)])
        elif i.turnStage >= 2:
            screen.fill((100, 100, 100), [max((i.location[0]+area[0])*100, 0), max((i.location[1]+area[1])*100, 0)] + [min((area[0] + i.location[0] + 1)*100, 100), min((area[1] + i.location[1] + 1)*100, 100)])

        # Unit image
        screen.blit(i.img, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    # Draw enemies
    for i in enemies:
        screen.blit(i.img, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    # Highlights selected unit
    if selected:
        transparentSurface.fill((255, 175, 0), [max((selected.location[0]+area[0])*100, 0), max((selected.location[1]+area[1])*100, 0)] + [min((area[0] + selected.location[0] + 1)*100, 100), min((area[1] + selected.location[1] + 1)*100, 100)])

def drawMoveArea(transparentSurface, size, area, grid, moveTo):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if ((i+area[1])*100 < size[1] and (i+area[1])*100 > -100): # If the spot is within the selected area
                if ((j+area[0])*100 < size[0] and (j+area[0])*100 > -100): # If the spot is within the selected area
                    if [j, i] in moveTo:
                        # Adjusts size of rectangle to fit in the correct spot
                        transparentSurface.fill((0, 0, 255), [max((j+area[0])*100, 0), max((i+area[1])*100, 0)] + [min((area[0] + j + 1)*100, 100), min((area[1] + i + 1)*100, 100)])
