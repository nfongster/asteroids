import pygame
from utility import *


class Lives(pygame.sprite.Sprite):
    def __init__(self, screen):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.num_lives = 3
        self.screen = screen
        self.text = pygame.font.Font(size=TEXT_SIZE)

    def decrement(self):
        self.num_lives -= 1

    def draw(self, screen):
        lives_text = self.text.render(f"LIVES: {self.num_lives}", True, (255, 0, 0))
        screen.blit(lives_text, (LIVES_LOCATION_X, LIVES_LOCATION_Y))