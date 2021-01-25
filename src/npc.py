import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from conf import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

class NPC(pygame.sprite.Sprite):

    def __init__(self):

        super(NPC, self).__init__()
        self.image = pygame.image.load('Wraith_01_Idle_000.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 3)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        