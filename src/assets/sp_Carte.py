import pygame
import os
class Carte(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/carte.png")#pygame.Surface((250,100))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.drag = False