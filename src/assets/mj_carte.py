from AbstractMiniJeu import AbstractMiniJeu
import pygame
from sp_Carte import Carte
import random
import Utils


class mj_crous(AbstractMiniJeu):

    def __init__(self, level):
        self.m_level = level

    def run_miniJeu(self):
        clock = pygame.time.Clock()
        timer = 0
        max_time = 20#Utils.getMaxTimeForLevel(10, self.m_level)
        timer_width = 600
        
        mid_x = screen.get_width() / 2
        mid_y = screen.get_height() / 2

        sprite_group = pygame.sprite.Group()
        carte = Carte(mid_x, mid_y-100)
        sprite_group.add(carte)
    
        while (timer < max_time):
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and carte.rect.collidepoint(event.pos) and not carte.drag:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    carte.drag = True
                    carte.rect.center = (mouse_x, mouse_y)

                elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                        carte.drag = False

                elif (event.type == pygame.MOUSEMOTION and carte.drag):
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        carte.rect.center = (mouse_x, mouse_y)
                


            screen.fill("black")
            #^ screen.blit du background
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

    obj = mj_crous(1)
    print("Resultat du mini jeu: ", obj.run_miniJeu())

    # for i in range(1,10):
    #     obj = mj_crous(i)
    #     print(f"Resultat du mini jeu: {obj.run_miniJeu()}")


    pygame.quit()
    print("Ok")
    