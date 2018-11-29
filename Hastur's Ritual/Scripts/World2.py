import pygame
import time
from pytmx import load_pygame


pygame.init()


    ### Hier eine Liste, für die dodraw-Funktion ###

img = [pygame.image.load("Assests/Boden.jpg"),
       pygame.image.load("Assests/Grass.png"),
       pygame.image.load("Assests/Mauer.jpg"),
       pygame.image.load("Assests/Wasser.jpg")]

    ### Zuordnung der Tile-Bezeichnungen ###
floor = 0
grass = 1
wall = 2
water = 3


#Die Tile-Map als Liste im bezug auf die Zuordnung der Tiles ###

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

    ### Welche Tiles lösen eine Kollision aus? ###

kollisionlist = (wall, water)

    ### Größe der Tiles und die Größe der Map in Tiles  in Pixeln ###
TILESIZE = 50
MAPWIDTH =  len(tilemap[1])
MAPHEIGHT = len(tilemap)


    ### Fenster-Größe ###
display_width = TILESIZE * MAPWIDTH
display_height = TILESIZE * MAPHEIGHT



    ### Größe des Spielers in Pixeln ###
player_width = 29
player_height = 35
    ### Aktivierte Farben fürs Programieren von Objekten
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

    ### Eigenschaften des PyGame-Fensters ###
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hastur's Ritual")


    ### Initialisierung der System Uhr ###
clock = pygame.time.Clock()


    ### Spieler-Grafik laden ###
playerImg = pygame.image.load("Assests/Ready-Player-One-UP1.png")



    
### Spiel zeichnen, aktivierung der Tiles in Reihe,Form und Funktion ###
def dodraw(playerx, playery):
    gameDisplay.fill(white)
    for y in range(MAPHEIGHT):
        for x in range(MAPWIDTH):
            gameDisplay.blit(img[int(tilemap[y][x])], (TILESIZE*x,TILESIZE*y))
        
    gameDisplay.blit(playerImg, (playerx,playery))
    pygame.display.update() #Aktualiesiere den Bildschirm
    clock.tick(60) #Maximale FPS begrenzung: 60FPS
    
### Text-Ausgabe-Aktiviert ###
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


### Text Form,Größe,Farbe und Position [Text-Objects] ###
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update() #Aktualiesiere den Bildschirm
    
    time.sleep(2) #Text 2 Sekunden lang anzeigen
    
    game_loop() #Gameschleife starten



### Die Game-Schleife ###
def game_loop():
    x = (display_width * 0.45)    ### Startposition des Spielers
    y = (display_height * 0.88)

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
        
            if event.type == pygame.KEYUP:     ### Beim Loslassen der Taste hört die Funktion aus
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
          
        x += x_change     ### Spielerposition verändern
        y += y_change
    
        
        dodraw(x,y)    ### Hier wird das gesamte Spielfeld neu gezeichnet

        
            ### Kollisionsabfrage ###
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

            ### Ende der Kollisionsabfrage ###    
       
        
game_loop()   ###Ende der Game-Schleife###
pygame.quit() ###Pygame ordentlich schließen###
quit()        ###Programm beenden###