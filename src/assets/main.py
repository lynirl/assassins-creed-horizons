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
def play_sound_effect(sound_effect):
    effect_channel = pygame.mixer.find_channel(True)
    if effect_channel:
        effect_channel.play(sound_effect)


def startMenu(a_screen):
    # Charger le son au format MP3
    MENU_THEME = pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/main-menu.mp3")
    CHANNEL_MM = pygame.mixer.Channel(1)
    CHANNEL_MM.play(MENU_THEME,loops=-1)

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

    inStartMenu = True

    a_screen.blit(BG, (0,0))
    screen.blit(LOGO, LOGO_RECT)
    inMenu = True
    btnId = 0
    while (inMenu):
        for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and startButton.rect.collidepoint(pygame.mouse.get_pos())):
                        inMenu = False
                        btnId = id(startButton)

                elif (event.type == pygame.MOUSEBUTTONDOWN and quitButton.rect.collidepoint(pygame.mouse.get_pos())):
                        inMenu = False
                        btnId = id(quitButton)
        sprite_group.draw(a_screen)
        pygame.display.update()
        CLOCK.tick(30)
    
    play_sound_effect(Button.SOUND)
    if (btnId ==  id(startButton)):
        return 0
    elif (btnId == id(quitButton)):
        return 1
    else:
        return 2
    



def main():
    IMG_SUCCESS = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/succes.png")
    IMG_ECHEC = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/explosion.png")
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
            screen.fill("black")
            # for alpha in range(0, 255, 5):
            #         screen.fill((255,255,255, alpha))
            #         pygame.display.flip()

            if (mini_jeux[i].run_miniJeu()):
                for j in range(400, 650, 20):
                    img_temp = pygame.transform.scale(IMG_SUCCESS, (j, j))
                    rect = img_temp.get_rect()
                    rect.center = (MID_X, MID_Y)
                    screen.blit(img_temp, rect)
                    CLOCK.tick(60)
                    pygame.display.flip()
                pygame.time.wait(500)
            else:
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
            score += 1
            # i+=1
        round +=1

            
        

    pygame.quit()
    print("Cya")



if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    if (len(sys.argv) > 0):
        for arg in sys.argv:
            if arg.lower() == "credits":
                screen.fill("Black")
                font = pygame.font.Font(None, 36)
                texte_lines = [
                    "Elisée Chemin - Chef de projet, Lead programmer",
                    "Rachel Peretti - Programmer",
                    "Tom Jochum Faure- Artist",
                    "Fantine Comparin - Programmer, Artist"]

                # Afficher le texte initial
                y_offset = 50           
                for line in texte_lines:
                    texte_surface = font.render(line, True, "white")
                    texte_rect = texte_surface.get_rect(center=(screen.get_width() // 2, y_offset))
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




