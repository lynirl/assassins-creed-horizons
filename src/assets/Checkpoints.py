import pygame
class Checkpoint():
    def __init__(self, *pos):
        self.liste = []
        for p in pos:
            posx, posy = p
            r = pygame.rect.Rect(posx-25, posy-70, 50, 140)
            self.liste.append(r)
        self.index = 0
        