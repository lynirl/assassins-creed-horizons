import pygame
from mj_crous import mj_crous
from mj_carte import mj_carte
from mj_alarmClock import mj_alarmClock
from mj_velo import mj_velo

def main():
    score = 0
    round = 1
    vies = 3


    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    print("here")
    while (round < 10 and vies > 0):
        print("there")
        mini_jeux = [mj_alarmClock(round, screen),
                     mj_velo(round),
                     mj_carte(round),
                     mj_crous(round)]
        
        i = 0
        while (i < len(mini_jeux) and vies > 0):
            print("damn")
            if (mini_jeux[i].run_miniJeu()):
                #afficher c gagne
                print("OK")
            else:
                vies -=1
            score += 1
            i+=1
        round +=1

            
        

    pygame.quit()
    print("Cya")



if __name__ == "__main__":
    main()