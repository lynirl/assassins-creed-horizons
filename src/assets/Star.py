import pygame
import os
class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load("./src/assets/sprites/images/stars.png")
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y