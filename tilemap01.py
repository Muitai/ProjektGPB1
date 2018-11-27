from pygame.locals import *
import pygame, sys

green = (40,255,30)
brown = (40,60,90)
red =  (155,20,30)
yellow = (0,155,155)

grass = 0
dirt = 1
lava = 2

colours = {
    grass: green,
    dirt: brown,
    lava: red,
    }

tilemap = [
        [grass,dirt,dirt,dirt, lava],
        [dirt,lava,dirt,dirt, dirt],
        [lava, grass,dirt,dirt, lava],
        [lava, grass,dirt,dirt, grass],
        [dirt,dirt,dirt,dirt,grass]

        ]

TILESIZE = 25
MAPWIDTH =  5
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))


while True:

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    print (mouse_x, mouse_y)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        DISPLAYSURF.fill((0,0,0));
        for row in range(MAPWIDTH):
            print            
            for column in range(MAPHEIGHT):
                color = colours[tilemap[row][column]];
                if mouse_x >= (column * TILESIZE) and mouse_x <= (column* TILESIZE) + TILESIZE:
                    if mouse_y >= (row * TILESIZE) and mouse_y <= (row* TILESIZE) + TILESIZE:
                        print (str(row) + " " + str(column))
                        color = yellow;                                                                                                            

                pygame.draw.rect(DISPLAYSURF, color, (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))


    pygame.display.update()
