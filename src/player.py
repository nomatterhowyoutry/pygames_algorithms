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
    SCREEN_WIDTH,
    LEFT_BORDER,
    RIGHT_BORDER,
    TOP_BORDER,
    BOTTOM_BORDER
)


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()
        self.image = pygame.image.load('adventurer-idle-00.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.camera_position = [0, 0]
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.speed_x = 10
        self.speed_y = 10
        self.orientation = 'right'

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            if self.rect[1] > TOP_BORDER:
                self.camera_position[1] -= self.speed_y
                self.rect.centery -= self.speed_y
        if pressed_keys[K_DOWN]:
            if self.rect[1] < BOTTOM_BORDER:
                self.camera_position[1] += self.speed_y
                self.rect.centery += self.speed_y
        if pressed_keys[K_LEFT]:
            self.blit('left')
            if self.rect[0] > LEFT_BORDER:
                self.camera_position[0] -= self.speed_x
                self.rect.centerx -= self.speed_x
        if pressed_keys[K_RIGHT]:
            self.blit('right')
            if self.rect[0] < RIGHT_BORDER:
                self.camera_position[0] += self.speed_x
                self.rect.centerx += self.speed_x

    @property
    def coords(self):
        return self.rect.centerx, self.rect.centery

    @property
    def position(self):
        return self.rect.centerx, self.rect.centery

    def blit(self, orientation):
        if self.orientation != orientation:
            self.orientation = orientation
            self.image = pygame.transform.flip(self.image, True, False)
