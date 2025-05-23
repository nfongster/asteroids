import pygame, sprites
from utility import *


class Shot(sprites.CircleShape):
    def __init__(self, x, y, cooldown):
        super().__init__(x, y, SHOT_RADIUS)
        self.cooldown = cooldown

    def draw(self, screen):
        pass

    def update(self, dt):
        self.position += self.velocity * dt


class SingleShot(Shot):
    def __init__(self, x, y):
        super().__init__(x, y, 0.3)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.position, self.radius, width=0)


class RapidShot(Shot):
    def __init__(self, x, y):
        super().__init__(x, y, 0.2)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, width=0)


class SpreadShot(Shot):
    def __init__(self, x, y):
        super().__init__(x, y, 0.2)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, self.radius, width=0)


class LaserShot(Shot):
    def __init__(self, x, y):
        super().__init__(x, y, 0.1)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), self.position, self.radius, width=0)


def get_shot(weapon_type, x, y):
    if weapon_type == WeaponType.SINGLE_SHOT:
        return SingleShot(x, y)
    if weapon_type == WeaponType.RAPID_SHOT:
        return RapidShot(x, y)
    if weapon_type == WeaponType.SPREAD_SHOT:
        return SpreadShot(x, y)
    if weapon_type == WeaponType.LASER_SHOT:
        return LaserShot(x, y)
    raise Exception(f"Unknown weapon type \"{weapon_type}\"!")