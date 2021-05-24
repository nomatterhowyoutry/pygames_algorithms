import pygame
import random
from utils import (
    vector_length, 
    normalize_vector,
)
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
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 3
        self.position = (self.rect.centerx, self.rect.centery)
        self.destination = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        self.mov = False

    def update(self, player_position):
        self.position = (self.rect.centerx, self.rect.centery)
        if self.__calculate_distance(player_position) < 100:
            self.destination = (2 * self.position[0] - player_position[0], 2 * self.position[1] - player_position[1])
        self.__calculate_direction()
        if self.__calculate_distance(self.destination) < 10:
            self.__update_destination()
        self.__move()

    def __move(self):
        self.rect.x += self.stepx * self.speed
        self.rect.y += self.stepy * self.speed

    def __calculate_distance(self, target):
        self.position = (self.rect.centerx, self.rect.centery)
        return vector_length(target[0] - self.position[0], target[1] - self.position[1])

    def __calculate_direction(self):
        self.directions = normalize_vector(self.destination[0] - self.position[0], self.destination[1] - self.position[1])
        self.stepx = self.directions[0]
        self.stepy = self.directions[1]

    def __update_destination(self):
        self.destination = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))