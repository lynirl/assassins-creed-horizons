import pygame
import os

class Button(pygame.sprite.Sprite):
    
    def __init__(self, x, y, texte, color = ((180,180,180))):
        super().__init__()
        #self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/images/gros_button.png"))
        self.image = pygame.surface.Surface((300, 75))
        self.image.fill(color)
        pygame.draw.rect(self.image, "black", pygame.rect.Rect((0,0), (300, 75)), 5)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        font = pygame.font.SysFont(None, 35)
        texte_rendu = font.render(texte, True, "white")
        texte_rect = texte_rendu.get_rect()
        texte_rect.center = (self.rect.width /2, self.rect.height/2)
        self.image.blit(texte_rendu, texte_rect)
