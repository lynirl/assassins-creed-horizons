import pygame
import os
import random
import Utils
from sp_Carte import Carte
from Checkpoints import Checkpoint

class mj_carte():
    SWIPE_A = [pygame.image.load(os.path.dirname(__file__) + "/sprites/images/cardswipe/aSwipe.png"),
               pygame.image.load(os.path.dirname(__file__) + "/sprites/images/cardswipe/aSwipeOK.png")]

    SWIPE_B = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/cardswipe/bSwipe.png")
    def __init__(self, level, screen = pygame.display.set_mode((1024, 768))):
        self.m_level = level
        self.screen = screen

    def run_miniJeu(self):
        success = False
        clock = pygame.time.Clock()
        timer = 0
        MAX_TIME = Utils.getMaxTimeForLevel(10, self.m_level)
        TIMER_WIDTH = 600
        
        MID_X = 1024 / 2
        MID_Y = 768 / 2

        sprite_group = pygame.sprite.Group()
        carte = Carte(MID_X, MID_Y-100)
        sprite_group.add(carte)

        SLIDE_HEIGHT = MID_Y + 150

        checkpoints = Checkpoint((MID_X - 350, SLIDE_HEIGHT),(MID_X - 125, SLIDE_HEIGHT),
                                  (MID_X + 125, SLIDE_HEIGHT), (MID_X + 350, SLIDE_HEIGHT))
        
        swipeRectA = mj_carte.SWIPE_A[0].get_rect()
        print(id(swipeRectA))
        swipeRectA.centerx = (MID_X)
        swipeRectA.bottom = (SLIDE_HEIGHT)

        swipeRectB = mj_carte.SWIPE_B.get_rect()
        swipeRectB.centerx = (MID_X)
        swipeRectB.top = (SLIDE_HEIGHT)

        while (timer < MAX_TIME):
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and carte.rect.collidepoint(event.pos) and not carte.drag:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    carte.drag = True
                    carte.rect.center = (mouse_x, mouse_y)

                elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                        carte.drag = False
                        if (not success):
                            carte.rect.center = (MID_X, MID_Y-100)     

                elif (event.type == pygame.MOUSEMOTION and carte.drag):
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if (abs(SLIDE_HEIGHT - mouse_y) < 75):
                            carte.rect.center = (mouse_x, SLIDE_HEIGHT)
                        else:
                            carte.rect.center = (mouse_x, mouse_y)
                            checkpoints.index = 0
            overlap = [currCheck for currCheck in checkpoints.liste if (pygame.Rect(currCheck)).colliderect(carte.rect)]
            if (len(overlap) > 0):
                if id(overlap[0]) == id(checkpoints.liste[checkpoints.index]):
                    checkpoints.index += 1
                    if (checkpoints.index == len(checkpoints.liste)):
                        return True

            self.screen.fill("black")
            screen.blit(mj_carte.SWIPE_A[0], swipeRectA)
            # for cp in checkpoints.liste:
            #     pygame.draw.rect(screen, ("white"), cp)
            sprite_group.draw(self.screen)
            screen.blit(mj_carte.SWIPE_B, swipeRectB)

            barre_w = TIMER_WIDTH * (1-(timer/MAX_TIME))
            loading_bar_rect = pygame.Rect(MID_X-(TIMER_WIDTH/2), MID_Y-250, barre_w, 20)
            pygame.draw.rect(self.screen, "red", loading_bar_rect)
            
            
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
    