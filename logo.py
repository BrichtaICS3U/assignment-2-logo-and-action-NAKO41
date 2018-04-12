# ICS3U
# Assignment 2: Logo
# <NICK SPROTT>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()
import math

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BEETSRED = (181, 16, 32)
PURP = (49, 7, 122)
LIGHTPURP = (79, 55, 122)
YELLOW = (242,161,0)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Eclips logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)#changed to background to black

    # Queue different shapes and lines to be drawn
    #i am drawing the eclipse logo
    pygame.draw.ellipse(screen,YELLOW,[2,0,400,400])#this is the arc 
    pygame.draw.ellipse(screen,WHITE,[30,0,400,400])#this circle is used to create the arc in the logo
    pygame.draw.ellipse(screen,PURP,[40,30,340,340])#this is the body circle
    pygame.draw.ellipse(screen,LIGHTPURP,[110,105,200,200])#mid light purple circle
    pygame.draw.rect(screen,PURP,[110,105, 200,100])#blocks half the light purple
    pygame.draw.rect(screen,WHITE,[39,150,400,20])#white line #1
    pygame.draw.rect(screen,WHITE,[39,190,400,20])#white line #2
    pygame.draw.rect(screen,WHITE,[39,230,400,20])#white line #3
    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
