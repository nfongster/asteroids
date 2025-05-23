import pygame
from utility import *


class Score(pygame.sprite.Sprite):
    def __init__(self, screen):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.points = 0
        self.screen = screen
        self.text = pygame.font.Font(size=40)

    def increment(self):
        self.points += 1

    def draw(self, screen):
        score_text = self.text.render(f"SCORE: {self.points}", True, (0, 255, 0))
        screen.blit(score_text, (SCORE_LOCATION_X, SCORE_LOCATION_Y))