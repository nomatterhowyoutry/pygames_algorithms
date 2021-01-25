import pygame
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

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()
        self.image = pygame.image.load('adventurer-idle-00.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.speed_x = 1
        self.speed_y = 1.5
        self.orientation = 'right'

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed_y)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed_y)
        if pressed_keys[K_LEFT]:
            if (self.orientation != 'left'):
                self.blit('left')
            self.rect.move_ip(-self.speed_x, 0)
        if pressed_keys[K_RIGHT]:
            if (self.orientation != 'right'):
                self.blit('right')
            self.rect.move_ip(self.speed_x, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


    def blit(self, orientation):
        self.orientation = orientation
        self.image = pygame.transform.flip(self.image, True, False)