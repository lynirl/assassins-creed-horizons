import pygame
import os
import Utils

class Teacher(pygame.sprite.Sprite):
    WATCHING_POS = (447, 200)
    def __init__(self,x ,y ):
        pygame.sprite.Sprite.__init__(self)
        self.BASE_X = x
        self.BASE_Y = y
        self.image = pygame.image.load("./src/assets/sprites/images/phone/blanchon_crop.png")
        self.duree = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.BASE_X, self.BASE_Y)
        self.isWatching = False
        self.hasBeenPlayed = False

    def update(self):

        if(self.duree < 25):
            #quand il se retourne il bouge
            self.isWatching = True
            self.rect.center = (Teacher.WATCHING_POS)
            self.duree+=1
            if self.hasBeenPlayed == False: #si son n'a pas été joué
                Utils.play_sound_effect(pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/mj_phone_spotted.mp3")) #on joue
                self.hasBeenPlayed = True #et il est considéré comme joué
        else :
            #il revient a la normale
            self.rect.center = (self.BASE_X, self.BASE_Y)
            self.isWatching = False
            self.duree = 0
            self.hasBeenPlayed = False #le son peut être joué à nouveau
    
        
    
class Student(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/phone/student.png")

        self.rect = self.image.get_rect()
        self.rect.center = (x, y) #position du sprite
        self.phoneOut = False

class Bureau(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/assets/sprites/images/phone/bureau.png")

        self.rect = self.image.get_rect()
        self.rect.center = (x, y) #position du sprite
        self.phoneOut = False