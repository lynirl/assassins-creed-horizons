import pygame
import os

class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/blanchon_crop.png")
        self.duree = 0
        self.rect = self.image.get_rect()
        self.rect.center = ((1024 / 2) - 61, (768 / 2) - 200)
        self.isWatching = False
    
class Student(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/student.png")

        self.rect = self.image.get_rect()
        self.rect.center = ((1024 / 2) - 14, (768 / 2) + 68) #position du sprite
        self.phoneOut = False

class Bureau(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/bureau.png")

        self.rect = self.image.get_rect()
        self.rect.center = ((1024 / 2) - 61, (768 / 2) - 134) #position du sprite
        self.phoneOut = False