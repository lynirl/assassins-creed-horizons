import math
import pygame
import Utils
from AbstractMiniJeu import AbstractMiniJeu

class mj_velo(AbstractMiniJeu):
    def __init__(self,level):
        self.m_level = level
        super().__init__()

    def erreur(self, screen):

        fondv = pygame.image.load("./src/assets/fondv.png")
        tombe = pygame.image.load("./src/assets/tombe.png")
        envelo = pygame.image.load("./src/assets/envelo.png")
        fond_x = 0

        print("erreur")
        screen.blit(fondv, (fond_x, 0))
        pygame.display.flip()
        screen.blit(tombe, (512, 505))
        pygame.display.flip()
        pygame.time.delay(3000)
        screen.blit(fondv, (fond_x, 0))
        pygame.display.flip()
        screen.blit(envelo, (512, 505))
        pygame.display.flip()


    def run_miniJeu(self):
        pygame.init()
        #Timer
        clock = pygame.time.Clock()
        timer = 0
        max_time = 30#Utils.getMaxTimeForLevel(10,self.m_level)
        #Variables
        click = True
        parcours, ARRIVEE = 0, 20
        fond_x = 0
        fondv = pygame.image.load("./src/assets/fondv.png")
        tombe = pygame.image.load("./src/assets/tombe.png")
        envelo = pygame.image.load("./src/assets/envelo.png")

        # Initialisation de l'écran
        screen = pygame.display.set_mode((1024, 768))

        while parcours<ARRIVEE and timer < max_time:

            screen.blit(fondv, (fond_x, 0))
            screen.blit(envelo, (512, 505))
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (event.key==pygame.K_a and click) or (event.key==pygame.K_z and not click):
                        click = not click
                        parcours+=1
                        fond_x -= 50
                        screen.blit(fondv,(fond_x,0))
                    else:
                        self.erreur(screen)

                    print(f"Touche : {event.key}")
            pygame.display.update()
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