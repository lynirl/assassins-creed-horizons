import pygame
import random
import sp_Teacher

class mj_Phone():

    def __init__(self, level, screen):
        self.m_level = level
        self.screen = screen
    
    def run_miniJeu(self):

        #clock du jeu
        clock = pygame.time.Clock()
        
        teacherChance = 0

        
        #temps écoulé et temps max
        max_time = 30
        timer = 0
        timer_width = 600

        #coords du timer
        mid_x = self.screen.get_width() / 2
        mid_y = self.screen.get_height() / 2


        #barre de distraction
        PROGRESSMIN = 0 #constantes min et max
        PROGRESSMAX = 500
        
        progressBar = 0
        bar_height = 50
        
        #items
        bg = pygame.image.load("./src/assets/sprites/images/phone/classroom_1.png")
        teach = sp_Teacher.Teacher()
        student = sp_Teacher.Student()
        bureau = sp_Teacher.Bureau()

        #sprite groups
    
        sprite_teach = pygame.sprite.Group()
        sprite_student = pygame.sprite.Group()
        sprite_bureau = pygame.sprite.Group()
        
        sprite_teach.add(teach)
        sprite_student.add(student)
        sprite_bureau.add(bureau)

        #-----------------------------------

        while (timer < max_time): #tant que le jeu tourne
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN: #utiliser téléphone ou pas
                    sprite_student.draw(screen)
                    student.phoneOut = True

                if event.type == pygame.MOUSEBUTTONUP:
                    student.phoneOut = False
            if student.phoneOut: #si on utilise le téléphone ça augmente progressBar
                progressBar += 100

            #-----------------------------------
            screen.blit(bg, (0, 0)) #la classe en background
            
            sprite_teach.draw(screen) #spawnez svp
            sprite_bureau.draw(screen)

            #tout pour la barre du timer
            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-300, barre_w, 20)

            #barre de distraction
            barre_d = -(bar_height * (1-(progressBar/PROGRESSMAX))) #calculer sa hauteur (+ parce que sinon ça va dans l'autre sens.......)
            dis_rect = pygame.Rect(50, 200, 20, barre_d) #son rectangle associé


            #affiche la barre du timer
            pygame.draw.rect(self.screen, "red", loading_bar_rect)

            #affiche la barre de distraction
            pygame.draw.rect(self.screen, "blue", dis_rect)
            
            #-----------------------------------

            #60 fps
            clock.tick(60)

            pygame.display.flip()
            timer += (clock.tick(30)/1000) #incrémenter le timer

            #-----------------------------------


            #gérer que le prof se retourne
            teacherChance = random.randint(0,100)
            if teacherChance == 3 and teach.isWatching == False:
                print("AYAYAYAYAYAYA")
                sprite_teach.update()
            

            #si phone est sorti et le teacher regarde
            #if (student.phoneOut == True and teach.isWatching == True):
                #return False #c'est TERMINE

            #décrémenter la barre si on est pas déja au minimum
            if progressBar > PROGRESSMIN:
                progressBar -= 50

        return False
    
        #-----------------------------------

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    obj = mj_Phone(1, screen)
    print("état:", obj.run_miniJeu())

    pygame.quit()
print("Ok")