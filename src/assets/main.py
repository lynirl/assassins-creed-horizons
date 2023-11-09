import pygame
import os
import warnings
import sys
import Utils

from bouton import Button

from mj_crous import mj_crous
from mj_carte import mj_carte
from mj_alarmClock import mj_alarmClock
from mj_velo import mj_velo
from mj_phone import mj_Phone
warnings.filterwarnings("ignore", "libpng warning: iCCP: known incorrect sRGB profile",category=RuntimeWarning)

def startMenu(a_screen):
    # Charger le son au format MP3
    MENU_THEME = pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/main-menu.mp3") #constante du vent
    CHANNEL_MM = pygame.mixer.Channel(1) #choisir le channel
    CHANNEL_MM.play(MENU_THEME,loops=-1) #démarrer le vent, à l'infini (loops=-1)

    MID_X = 1024 / 2
    MID_Y = 768 / 2
    BG = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/startMenu/sm_BG0.png")
    LOGO = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/logo.png")
    LOGO_RECT = LOGO.get_rect()
    LOGO_RECT.center = (MID_X, 200)

    startButton = Button(MID_X, MID_Y+150, "START", "lime")
    quitButton = Button(MID_X, MID_Y+250, "QUITTER", "red")
    sprite_group = pygame.sprite.Group(startButton, quitButton)

    CLOCK = pygame.time.Clock()

    a_screen.blit(BG, (0,0))
    screen.blit(LOGO, LOGO_RECT)
    inMenu = True
    btnId = 0
    while (inMenu):
        for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and startButton.rect.collidepoint(pygame.mouse.get_pos())):
                        CHANNEL_MM.stop() #arrêter le vent quand on démarre le jeu
                        inMenu = False
                        btnId = id(startButton)
                elif (event.type == pygame.MOUSEBUTTONDOWN and quitButton.rect.collidepoint(pygame.mouse.get_pos())):
                        inMenu = False
                        btnId = id(quitButton)
        sprite_group.draw(a_screen)
        pygame.display.update()
        CLOCK.tick(30)
    
    Utils.play_sound_effect(Button.SOUND)
    if (btnId ==  id(startButton)):
        return 0
    elif (btnId == id(quitButton)):
        return 1
    else:
        return 2
    



def main():
    #channels pour pouvoir les arrêter a tout moment (on en utilise maximum 2)
    CHANNEL_1 = pygame.mixer.Channel(1)
    CHANNEL_2 = pygame.mixer.Channel(2)

    IMG_SUCCESS = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/succes.png")
    IMG_ECHEC = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/explosion.png")
    IMG_CHARGEMENTS = [pygame.image.load(os.path.dirname(__file__) + "/sprites/images/transition/tr_lit.png"),
                       pygame.image.load(os.path.dirname(__file__) + "/sprites/images/transition/tr_velo.png"),
                       pygame.image.load(os.path.dirname(__file__) + "/sprites/images/transition/tr_phone.png"),
                       pygame.image.load(os.path.dirname(__file__) + "/sprites/images/transition/tr_crous.png"),
                       pygame.image.load(os.path.dirname(__file__) + "/sprites/images/transition/tr_velo2.png")]
    IMG_GAMEOVER = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/transition/gameover.png")
    MID_X = 1024 / 2
    MID_Y = 768 / 2
    CLOCK = pygame.time.Clock()
    score = 0
    round = 1
    vies = 3


    
    while (round < 10 and vies > 0):
        mini_jeux = [mj_alarmClock(round, screen),
                     mj_velo(round, screen),
                     mj_Phone(round, screen),
                     mj_carte(round,screen),
                     mj_crous(round, screen)]
        
        i = 0
        while (i < len(mini_jeux) and vies > 0):
            screen.blit(IMG_CHARGEMENTS[5 - len(mini_jeux)], (0,0))
            pygame.display.flip()
            pygame.time.wait(3000)
            screen.fill("black")
            if (mini_jeux[i].run_miniJeu()):
                Utils.play_sound_effect(pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/main_succes.mp3")) #son succès
                for j in range(400, 650, 20):
                    img_temp = pygame.transform.scale(IMG_SUCCESS, (j, j))
                    rect = img_temp.get_rect()
                    rect.center = (MID_X, MID_Y)
                    screen.blit(img_temp, rect)
                    CLOCK.tick(60)
                    pygame.display.flip()
                pygame.time.wait(500)
                score += 1
            else:
                Utils.play_sound_effect(pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/main_explo.mp3")) #son fail
                for j in range(1, 10):
                    img_temp = pygame.transform.scale(IMG_ECHEC, ((j/10) *900, (j/10) *900))
                    rect = img_temp.get_rect()
                    rect.center = (MID_X, MID_Y)
                    screen.blit(img_temp, rect)
                    pygame.time.Clock().tick(60)
                    pygame.display.flip()
                pygame.time.wait(500)
                vies -=1
            del(mini_jeux[i])
            # i+=1
        round +=1
    #plus de musique   
    CHANNEL_1.stop()
    CHANNEL_2.stop()
    Utils.play_sound_effect(pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/pre_gameover.mp3")) #son gameover
    screen.blit(IMG_GAMEOVER,(0,0))

    font = pygame.font.Font(None, 50)
    scoreTexte = font.render(f"Votre score est de :{score}", True, "white")
    #scoreRect = scoreTexte.get_rect(center=(MID_X, MID_Y))
    screen.blit(scoreTexte, scoreTexte.get_rect(center=(MID_X, MID_Y)))
    #TODO SON POUR LE GAMEOVER

    quitButton = Button(MID_X, MID_Y+250, "QUITTER", "red")
    sprite_group = pygame.sprite.Group(quitButton)
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN and quitButton.rect.collidepoint(pygame.mouse.get_pos())):
                return True
        sprite_group.draw(screen)
        pygame.display.update()
        CLOCK.tick(30)



if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Stuck in the loop")

    #arguments en ligne de commande
    if (len(sys.argv) > 0):
        for arg in sys.argv:
            if arg.lower() == "credits":
                screen.fill("Black")
                font = pygame.font.Font(None, 36)
                texte_lines = [
                    "Elisée Chemin - Chef de projet, Lead programmer",
                    "Rachel Peretti - Programmer",
                    "Tom Jochum Faure - Artist, Programmer",
                    "Fantine Comparin - Programmer, Artist"]

                # Afficher le texte initial
                y_offset = 50           
                for line in texte_lines:
                    texte_surface = font.render(line, True, "white")
                    texte_rect = texte_surface.get_rect(center=(screen.get_width() / 2, y_offset))
                    screen.blit(texte_surface, texte_rect)
                    y_offset += 50
                    pygame.display.flip()

                pygame.time.wait(3000)

            if arg.lower() == "sources":
                print("World !")
        
    if (startMenu(screen) == 1):
        pygame.quit()
        sys.exit
    else:
        main()
    pygame.quit()




