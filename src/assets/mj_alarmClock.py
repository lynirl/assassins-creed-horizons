from AbstractMiniJeu import AbstractMiniJeu
import pygame

class mj_alarmClock(AbstractMiniJeu):

    def __init__(self, level):
        self.m_level = level
    
    def run_miniJeu(self):

        #clock du jeu
        clock = pygame.time.Clock()

        #temps écoulé et temps max
        max_time = 5
        timer = 0
        timer_width = 600

        #coords du timer
        mid_x = screen.get_width() / 2
        mid_y = screen.get_height() / 2

        #running?
        running = True
        dt = 0

        #position du rectangle
        rect_x = 50
        rect_y = 50

        #vitesse & direction
        rect_speed_x = 5
        rect_speed_y = 5

        #compteur de clicks
        compteur = 0

        #-----------------------------------

        while (timer < max_time): #tant que le jeu tourne
            for event in pygame.event.get(): #on parcourt les events en cours
                if event.type == pygame.QUIT: #si l'event est de type quit, alors on quitte le jeu (= quand on appuie sur la croix)
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos() #on récup la pos
                    if re.collidepoint(x, y):
                        compteur+=1
            
            #après 3 clicks on win
            if compteur == 3:
                return True

            
            #on bouge le rectangle en incrémentant ses coords avec sa vitesse
            rect_x += rect_speed_x
            rect_y += rect_speed_y

            #collisions avec les bords
            if rect_y + 100 > 768 or rect_y < 0: 
                rect_speed_y = -rect_speed_y #on part de l'autre coté
            if rect_x + 200 > 1024 or rect_x < 0:
                rect_speed_x = -rect_speed_x #la même ici
            
            screen.fill("black") #la couleur de fond

            #tout pour la barre
            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-250, barre_w, 20)
            
            #le rectangle
            re = pygame.draw.rect(screen, "white", [rect_x, rect_y, 200, 100])

            #afficher la barre au dessus et pas au dessous du rectangle 
            pygame.draw.rect(screen, "red", loading_bar_rect)

            #60 fps
            clock.tick(60)

            pygame.display.flip()
            timer += (clock.tick(30)/1000) #incrémenter le timer
        return False

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_alarmClock(1)
    print("état:", obj.run_miniJeu())

    pygame.quit()
    print("Ok")