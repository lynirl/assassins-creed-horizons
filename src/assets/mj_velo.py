import math
import pygame as py
from pynput import keyboard

class mj_velo(AbstractMiniJeu):
    def __init__(self,level):
        self.m_level = level
        super().__init__()

    def erreur(screen, tombe, envelo):

        # Afficher "tombe.png" au premier plan
        screen.blit(tombe, (0, 0))
        pygame.display.flip()

        # Bloquer le jeu pendant 3 secondes
        pygame.time.delay(3000)

        # Afficher l'image de premier plan "velo.png" à nouveau
        screen.blit(envelo, (0, 0))
        pygame.display.flip()



    def run_miniJeu(self):
        pygame.init()
        #Timer
        clock = pygame.time.Clock()
        timer = 0
        max_time = Utils.getMaxTimeForLevel(10,self.m_level)
        #Variables
        click = 0
        parcours = 0
        ARRIVEE = 10
        fond_x=0
        fin_jeu = False
        fond = pygame.image.load("fondv.png")
        tombe = pygame.image.load("tombe.png")
        envelo = pygame.image.load("envelo.png")

        # Initialisation de l'écran
        screen = pygame.display.set_mode((1024, 768))

        while parcours<ARRIVEE and timer < max_time:

            screen.blit(fond, (fond_x, 0))
            screen.blit(envelo, (0, 0))
            pygame.display.flip()

            if key.char == 'A' or key.char == 'a':
                if click == 0:
                    parcours+=1
                    click = 1
                    fond_x -= 6 #Déplacer vers la droite
                    screen.blit(fondv.png,(fond_x,0))
                else:
                    erreur()tombé
            if key.char == 'Z' or key.char == 'z':
                if click == 1:
                    parcours+=1
                    click = 0;
                    fond_x -= 6
                else:
                    erreur()           


if __name__ == "__main__":
    print("Hello World !")
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_crous(1)
    print("Résultats mj : ", obj.run_minijeu())

    pygame.quit()
    print("Ok")