import pygame
import os
class Carte(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/cardswipe/carte.png")#pygame.Surface((250,100))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.drag = False