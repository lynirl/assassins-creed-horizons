from AbstractMiniJeu import AbstractMiniJeu
import pygame
import random
import sp_Teacher

class mj_Phone(AbstractMiniJeu):

    def __init__(self, level):
        self.m_level = level
    
    def run_miniJeu(self):

        #clock du jeu
        clock = pygame.time.Clock()
        
        teacherChance = 0

        
        #temps écoulé et temps max
        max_time = 30
        timer = 0
        timer_width = 600

        #coords du timer
        mid_x = screen.get_width() / 2
        mid_y = screen.get_height() / 2


        #barre de distraction
        progressBarMin = 0
        progressBarMax = 500
        progressBar = 0
        bar_height = 5
        
        #items
        bg = pygame.image.load("./src/assets/sprites/images/classroom_1.png")
        teach = sp_Teacher.Teacher()
        student = sp_Teacher.Student()

        #sprite groups
        sprite_teacher = pygame.sprite.Group()
        sprite_student = pygame.sprite.Group()
        sprite_teacher.add(teach)
        sprite_student.add(student)

        #-----------------------------------

        while (timer < max_time): #tant que le jeu tourne
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN: #utiliser téléphone ou pas
                    student.phoneOut = True
                if event.type == pygame.MOUSEBUTTONUP:
                    student.phoneOut = False
            if student.phoneOut: #si on utilise le téléphone ça augmente progressBar
                progressBar += 200

            #-----------------------------------
            screen.blit(bg, (0, 0)) #la classe en background
            sprite_student.draw(screen) #spawnez svp
            sprite_teacher.update()
            sprite_teacher.draw(screen)

            #tout pour la barre du timer
            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-300, barre_w, 20)

            #barre de distraction
            barre_d = -(bar_height * (1-(progressBar/progressBarMax))) #calculer sa hauteur (+ parce que sinon ça va dans l'autre sens.......)
            dis_rect = pygame.Rect(50, 200, 20, barre_d) #son rectangle associé


            #affiche la barre du timer
            pygame.draw.rect(screen, "red", loading_bar_rect)

            #affiche la barre de distraction
            pygame.draw.rect(screen, "blue", dis_rect)
            
            #-----------------------------------

            #60 fps
            clock.tick(60)

            pygame.display.flip()
            timer += (clock.tick(30)/1000) #incrémenter le timer

            #-----------------------------------


            #gérer que le prof se retourne
            teacherChance = random.randint(1,100)
            if teacherChance == 3:
                teach.isWatching = True #il se retourne attention!!

            #si phone est sorti et le teacher regarde
            #if (student.phoneOut == True and teach.isWatching == True):
                #return False #c'est TERMINE

            #décrémenter la barre si on est pas déja au minimum
            if progressBar > progressBarMin:
                progressBar -= 100

        return False
    
        #-----------------------------------

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_Phone(1)
    print("état:", obj.run_miniJeu())

    pygame.quit()
print("Ok")