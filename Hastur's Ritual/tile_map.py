import pygame
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

    ### A list which contains the tile images for the dodraw-function ###
img = [pygame.image.load("Assests/Boden.jpg"),
       pygame.image.load("Assests/Grass.png"),
       pygame.image.load("Assests/Mauer.jpg"),
       pygame.image.load("Assests/Wasser.jpg")]