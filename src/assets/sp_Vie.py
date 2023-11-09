import pygame
import os
class Vie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.C_X = x
        self.C_Y = y
        self.image = pygame.image.load("./src/assets/sprites/images/heart.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.C_X, self.C_Y)