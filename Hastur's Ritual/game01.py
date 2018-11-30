import pygame
import time
import random
from pytmx import load_pygame

from settings import *    # general settings, all player specs
from tile_map import *    # everything concerning the world map


pygame.init()   ### setup pyGame ### 
pygame.mixer.init()
    ### Initialization of the system clock ###
clock = pygame.time.Clock()



    ### monster class initializes and updates all monster attributes ###
class Mob(pygame.sprite.Sprite):
    def __init__(self):      # monster-postion is set up randomly on screen ###
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        randy = random.randrange(0, MAPWIDTH)
        randx = random.randrange(0, MAPHEIGHT)
        
        while int(tilemap[randx][randy]) in kollisionlist:   # check if monster in wall #
            randy = random.randrange(0, MAPWIDTH)
            randx = random.randrange(0, MAPHEIGHT)
        self.rect.y = 50 * randx
        self.rect.x = 50 * randy
               
        self.speedy = random.randrange(-2, 2)
        self.speedx = random.randrange(-2, 2)
        
    def update(self):      # for updating monster-position #
        self.rect.x += self.speedx
        self.rect.y += self.speedy



    ### Properties of the pyGame-window, sprite list and 'mobs' for monster spawning ###
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hastur's Ritual")
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()



    ### function for monster spawning ###
def mobspawn():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

   
    ### Draw the game screen, activation of tiles in form und funktion ###

def dodraw(playerx, playery, playerdir):
    gameDisplay.fill(white)
    for y in range(MAPHEIGHT):
        for x in range(MAPWIDTH):
            gameDisplay.blit(img[int(tilemap[y][x])], (TILESIZE*x,TILESIZE*y))
        
    gameDisplay.blit(imgPlayer[playerdir], (playerx,playery))
    all_sprites.draw(gameDisplay)
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
    x = (display_width * 0.45)    # initial position and direction of player
    y = (display_height * 0.88)
    playerdir = 0

    x_change = 0    # change variables for key triggered movements
    y_change = 0
    
    mobspawn()    ### spawn monster, add to monster-list ###
    mobspawn()    ### another one ###

    gameExit = False

    while not gameExit:
        xold = x    # old player position must be buffered
        yold = y
        x_change = 0    # change variables for key triggered movements
        y_change = 0
        
        event = pygame.event.get()    # key query
        if event == pygame.QUIT:
            gameExit = True
            
        pressed = pygame.key.get_pressed()   # the get_pressed method for continuous movement

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
    
        
        dodraw(x,y, playerdir)     ### draw everything with adjustments ###
        
        
            ### Collision detection ###

        for row in range(MAPHEIGHT):               
            for column in range(MAPWIDTH):
                if (x >= (column * TILESIZE) and x <= (column* TILESIZE) + TILESIZE) or ((x+29) >= (column * TILESIZE) and (x+29) <= (column* TILESIZE) + TILESIZE):
                    if (y >= (row * TILESIZE) and y <= (row* TILESIZE) + TILESIZE) or ((y+35) >= (row * TILESIZE) and (y+35) <= (row* TILESIZE) + TILESIZE):
                        if (int(tilemap[row][column]) in kollisionlist):
                            
                            x = xold    # buffered postions is set when collision occurs
                            y = yold
                            
        if (x >= display_width - player_width or x <= 0):  # check for screen-border collision
                            x = xold
                            y = yold
            
        if (y >= display_height - player_height or y <= 0):
                            x = xold
                            y = yold
            ### end of collision detection ###    
       
        
game_loop()     ### Start the  game loop ###
pygame.quit()   ### close pyGame tidily ###
quit()          ### quit programm ###
