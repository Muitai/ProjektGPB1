import pygame
import time
from pytmx import load_pygame


pygame.init()


    ### Zuordnung der Tile-Bezeichnungen ###

grass = 0
dirt = 1
stone = 2
water = 3


    ### Die Tile-Map als Liste ###

tilemap = [
        [grass, dirt, water, dirt, stone],
        [dirt, stone, dirt, water, dirt],
        [stone, grass, dirt, dirt, stone],
        [stone, grass, dirt, dirt, grass],
        [dirt, dirt, dirt, water, grass]
        ]

    ### Hier eine Liste, für die dodraw-Funktion ###

img = [pygame.image.load("tilepic1.png"),
       pygame.image.load("tilepic2.png"),
       pygame.image.load("tilepic3.png"),
       pygame.image.load("tilepic4.png")]


    ### Größe der Tiles und die Größe der Map in Tiles ###

TILESIZE = 50
MAPWIDTH =  5
MAPHEIGHT = 5


    ### Fenster-Größe ###

display_width = TILESIZE * MAPWIDTH
display_height = TILESIZE * MAPHEIGHT


    ### Ein paar Farbbezeichnungen für spätere Verwendung ###

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


    ### Größe des Spielers in Pixeln ###

player_width = 29
player_height = 35


    ### Eigenschaften des PyGame-Fensters ###

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hastur's Ritual")


    ### Initialisierung der Uhr ###

clock = pygame.time.Clock()


    ### Spieler-Grafik laden ###

playerImg = pygame.image.load("Ready Player One test.png")



    
    ### Spiel zeichnen, alles ###

def dodraw(playerx, playery):
    gameDisplay.fill(white)
    for y in range(5):
        for x in range(5):
            gameDisplay.blit(img[tilemap[y][x]], (50*x,50*y))
        
    gameDisplay.blit(playerImg, (playerx,playery))
    pygame.display.update()
    clock.tick(60)
    

    ### Text-Ausgabe ###

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


    ### Erstellt eine Message mit Hilfe von Text-Objects ###

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()



    ### Die Game-Schleife ###

def game_loop():
    x = (display_width * 0.45)    ### Startposition des Spielers
    y = (display_height * 0.8)

    x_change = 0    ### Change Variablen für Bewegung bei Tastendruck
    y_change = 0
    
    gameExit = False

    while not gameExit:
        xold = x    ### alte Spielerposition wird zwischengespeichert
        yold = y
        
        for event in pygame.event.get():    ### Tastaturabfrage
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:     ### Bewegungstastendruck
                if event.key == pygame.K_LEFT:
                    x_change = -2
                elif event.key == pygame.K_RIGHT:
                    x_change = 2
                elif event.key == pygame.K_UP:
                    y_change = -2
                elif event.key == pygame.K_DOWN:
                    y_change = 2
        
            if event.type == pygame.KEYUP:     ### Beim Loslassen der Taste passiert nichts
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
          
        x += x_change     ### Spielerposition verändern
        y += y_change
    
        
        dodraw(x,y)    ### Hier wird das gesamte Spielfeld neu gezeichnet
    
        
        for row in range(MAPWIDTH):    ### Kollisionsabfrage
           
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

            ### Ende der Kollisionsabfrage ###    
       
        
game_loop()
pygame.quit()    ### Pygame ordentlich schließen
quit()