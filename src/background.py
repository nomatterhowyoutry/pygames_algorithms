import pygame
from conf import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH)


class Background:

    def __init__(self, image_1, image_2, dim):
        self.image_1 = image_1
        self.image_1 = pygame.transform.scale(self.image_1, dim)
        self.image_2 = image_2
        self.image_2 = pygame.transform.scale(self.image_2, dim)
        self.dim = dim
        self.surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.render()

    def render(self):
        x = self.dim[0]
        y = self.dim[1]
        yy = SCREEN_HEIGHT
        i = -1
        while yy + y > 0:
            i += 1
            xx = 0
            yy -= y
            while xx < SCREEN_WIDTH + x:
                if i % 2 == 0:
                    self.surface.blit(self.image_1, (xx, yy))
                else:
                    self.surface.blit(self.image_2, (xx, yy))
                i += 1
                xx += x
