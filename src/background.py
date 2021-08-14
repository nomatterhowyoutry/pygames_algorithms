import pygame
from conf import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH)


class Background:

    def __init__(self, image, dim):
        self.image = image
        self.dim = dim
        self.surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.render()

    def render(self):
        x = self.dim[0]
        y = self.dim[1]
        yy = SCREEN_HEIGHT
        while yy + y > 0:
            xx = 0
            yy -= y
            while xx < SCREEN_WIDTH + x:
                self.surface.blit(self.image, (xx, yy))
                xx += x
