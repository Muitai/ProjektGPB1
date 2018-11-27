import pygame


pygame.init()


grass = 0
dirt = 1
lava = 2
no = 3


colours = {
    grass: "C:/Users/m.wirth/Desktop/tilepic1.png",
    dirt: "C:/Users/m.wirth/Desktop/tilepic2.png",
    lava: "C:/Users/m.wirth/Desktop/tilepic3.png",
    no: "C:/Users/m.wirth/Desktop/tilepic4.png"
    }


tilemap = [
        [grass,dirt, no,dirt, lava],
        [dirt,lava,dirt, no, dirt],
        [lava, grass,dirt,dirt, lava],
        [lava, grass,dirt,dirt, grass],
        [dirt,dirt,dirt,dirt,grass]
        ]

display_width = 250
display_height = 250

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Hastur's Ritual")

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

img = [pygame.image.load("C:/Users/m.wirth/Desktop/tilepic1.png"),
       pygame.image.load("C:/Users/m.wirth/Desktop/tilepic2.png"),
       pygame.image.load("C:/Users/m.wirth/Desktop/tilepic3.png"),
       pygame.image.load("C:/Users/m.wirth/Desktop/tilepic4.png")]




while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    for x in range(5):
        for y in range(5):
            gameDisplay.blit(img[tilemap[x][y]], (50*x,50*y))
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()