import pygame
import os
import random
import Utils
from sp_alarmClock import AlarmClock

class mj_alarmClock():

    #constante pour le bg
    IMG_BG = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/reveil/reveil_bg.png")
    
    def __init__(self, level, screen = pygame.display.set_mode((1024, 768))):
        super().__init__()
        self.m_level = level
        self.screen = screen
    
    def run_miniJeu(self):

        #constantes pour le son
        THEME = pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/mj_reveilMain.mp3")
        CHANNEL_MJ = pygame.mixer.Channel(1)
        CHANNEL_MJ.play(THEME, loops=-1)
        
        #clock du jeu
        clock = pygame.time.Clock()

        #temps écoulé et temps max
        max_time = Utils.getMaxTimeForLevel(12, self.m_level)
        timer = 0
        timer_width = 600

        #coords du timerr
        mid_x = self.screen.get_width() / 2
        mid_y = self.screen.get_height() / 2

        #position du rectangle
        rect_x = random.randint(200, self.screen.get_width() - 200)
        rect_y = random.randint(200, self.screen.get_height() - 100)

        sp_group = pygame.sprite.Group()
        reveil = AlarmClock(rect_x, rect_y)
        sp_group.add(reveil)
        re = reveil.rect

        #vitesse & direction
        rect_speed_x = random.randint(-1, -1) * (1.3**self.m_level)#random.randint(-1, -1) * (15 * (self.m_level / 10))
        rect_speed_y = random.randint(-1, -1) * (1.3**self.m_level)#random.randint(-1, -1) * (15 * (self.m_level / 10))

        #compteur de clicks
        compteur = 0

        #-----------------------------------

        while (timer < max_time): #tant que le jeu tourne
            for event in pygame.event.get(): #on parcourt les events en cours
                if event.type == pygame.QUIT: #si l'event est de type quit, alors on quitte le jeu (= quand on appuie sur la croix)
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos() #on récup la pos
                    if re.collidepoint(x, y):
                        compteur+=1
                        #pour jouer les différents sons du réveil
                        if compteur == 1:
                            Utils.play_sound_effect(pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/mj_reveil1.mp3"))
                        elif compteur == 2:
                            Utils.play_sound_effect(pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/mj_reveil2.mp3"))
                        elif compteur == 3:
                            Utils.play_sound_effect(pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/mj_reveil3.mp3"))
                            CHANNEL_MJ.stop()
                            return True
                        reveil.image = AlarmClock.STATES[compteur]
            
            #après 3 clicks on win

            
            #on bouge le rectangle en incrémentant ses coords avec sa vitesse
            re.x += rect_speed_x
            re.y += rect_speed_y

            #collisions avec les bords
            if re.y + 100 > 768 or re.y < 0: 
                rect_speed_y = -rect_speed_y #on part de l'autre coté
            if re.x + 200 > 1024 or re.x < 0:
                rect_speed_x = -rect_speed_x #la même ici
            
            self.screen.blit(mj_alarmClock.IMG_BG, (0,0))

            sp_group.draw(self.screen)

            #tout pour la barre
            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-250, barre_w, 20)
            pygame.draw.rect(self.screen, "red", loading_bar_rect)
            pygame.draw.rect(self.screen, (0,0,0, 120), loading_bar_rect, 4)
            #60 fps
            clock.tick(60)

            pygame.display.flip()
            timer += (clock.tick(30)/1000) #incrémenter le timer
        CHANNEL_MJ.stop()
        return False

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_alarmClock(10, screen)
    print("état:", obj.run_miniJeu())

    pygame.quit()
    print("Ok")