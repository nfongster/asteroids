import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.points = 0

    def increment(self):
        self.points += 1
        print(f"Asteroids destroyed: {self.points}")