import pygame
from conf import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

class Building(pygame.sprite.Sprite):

    def __init__(self):

        super(Building, self).__init__()
        self.rect = pygame.surface.Surface((50, 50))
        self.rect.fill((255, 0, 0))
        self.position = (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100)