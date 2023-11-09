import pygame
import math
import random
import Utils
import os

import sp_PhonesSprites as sp_PhonesSprites

class mj_Phone():
    def __init__(self, level, screen):
        self.m_level = level
        self.screen = screen

    def getTimeForLevelPhone(self, level):
        return ((math.e ** (2.75 - (0.075 * level))) * 0.6) + 10
    
    def run_miniJeu(self):

        #clock du jeu
        clock = pygame.time.Clock()
        teacherChance = 2

        
        #temps écoulé et temps max
        #max_time = Utils.getMaxTimeForLevel(20, self.m_level)
        max_time = self.getTimeForLevelPhone(self.m_level)
        timer = 0
        TIMER_WIDTH = 600
        STEP = 75

        #coords du timer
        MID_X = self.screen.get_width() / 2
        MID_Y = self.screen.get_height() / 2


        #barre de distraction
        PROGRESSMIN = 0 #constantes min et max
        PROGRESSMAX = 9000
        
        currProgress = 0
        BARRE_MAX_HEIGHT = 400
        
        #items
        BG = pygame.image.load("./src/assets/sprites/images/phone/classroom_1.png")
        teach = sp_PhonesSprites.Teacher(570, 200)
        student = sp_PhonesSprites.Student(MID_X - 23, MID_Y + 64)
        bureau = sp_PhonesSprites.Bureau(MID_X - 61, MID_Y - 134)

        #sprite groups
    
        sprite_teach = pygame.sprite.Group()
        sprite_student = pygame.sprite.Group()
        sprite_bureau = pygame.sprite.Group()
        
        sprite_teach.add(teach)
        sprite_student.add(student)
        sprite_bureau.add(bureau)

        #-----------------------------------

        while (timer < max_time): #tant que le jeu tourne
            self.screen.blit(BG, (0, 0)) #la classe en background
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #utiliser téléphone ou pas
                    student.phoneOut = True

                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    student.phoneOut = False
        
            if student.phoneOut: #si on utilise le téléphone ça augmente progressBar
                sprite_student.draw(self.screen)
                currProgress += STEP
                if(currProgress > PROGRESSMAX):
                    currProgress = PROGRESSMAX



            #-----------------------------------
            if currProgress > PROGRESSMIN and not student.phoneOut and not teach.isWatching:
                currProgress -= STEP
                if (currProgress < PROGRESSMIN):
                    currProgress = PROGRESSMIN


            #Spotted
            if (teach.isWatching and student.phoneOut):
                currProgress -= 200
                if (currProgress < PROGRESSMIN):
                    currProgress = PROGRESSMIN


            
            sprite_teach.draw(self.screen) #spawnez svp
            sprite_bureau.draw(self.screen)

            #tout pour la barre du timer
            barre_w = TIMER_WIDTH * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(MID_X-(TIMER_WIDTH/2), MID_Y-300, barre_w, 20)
            #affiche la barre du timer
            pygame.draw.rect(self.screen, "red", loading_bar_rect)
            pygame.draw.rect(self.screen, (0,0,0, 120), loading_bar_rect, 4)


            #barre de distraction
            barre_currHeight = (BARRE_MAX_HEIGHT * (currProgress/PROGRESSMAX)) #calculer sa hauteur (+ parce que sinon ça va dans l'autre sens.......)
            dis_rect = pygame.Rect(50, 200, 20, barre_currHeight) #son rectangle associé
            bg_distraction = pygame.Rect(50, 200, 20, BARRE_MAX_HEIGHT) #son rectangle associé
            
            #affiche la barre de distraction
            pygame.draw.rect(self.screen, "grey", bg_distraction)
            pygame.draw.rect(self.screen, "blue", dis_rect)
            pygame.draw.rect(self.screen, "black", bg_distraction, 4)
            
            #-----------------------------------

            #60 fps
            clock.tick(30)

            pygame.display.flip()
            timer += (clock.tick(30)/1000) #incrémenter le timer

            #-----------------------------------


            #gérer que le prof se retourne
            if random.randint(1,200) <= teacherChance or teach.isWatching == True:
                sprite_teach.update()
            
            if (currProgress >= PROGRESSMAX):
                return True
        return False
    
        #-----------------------------------

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_Phone(10, screen)
    print("état:", obj.run_miniJeu())

    pygame.quit()
print("Ok")