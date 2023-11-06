import pygame
import os
class Star(pygame.sprite.Sprite):
    good_path = "./src/assets/sprites/images/stars_w.png"
    bad_path = "./src/assets/sprites/images/stars.png"

    def __init__(self, x, y, right = False):
        pygame.sprite.Sprite.__init__(self)
        if right:
          self.image = pygame.transform.scale(pygame.image.load(Star.good_path), (64, 64))
        else:
            self.image = pygame.transform.scale(pygame.image.load(Star.bad_path), (64, 64))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y