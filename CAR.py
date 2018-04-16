import pygame
WHITE = (255,255,255)


class Car(pygame.sprite.Sprite):



    def __init__(self,color,width = 60,height = 50):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.color = color
        self.width = width
        self.height = height

        pygame.draw.rect(self.image,color,[15,0,30,10])#roof part of car
        pygame.draw.rect(self.image,color,[0,10,60,20])#body part of car
        pygame.draw.ellipse(self.image,(0,0,0),[10,25,10,10])#first wheel
        pygame.draw.ellipse(self.image,(0,0,0),[40,25,10,10])#second wheel


        self.rect = self.image.get_rect()



    def moveRight(self,pixels):#moves the car right
        self.rect.x += pixels

    def moveLeft(self,pixels):#moves the car left
        self.rect.x -= pixels

    def changeColor(self,color):#this function will change the colour of the car from a list of clours
        self.color = color
        pygame.draw.rect(self.image,self.color,[15,0,30,10])#roof part of car
        pygame.draw.rect(self.image,self.color,[0,10,60,20])#body part of car
        pygame.draw.ellipse(self.image,(0,0,0),[10,25,10,10])#first wheel
        pygame.draw.ellipse(self.image,(0,0,0),[40,25,10,10])#second wheel
        


        


    
