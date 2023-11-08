from AbstractMiniJeu import AbstractMiniJeu
import pygame

class mj_Phone(AbstractMiniJeu):

    def __init__(self, level):
        self.m_level = level
    
    def run_miniJeu(self):

        #clock du jeu
        clock = pygame.time.Clock()
        
        teacherState = False #false quand il regarde pas, true quand il regarde
        phoneState = False #false quand on l'utilise pas, true quand si

        
        #temps écoulé et temps max
        max_time = 30
        timer = 0
        timer_width = 600

        #coords du timer
        mid_x = screen.get_width() / 2
        mid_y = screen.get_height() / 2


        #barre de distraction
        progressBarMin = 0
        progressBarMax = 200
        progressBar = 0
        bar_height = 200

        

        #-----------------------------------

        while (timer < max_time): #tant que le jeu tourne
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN: #pour augmenter progressBar
                    progressBar += 10
                
            screen.fill("black") #la couleur de fond pour actualiser
            
            #tout pour la barre du timer
            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-300, barre_w, 20)

            #barre de distraction
            barre_d = bar_height * (1-(progressBar/progressBarMax)) #calculer sa hauteur
            dis_rect = pygame.Rect(50, 200, 20, barre_d) #son rectangle associé


            #affiche la barre du timer
            pygame.draw.rect(screen, "red", loading_bar_rect)

            #affiche la barre de distraction
            pygame.draw.rect(screen, "white", dis_rect)
            

            #60 fps
            clock.tick(60)

            pygame.display.flip()
            timer += (clock.tick(30)/1000) #incrémenter le timer

            #décrémenter la barre si on est pas déja au minimum
            if progressBar > progressBarMin:
                progressBar -= 2
        return False
    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_Phone(1)
    print("état:", obj.run_miniJeu())

    pygame.quit()
print("Ok")