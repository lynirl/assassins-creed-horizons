from AbstractMiniJeu import AbstractMiniJeu
import pygame
from Star import Star


class mj_crous(AbstractMiniJeu):
    #background = pygame.image.load("./src/wallpaper.jpeg")

    def __init__(self, level):
        self.m_level = level

    def run_miniJeu(self):
        background = pygame.image.load("./src/wallpaper.jpg")
        clock = pygame.time.Clock()
        running = True
        timer = 0

        sprite_group = pygame.sprite.Group()
        stars = [Star(10, 10), Star(100, 100)]
        for star in stars:
            sprite_group.add(star)

        while (running and timer < 500):
            screen.blit(background, (timer*5,timer*2))
            sprite_group.draw(screen)
            pygame.display.flip()

            timer +=1
            clock.tick(60)
        return True

    
if __name__ == "__main__":
    print("Hello, World !")
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_crous(1)
    print("Resultat du mini jeu: ", obj.run_miniJeu())


    pygame.quit()
    print("Ok")
    