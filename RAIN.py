import pygame, random
WHITE = (255,255,255)


class Rain(pygame.sprite.Sprite):

   def __init__(self,color,width,height):
      super().__init__()

      self.image = pygame.Surface([width,height])
      self.image.fill(WHITE)
      self.image.set_colorkey(WHITE)

      self.color = color
      self.width = width
      self.height = height

      pygame.draw.rect(self.image,color,[0,0,width,height])

      self.rect = self.image.get_rect()


   def fall(self,pixels):
       self.rect.y += pixels


      
