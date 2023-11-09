import pygame
import os

class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/phone/blanchon_crop.png")
        self.duree = 0
        self.rect = self.image.get_rect()
        self.rect.center = ((1024 / 2) - 61, (768 / 2) - 200)
        self.isWatching = False

    def update(self): #TODO: nul
        while(self.duree < 200):
            #quand il se retourne il bouge
            self.isWatching = True
            self.rect.center = ((1024 / 2) - 250, (768 / 2) - 200)
            self.duree+=1
        #il revient a la normale
        self.rect.center = ((1024 / 2) - 61, (768 / 2) - 200)
        self.isWatching = False
        
    
class Student(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/phone/student.png")

        self.rect = self.image.get_rect()
        self.rect.center = ((1024 / 2) - 15, (768 / 2) + 82) #position du sprite
        self.phoneOut = False

class Bureau(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/phone/bureau.png")

        self.rect = self.image.get_rect()
        self.rect.center = ((1024 / 2) - 61, (768 / 2) - 134) #position du sprite
        self.phoneOut = False