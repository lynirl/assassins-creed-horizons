from AbstractMiniJeu import AbstractMiniJeu
import pygame

class mj_crous(AbstractMiniJeu):
    #background = pygame.image.load("./src/wallpaper.jpeg")

    def __init__(self, level):
        self.m_level = level

    def run_miniJeu(self):
        background = pygame.image.load("./src/wallpaper.jpg")
        clock = pygame.time.Clock()
        running = True
        timer = 0
        screen.blit(background, (0,0))
        while (running and timer < 240):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                screen.fill("red")
                running = False
            pygame.display.flip()
            timer +=1
            clock.tick(60)
        return True
    

    
if __name__ == "__main__":
    print("Hello, World !")
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_crous(1)
    print("Resulatat du mini jeu: ", obj.run_miniJeu())


    pygame.quit()
    print("Ok")
    