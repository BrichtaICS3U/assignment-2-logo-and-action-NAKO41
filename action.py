# ICS3U
# Assignment 2: Action
# <Nihcolas Sprott>
#!!there are times that the framerate of the code drops!!

# adapted from http://www.101computing.net/getting-started-with-pygame/




# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
pygame.init()
from RAIN import Rain
from CAR import Car


#this will be the png or jpg background
#https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_anRxwzGcZkKIBu7Z8ic-PZiSL-ArAGqXinrhqgq9LnOmr5j4
background = pygame.image.load('clouds.jpg')#this is the background


#this is where the sounds are inserted

#rain noises
#https://www.soundjay.com/rain-sound-effect.html 
pygame. mixer.pre_init(frequency = 44100, size =-16, channels = 1, buffer = 1000)
pygame.mixer.music.load('Rain.mp3')
pygame.mixer.music.play(-1)#-1 will loop the song, 0 will play once



# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
RAINBLUE = (3, 74, 236)
GREY = (37,37,37)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PINK = (255,114,255)
ORANGE = (255,100,0)
TURQUOISE = (0,255,255)


#list of the diffirent kinds of colours that the cars will change into
colorList = [BLUE,RED,GREEN,YELLOW,PINK,ORANGE,TURQUOISE]

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
    
#this code will create the car list and import a car in it
cars = pygame.sprite.Group()

car1 = Car(RED,)#this will be the car closer to the screen
car1.rect.x = 0
car1.rect.y = 365

car2 = Car(BLUE,)#this will be the farther car
car2.rect.x = 340
car2.rect.y = 350

cars.add(car2)
cars.add(car1)

#how fast each car will initialy go in the start
speed1 = 5
speed2 = 4
#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type==pygame.KEYDOWN:#this bit of code allows the user
            if event.key==pygame.K_SPACE:#to close the game with the space bar
                carryOn = False

    # --- Game logic goes here
    rain_drops.update()
    cars.update()

    for rain in rain_drops:#this code makes the rain move and reset after it's hit the ground
        rain.fall(random.randint(5,10))
        if rain.rect.y > 400:#this rests the rain to the top
            rain.rect.y = 0

    #cars logic
    car1.moveRight(speed1)
    car2.moveLeft(speed2)

    if car1.rect.x > 400:#this will change car 1 when it reaches the edge of the screen
        speed1 = random.randint(4,6)
        car1.rect.x = -60
        car1.changeColor(random.choice(colorList))

    if car2.rect.x < -60:#this will change car 1 when it reaces the edge of the screen
        speed2 = random.randint(4,6)
        car2.rect.x = 420
        car2.changeColor(random.choice(colorList))
        
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)
    screen.blit(background,(0,0))


   

    # Queue different shapes and lines to be drawn
    pygame.draw.rect(screen,GREY,[0,370,400,30])#this is the road
    pygame.draw.line(screen,YELLOW,[10,385],[30,385],4)#1 seperator line
    pygame.draw.line(screen,YELLOW,[40,385],[60,385],4)#2 seperator line
    pygame.draw.line(screen,YELLOW,[70,385],[90,385],4)#3 seperator line
    pygame.draw.line(screen,YELLOW,[100,385],[120,385],4)#4 seperator line
    pygame.draw.line(screen,YELLOW,[130,385],[150,385],4)#5 seperator line
    pygame.draw.line(screen,YELLOW,[160,385],[180,385],4)#6 seperator line
    pygame.draw.line(screen,YELLOW,[190,385],[210,385],4)#7 seperator line
    pygame.draw.line(screen,YELLOW,[220,385],[240,385],4)#8 seperator line
    pygame.draw.line(screen,YELLOW,[250,385],[270,385],4)#9 seperator line
    pygame.draw.line(screen,YELLOW,[280,385],[300,385],4)#10 seperator line
    pygame.draw.line(screen,YELLOW,[310,385],[330,385],4)#11 seperator line
    pygame.draw.line(screen,YELLOW,[340,385],[360,385],4)#12 seperator line
    pygame.draw.line(screen,YELLOW,[370,385],[390,385],4)#13 seperator line

   


    #draw the sprites
    cars.draw(screen)#draws the cars in the class
    rain_drops.draw(screen)#draws the rain
    
    
    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
