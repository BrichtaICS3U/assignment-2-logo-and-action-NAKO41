# ICS3U
# Assignment 2: Action
# <your name>

# adapted from http://www.101computing.net/getting-started-with-pygame/




# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
pygame.init()
from RAIN import Rain





#this will be the png or jpg background
background = pygame.image.load('clouds.jpg')#this is the background




# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
RAINBLUE = (3, 74, 236)
# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#this will be the code that creates the rain and places them in a list
rain_drops = pygame.sprite.Group()

for i in range(1000):
    rain = Rain(RAINBLUE,2,3)
    rain.rect.x = random.randint(2,398)
    rain.rect.y = random.randint(0,350)

    rain_drops.add(rain)#this adds every drop to the rainstorm
    

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    rain_drops.update()

    for rain in rain_drops:#this code makes the rain move and reset after it's hit the ground
        rain.fall(random.randint(5,10))
        if rain.rect.y > SCREENHEIGHT:#this rests the rain to the top
            rain.rect.y = 0
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)
    screen.blit(background,(0,0))

    # Queue different shapes and lines to be drawn




    #draw the sprites
    rain_drops.draw(screen)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
