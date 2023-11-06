import math
import pygame as py
from pynput import keyboard

class mj_velo(AbstractMiniJeu):
    def __init__(self):
        # Initialisation de la classe mj_velo
        super().__init__()
        # Autres initialisations spécifiques à mj_velo

    def erreur(screen):

        # Afficher tombé.png au premier plan
        screen.blit(img_tombe, (0, 0))
        pygame.display.flip()

        # Bloquer le jeu pendant 3 secondes
        pygame.time.delay(3000)

        # Retirer l'image tombé.png
        screen.fill((0, 0, 0))  # Remplir l'écran avec une couleur noire pour effacer l'image précédente
        pygame.display.flip()

        # Afficher envélo.png au premier plan
        screen.blit(img_velo, (0, 0))
        pygame.display.flip()


    def run_miniJeu(self):
        pygame.init()
        clock = pygame.time.Clock()
        click = 0
        parcours = 0
        ARRIVEE = 10
        tombe = pygame.image.load("tombe.png")
        envelo = pygame.image.load("envelo.png")

        # Initialisation de l'écran
        screen = pygame.display.set_mode((1024, 768))
        fond = pygame.image.load("fondv.png")
        velo = pygame.image.load("imagevelo.png")

        fond_x=0;

        #afficher_image_frame_1 (bg)
        #afficher imagevélo.png (fg)
        while parcours<ARRIVEE #and timer pas à 0:
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