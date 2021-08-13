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
        self.camera_position = [0, 0]
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.speed_x = 3
        self.speed_y = 3
        self.orientation = 'right'

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.camera_position[1] += self.speed_y
            self.rect.centery -= self.speed_y
            # self.rect.move_ip(0, -self.speed_y)
        if pressed_keys[K_DOWN]:
            self.camera_position[1] -= self.speed_y
            self.rect.centery += self.speed_y
            # self.rect.move_ip(0, self.speed_y)
        if pressed_keys[K_LEFT]:
            self.blit('left')
            self.camera_position[0] += self.speed_x
            self.rect.centerx -= self.speed_x
            # self.rect.move_ip(-self.speed_x, 0)
        if pressed_keys[K_RIGHT]:
            self.blit('right')
            self.camera_position[0] -= self.speed_x
            self.rect.centerx += self.speed_x
            # self.rect.move_ip(self.speed_x, 0)

        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > SCREEN_WIDTH:
        #     self.rect.right = SCREEN_WIDTH
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT

    @property
    def position(self):
        return self.rect.centerx, self.rect.centery

    def blit(self, orientation):
        if self.orientation != orientation:
            self.orientation = orientation
            self.image = pygame.transform.flip(self.image, True, False)
