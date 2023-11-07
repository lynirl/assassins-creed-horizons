from AbstractMiniJeu import AbstractMiniJeu
import pygame
from Star import Star
import random
import Utils


class mj_crous(AbstractMiniJeu):

    def __init__(self, level):
        self.m_level = level

    def run_miniJeu(self):
        clock = pygame.time.Clock()
        running = True
        timer = 0
        #fonction de get time a faire
        max_time = 10
        timer_width = 600
        
        mid_x = screen.get_width() / 2
        mid_y = screen.get_height() / 2
        sprite_group = pygame.sprite.Group()
    
        while (running and timer < max_time):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                     for sprite in sprite_group:
                        if sprite.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            #sprite.kill()
                            return sprite.type

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
    