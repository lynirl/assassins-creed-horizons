import pygame
import random
import Utils

class mj_alarmClock():

    def __init__(self, level, screen = pygame.display.set_mode((1024, 768))):
        super().__init__()
        self.m_level = level
        self.screen = screen
    
    def run_miniJeu(self):

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
        rect_x = random.randint(0, self.screen.get_width() - 200)
        rect_y = random.randint(0, self.screen.get_height() - 100)
        re = pygame.rect.Rect([rect_x, rect_y, 200, 100])

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
            
            #après 3 clicks on win
            if compteur == 3:
                return True

            
            #on bouge le rectangle en incrémentant ses coords avec sa vitesse
            re.x += rect_speed_x
            re.y += rect_speed_y

            #collisions avec les bords
            if re.y + 100 > 768 or re.y < 0: 
                rect_speed_y = -rect_speed_y #on part de l'autre coté
            if re.x + 200 > 1024 or re.x < 0:
                rect_speed_x = -rect_speed_x #la même ici
            
            self.screen.fill("black") #la couleur de fond

            #tout pour la barre
            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-250, barre_w, 20)
            
            #le rectangle
            pygame.draw.rect(self.screen, "white", re)

            #afficher la barre au dessus et pas au dessous du rectangle 
            pygame.draw.rect(self.screen, "red", loading_bar_rect)

            #60 fps
            clock.tick(60)

            pygame.display.flip()
            timer += (clock.tick(30)/1000) #incrémenter le timer
        return False

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_alarmClock(10, screen)
    print("état:", obj.run_miniJeu())

    pygame.quit()
    print("Ok")