import math
import pygame
import Utils
import os

class mj_velo(): 
    VELO_FS = []
    IMG_FONDV = pygame.image.load((os.path.dirname(__file__) + "/sprites/images/velo/veloBG.png"))
        
    def __init__(self,level, screen =pygame.display.set_mode((1024, 768))):
        self.m_level = level
        self.screen = screen
        mj_velo.VELO_FS = [pygame.image.load((os.path.dirname(__file__) + "/sprites/images/velo/velo1.png")),
               pygame.image.load((os.path.dirname(__file__) + "/sprites/images/velo/velo2.png")),
               pygame.image.load((os.path.dirname(__file__) + "/sprites/images/velo/velo3.png"))]

    def getNbStep(self, level):
        #return int( (-4 * math.e**(-0.2 * level)) + (0.6 * math.log(level, math.e)) + 20)
        return int( (-4 * math.e**(-0.5 * level)) + (1.5 * math.log(level, math.e)) + 25)

    def getTimeForLevelVelo(self, level):
        return ((math.e ** (2.75 - (0.1 * level))) * 0.5 ) + 1

    def run_miniJeu(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))

        #Timer
        clock = pygame.time.Clock()
        timer = 0
        MAX_TIME = self.getTimeForLevelVelo(self.m_level)
        print(MAX_TIME)
        TIMER_WIDTH = 600
        MID_X = self.screen.get_width() / 2
        MID_Y = self.screen.get_height() / 2

        velo_frame = 0

        #Variables
        click = True
        parcours = 0
        ARRIVEE = self.getNbStep(self.m_level)
        LONGUEUR_PAS = 75
        fond_x = -mj_velo.IMG_FONDV.get_rect().width + (ARRIVEE * LONGUEUR_PAS) + 1300
        print(ARRIVEE)

        while parcours<ARRIVEE and timer < MAX_TIME:

            self.screen.blit(mj_velo.IMG_FONDV, (fond_x, 0))
            self.screen.blit(mj_velo.VELO_FS[velo_frame], (0, self.screen.get_height() - 350))
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (event.key==pygame.K_a and click) or (event.key==pygame.K_z and not click):
                        click = not click
                        parcours+=1
                        fond_x -= LONGUEUR_PAS
                        self.screen.blit(mj_velo.IMG_FONDV,(fond_x,0))
                        velo_frame += 1
                        if (velo_frame == len(mj_velo.VELO_FS)):
                            velo_frame = 0

            barre_w = TIMER_WIDTH * (1-(timer/MAX_TIME))
            loading_bar_rect = pygame.Rect(MID_X-(TIMER_WIDTH/2), MID_Y-250, barre_w, 20)
            pygame.draw.rect(self.screen, "red", loading_bar_rect, 0)
            pygame.draw.rect(self.screen, (0,0,0, 120), loading_bar_rect, 4)

            pygame.display.flip()
            timer += clock.tick(30)/1000
        return (parcours == ARRIVEE)         


if __name__ == "__main__":
    print("Hello World !")
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_velo(1)
    print("Résultats mj : ", obj.run_miniJeu())

    pygame.quit()
    print("Ok")