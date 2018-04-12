import pygame, random
RainBlue = (3,74,236)
WHITE = (255,255,255)
 

class RAIN(pygame.sprite.Sprite):


   def __init__ (self,  color = RainBlue, width = 2, height = 2, x = random.randint(2,398)):
       super().__init__()


       self.image = pygame.Surface([width,height])
       self.image.fill(WHITE)
       self.image.set_colorkey(WHITE)


       pygame.draw.ellipse(self.image,color,[x,0,width,height])

       self.ellipse = self.image.get_ellipse()
       

    
