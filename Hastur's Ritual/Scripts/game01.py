import pygame
import time
from settings import *
from pytmx import load_pygame


pygame.init()


    ### A list which contains the tile images for the dodraw-function ###
img = [pygame.image.load("Assests/Boden.jpg"),
       pygame.image.load("Assests/Grass.png"),
       pygame.image.load("Assests/Mauer.jpg"),
       pygame.image.load("Assests/Wasser.jpg")]


    ### Names of the tile types just for the ease of reading ###
floor = 0
grass = 1
wall = 2
water = 3


    ### The tile map as a list of strings, meanings of numbers see above ###

tilemap = ["2222222222222222222222222",
           "2222222220000022222222222",
           "2220000000000000000000222",
           "2220222220000022222202222",
           "2220222222222222222202222",
           "2000022222222222222202222",
           "2000022211111111222202222",
           "2000022211111111222202222",
           "2000000111111111100002222",
           "2000022211111111222202222",
           "2000022211111111222202222",
           "2220222222222222220000322",
           "2220222222200000000000332",
           "2220222222202222220000332",
           "2000000222202222222222222",
           "2000000220000033333332222",
           "2000000220000031111112222",
           "2222222222222221111122222"]


    ### Which tiles trigger collision ? ###
kollisionlist = (wall, water)


    ### Size of the tiles and the size of the map in tiles ###
TILESIZE = 50
MAPWIDTH =  len(tilemap[1])
MAPHEIGHT = len(tilemap)


    ### Window size in pixels ###
display_width = TILESIZE * MAPWIDTH
display_height = TILESIZE * MAPHEIGHT


    ### Color assignments for the creaton of text objects ###
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


    ### Properties of the pyGame-window ###
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hastur's Ritual")


    ### Initialization of the system clock ###
clock = pygame.time.Clock()


   
    ### Draw the game screen, activation of tiles in form und funktion ###

def dodraw(playerx, playery, playerdir):
    gameDisplay.fill(white)
    for y in range(MAPHEIGHT):
        for x in range(MAPWIDTH):
            gameDisplay.blit(img[int(tilemap[y][x])], (TILESIZE*x,TILESIZE*y))
        
    gameDisplay.blit(imgPlayer[playerdir], (playerx,playery))
    pygame.display.update()     # update display
    clock.tick(6000)      # maximum FPS-limit: 60FPS
    

    
    ### function for activating a text surface ###

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



    ### display text; set text font, size, color and position [text-objects] ###
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()     # update display
    
    time.sleep(2)        # show text for () seconds
    
    game_loop()      # (re)start game loop

    

    ### the major game loop ###

def game_loop():
    x = (display_width * 0.45)    # initial position of player
    y = (display_height * 0.88)
    playerdir = 0

    x_change = 0    # change variables for key triggered movements
    y_change = 0
    
    gameExit = False

    while not gameExit:
        xold = x    # old player position must be buffered
        yold = y
        x_change = 0    # change variables for key triggered movements
        y_change = 0
        
        event = pygame.event.get()    # key query
        #if event.type == pygame.QUIT:
        #    gameExit = True
            
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
                    playerdir = 2
                    x_change = -2
        if pressed[pygame.K_RIGHT]:
                    playerdir = 3
                    x_change = 2
        if pressed[pygame.K_UP]:
                    playerdir = 0
                    y_change = -2
        if pressed[pygame.K_DOWN]:
                    playerdir = 1
                    y_change = 2
        x += x_change     # adjust player position
        y += y_change
    
        
        dodraw(x,y, playerdir)
        
        
            ### Collision detection ###

        for row in range(MAPHEIGHT):               
            for column in range(MAPWIDTH):
                if (x >= (column * TILESIZE) and x <= (column* TILESIZE) + TILESIZE) or ((x+29) >= (column * TILESIZE) and (x+29) <= (column* TILESIZE) + TILESIZE):
                    if (y >= (row * TILESIZE) and y <= (row* TILESIZE) + TILESIZE) or ((y+35) >= (row * TILESIZE) and (y+35) <= (row* TILESIZE) + TILESIZE):
                        if (int(tilemap[row][column]) in kollisionlist):
                            
                            x = xold
                            y = yold
      
        if (x >= display_width - player_width or x <= 0):
                            x = xold
                            y = yold
            
        if (y >= display_height - player_height or y <= 0):
                            x = xold
                            y = yold
            ### end of collision detection ###    
       
        
game_loop()     ### Start the  game loop ###
pygame.quit()   ### close pyGame tidily ###
quit()          ### quit programm ###
