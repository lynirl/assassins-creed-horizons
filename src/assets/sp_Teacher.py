import pygame
import os

class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/blanchon_crop.png")

        self.rect = self.image.get_rect()
        self.rect.center = (1024 / 2, 768 / 2)
        self.isWatching = False
        
    def update(self):
        self.rect.x += 2
    
class Student(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/carte.png")

        self.rect = self.image.get_rect()
        self.rect.center = (1024 / 2, 768 / 2)
        self.phoneOut = False