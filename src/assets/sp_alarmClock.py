import pygame
import os
class AlarmClock(pygame.sprite.Sprite):
    STATES = [pygame.image.load(os.path.dirname(__file__) + "/sprites/images/reveil/reveil1.png"),
              pygame.image.load(os.path.dirname(__file__) + "/sprites/images/reveil/reveil2.png"),
              pygame.image.load(os.path.dirname(__file__) + "/sprites/images/reveil/reveil3.png")]
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = AlarmClock.STATES[0]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.drag = False