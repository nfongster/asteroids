import pygame, sprites
from utility import *


class Shot(sprites.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.position, self.radius, width=0)

    def update(self, dt):
        self.position += self.velocity * dt