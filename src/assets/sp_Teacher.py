import pygame
import os

class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/blanchon_crop.png")
        self.duree = 0
        self.rect = self.image.get_rect()
        self.rect.center = (1024 / 2, 768 / 2)
        self.isWatching = False
        
    def update(self):
        self.rect.x += 2

    def stare(self):
        while(self.duree < 10):
            self.duree += 1
        duree = 0
    
class Student(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/cardswipe/carte.png")

        self.rect = self.image.get_rect()
        self.rect.center = (1024 / 2, 768 / 2)
        self.phoneOut = False