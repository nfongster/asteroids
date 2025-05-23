import pygame, sprites
from utility import *


class Score(pygame.sprite.Sprite):
    RAPID_SHOT_SCORE = 2
    SPREAD_SHOT_SCORE = 10
    LASER_SHOT_SCORE = 15

    def __init__(self, screen):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.points = 0
        self.screen = screen
        self.text = pygame.font.Font(size=TEXT_SIZE)

    def increment(self, player):
        self.points += 1
        if self.points == Score.RAPID_SHOT_SCORE:
            player.weapon_type = WeaponType.RAPID_SHOT
        elif self.points == Score.SPREAD_SHOT_SCORE:
            player.weapon_type = WeaponType.SPREAD_SHOT
        elif self.points == Score.LASER_SHOT_SCORE:
            player.weapon_type = WeaponType.LASER_SHOT

    def draw(self, screen):
        score_text = self.text.render(f"SCORE: {self.points}", True, (0, 255, 0))
        screen.blit(score_text, (SCORE_LOCATION_X, SCORE_LOCATION_Y))