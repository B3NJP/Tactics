import pygame

def drawUnits(units, enemies, screen, transparentSurface, area, selected):
    # Draws units
    for i in units:
        # Shows move stage
        if i.turnStage >= 1:
            screen.fill((200, 200, 200), [max((i.location[0]+area[0])*100, 0), max((i.location[1]+area[1])*100, 0)] + [min((area[0] + i.location[0] + 1)*100, 100), min((area[1] + i.location[1] + 1)*100, 100)])
        elif i.turnStage >= 2:
            screen.fill((100, 100, 100), [max((i.location[0]+area[0])*100, 0), max((i.location[1]+area[1])*100, 0)] + [min((area[0] + i.location[0] + 1)*100, 100), min((area[1] + i.location[1] + 1)*100, 100)])

        # Highlights selected unit
        if action == tacticsfunctions.Actions.CHOOSE and selected == i:
            transparentSurface.fill((255, 175, 0), [max((selected.location[0]+area[0])*100, 0), max((selected.location[1]+area[1])*100, 0)] + [min((area[0] + selected.location[0] + 1)*100, 100), min((area[1] + selected.location[1] + 1)*100, 100)])

        # Unit image
        screen.blit(i.img, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])

    # Draw enemies
    for i in enemies:
        screen.blit(i.img, [(i.location[0]+area[0])*100, (i.location[1]+area[1])*100])
