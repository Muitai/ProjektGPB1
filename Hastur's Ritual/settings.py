### general settings, especially player settings
import pygame

    ### Player speed ###
player_speed = 300
player_rot_speed = 250

    ### Size of the player sprite in pixels ###
player_width = 29
player_height = 35

    ### Load the images of the player sprite for all four directions in a list ### 
imgPlayer = [pygame.image.load("Assests/Ready-Player-One-UP1.png"),
             pygame.image.load("Assests/Ready-Player-One-Down.png"),
             pygame.image.load("Assests/Ready-Player-One-Left.png"),
             pygame.image.load("Assests/Ready-Player-One-Right.png")]


    ### Color assignments for the creaton of text objects ###
white  = (255, 255, 255)
black  = (  0,   0,   0)
red    = (255,   0,   0)
green  = (  0, 255,   0)
blue   = (  0,   0, 255)
yellow = (255, 255,   0)
