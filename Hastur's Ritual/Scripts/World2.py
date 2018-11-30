import pygame
import time
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


    ### Size of the player sprite in pixels ###
player_width = 29
player_height = 35


    ### Color assignments for the creaton of text objects ###
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


    ### Properties of the pyGame-window ###
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hastur's Ritual")


    ### Initialization of the system clock ###
clock = pygame.time.Clock()


    ### Load player image ###
playerImg = pygame.image.load("Assests/Ready-Player-One-UP1.png")


    
    ### Draw the game screen, activation of tiles in form und funktion ###

def dodraw(playerx, playery):
    gameDisplay.fill(white)
    for y in range(MAPHEIGHT):
        for x in range(MAPWIDTH):
            gameDisplay.blit(img[int(tilemap[y][x])], (TILESIZE*x,TILESIZE*y))
        
    gameDisplay.blit(playerImg, (playerx,playery))
    pygame.display.update()     # update display
    clock.tick(60)      # maximum FPS-limit: 60FPS
    

    
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

    x_change = 0    # change variables for key triggered movements
    y_change = 0
    
    gameExit = False

    while not gameExit:
        xold = x    # old player position must be buffered
        yold = y
        
        for event in pygame.event.get():    # key query
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:     # set change variables if a arrow key is pressed
                if event.key == pygame.K_LEFT:
                    x_change = -2
                elif event.key == pygame.K_RIGHT:
                    x_change = 2
                elif event.key == pygame.K_UP:
                    y_change = -2
                elif event.key == pygame.K_DOWN:
                    y_change = 2
        
            if event.type == pygame.KEYUP:     # here you could set a action to perform when key-up
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
          
        x += x_change     # adjust player position
        y += y_change
    
        
        dodraw(x,y)    # dodraw - draw all of the game screen anew

        
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
