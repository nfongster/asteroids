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
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=0)


class SpreadShot(Shot):
    def __init__(self, x, y):
        self.left_shot = RapidShot(x, y)
        self.left_shot.color = (40, 160, 176)
        self.right_shot = RapidShot(x, y)
        self.right_shot.color = (40, 160, 176)
        super().__init__(x, y, 0.2)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name == 'velocity':
            self.left_shot.velocity = self.velocity.rotate(20)
            self.right_shot.velocity = self.velocity.rotate(-20)

    def update(self, dt):
        super().update(dt)
        self.left_shot.update(dt)
        self.right_shot.update(dt)

    def draw(self, screen):
        pygame.draw.circle(screen, (40, 160, 176), self.position, self.radius, width=0)
        self.left_shot.draw(screen)
        self.right_shot.draw(screen)


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