import pygame
import os
from mj_crous import mj_crous
from mj_carte import mj_carte
from mj_alarmClock import mj_alarmClock
from mj_velo import mj_velo

def startMenu(a_screen):
    BG = [pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG0.png")]#,
        #   pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG1.png"),
        #   pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG2.png"),
        #   pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG3.png"),
        #   pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG4.png"),
        #   pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG5.png"),
        #   pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG6.png"),
        #   pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG7.png")]


    inStartMenu = True
    surf = pygame.surface.Surface((1024,768))
    surf.fill("white")
    frame = 0
    time = 0
    while(inStartMenu and time < 6):
   
        a_screen.blit(surf, (0,0))
        if (frame == 2):
            frame = 0
        else:
            frame+=1
        time += pygame.time.Clock().tick(2) / 1000
    




def main():
    IMG_SUCCESS = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/succes.png")
    MID_X = 1024 / 2
    MID_Y = 768 / 2
    score = 0
    round = 1
    vies = 3


    
    while (round < 10 and vies > 0):
        mini_jeux = [mj_alarmClock(round, screen),
                     mj_velo(round, screen),
                     mj_carte(round,screen),
                     mj_crous(round, screen)]
        
        i = 0
        while (i < len(mini_jeux) and vies > 0):
            screen.fill("black")
            if (mini_jeux[i].run_miniJeu()):
                for j in range(1, 10):
                    img_temp = pygame.transform.scale(IMG_SUCCESS, ((j/10) *900, (j/10) *900))
                    rect = img_temp.get_rect()
                    rect.center = (MID_X, MID_Y)
                    screen.blit(img_temp, rect)
                    pygame.time.Clock().tick(60)
                    pygame.display.flip()
                pygame.time.wait(500)
            else:
                vies -=1
            score += 1
            i+=1
        round +=1

            
        

    pygame.quit()
    print("Cya")



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    startMenu(screen)
    main()
