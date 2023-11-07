import math
import pygame
import Utils
from AbstractMiniJeu import AbstractMiniJeu

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
        parcours, ARRIVEE = 0, 10
        fond_x = 0
        fond = pygame.image.load("./src/assets/fondv.png")
        tombe = pygame.image.load("./src/assets/tombe.jpeg")
        envelo = pygame.image.load("./src/assets/envelo.png")

        # Initialisation de l'écran
        screen = pygame.display.set_mode((1024, 768))

        while parcours<ARRIVEE and timer < max_time:

            screen.blit(fond, (fond_x, 0))
            screen.blit(envelo, (512, 505))
            pygame.display.flip()
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_a:
                            if click == 0:
                                parcours+=1
                                click = 1
                                fond_x -= 6 #Déplacer vers la droite
                                screen.blit(fondv.png,(fond_x,0))
                            else:
                                self.erreur()
                        if event.key==pygame.K_z:
                            if click == 1:
                                parcours+=1
                                click = 0
                                fond_x -= 6
                            else:
                                self.erreur()

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