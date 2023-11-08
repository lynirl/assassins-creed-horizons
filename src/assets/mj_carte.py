from AbstractMiniJeu import AbstractMiniJeu
import pygame
from sp_Carte import Carte
import random
import Utils
from Checkpoints import Checkpoint

class mj_carte(AbstractMiniJeu):

    def __init__(self, level):
        self.m_level = level

    def run_miniJeu(self):
        success = False
        clock = pygame.time.Clock()
        timer = 0
        max_time = Utils.getMaxTimeForLevel(10, self.m_level)
        timer_width = 600
        
        mid_x = screen.get_width() / 2
        mid_y = screen.get_height() / 2

        sprite_group = pygame.sprite.Group()
        carte = Carte(mid_x, mid_y-100)
        sprite_group.add(carte)

        slide_height = mid_y + 150

        checkpoints = Checkpoint((mid_x - 350, slide_height),(mid_x - 125, slide_height),
                                  (mid_x + 125, slide_height), (mid_x + 350, slide_height))

        while (timer < max_time):
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and carte.rect.collidepoint(event.pos) and not carte.drag:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    carte.drag = True
                    carte.rect.center = (mouse_x, mouse_y)

                elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                        carte.drag = False
                        if (not success):
                            carte.rect.center = (mid_x, mid_y-100)     

                elif (event.type == pygame.MOUSEMOTION and carte.drag):
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if (abs(slide_height - mouse_y) < 75):
                            carte.rect.center = (mouse_x, slide_height)
                        else:
                            carte.rect.center = (mouse_x, mouse_y)
                            checkpoints.index = 0
            overlap = [currCheck for currCheck in checkpoints.liste if (pygame.Rect(currCheck)).colliderect(carte.rect)]
            if (len(overlap) > 0):
                if id(overlap[0]) == id(checkpoints.liste[checkpoints.index]):
                    checkpoints.index += 1
                    if (checkpoints.index == len(checkpoints.liste)):
                        return True

            screen.fill("black")
            # for cp in checkpoints.liste:
            #     pygame.draw.rect(screen, ("white"), cp)
            sprite_group.draw(screen)

            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-250, barre_w, 20)
            pygame.draw.rect(screen, "red", loading_bar_rect)
            
            
            pygame.display.update()
            
            timer += (clock.tick(30)/1000)
                    
        return False
    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_carte(1)
    print("Resultat du mini jeu: ", obj.run_miniJeu())

    # for i in range(1,10):
    #     obj = mj_crous(i)
    #     print(f"Resultat du mini jeu: {obj.run_miniJeu()}")


    pygame.quit()
    print("Ok")
    