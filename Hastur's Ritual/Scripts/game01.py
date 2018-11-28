import pygame
import time
from pytmx import load_pygame


pygame.init()


grass = 0
dirt = 1
stone = 2
water = 3


tilemap = [
        [grass, dirt, water, dirt, stone],
        [dirt, stone, dirt, water, dirt],
        [stone, grass, dirt, dirt, stone],
        [stone, grass, dirt, dirt, grass],
        [dirt, dirt, dirt, water, grass]
        ]


img = [pygame.image.load("tilepic1.png"),
       pygame.image.load("tilepic2.png"),
       pygame.image.load("tilepic3.png"),
       pygame.image.load("tilepic4.png")]


TILESIZE = 50
MAPWIDTH =  5
MAPHEIGHT = 5

a = display_width = 250
b = display_height = 250

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

player_width = 10
player_height = 10


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hastur's Ritual")


clock = pygame.time.Clock()



playerImg = pygame.image.load("Ready Player One test.png")



def dodraw(playerx, playery):
    gameDisplay.fill(white)
    for y in range(5):
        for x in range(5):
            gameDisplay.blit(img[tilemap[y][x]], (50*x,50*y))
        
    gameDisplay.blit(playerImg, (playerx,playery))
    pygame.display.update()
    clock.tick(60)
    
    

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0
    gameExit = False

    while not gameExit:
        xold = x
        yold = y
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -2
                elif event.key == pygame.K_RIGHT:
                    x_change = 2
                elif event.key == pygame.K_UP:
                    y_change = -2
                elif event.key == pygame.K_DOWN:
                    y_change = 2
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        
    
    
        x += x_change
        y += y_change
    
        
        dodraw(x,y)
    
        for row in range(MAPWIDTH):
            print            
            for column in range(MAPHEIGHT):
                if (x >= (column * TILESIZE) and x <= (column* TILESIZE) + TILESIZE) or ((x+29) >= (column * TILESIZE) and (x+29) <= (column* TILESIZE) + TILESIZE):
                    if (y >= (row * TILESIZE) and y <= (row* TILESIZE) + TILESIZE) or ((y+35) >= (row * TILESIZE) and (y+35) <= (row* TILESIZE) + TILESIZE):
                        if (tilemap[row][column] ==  grass) or (tilemap[row][column] ==  stone):
                            
                            x = xold
                            y = yold

        
        if (x >= display_width - player_width or x <= 0) or ((x+20) >= display_width - player_width or (x+20) <= 0):
                            x = xold
                            y = yold
            
        if (y >= display_height - player_width or y <= 0) or ((y+26) >= display_height - player_width or (y+26) <= 0):
                            x = xold
                            y = yold
           
       
        
game_loop()
pygame.quit()
quit()