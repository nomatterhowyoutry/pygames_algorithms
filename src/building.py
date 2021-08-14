import pygame
from conf import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

class Building(pygame.sprite.Sprite):

    def __init__(self):

        super(Building, self).__init__()
        self.image = pygame.image.load('building_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((255, 255, 255))
        self.position = (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200)
        self.rect = self.image.get_rect(
            center=(
                self.position[0],
                self.position[1],
            )
        )
        
        