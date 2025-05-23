import pygame, sys, sprites, text
from utility import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock, dt = pygame.time.Clock(), 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    sprites.Player.containers = (updatable, drawable)
    sprites.Asteroid.containers = (asteroids, updatable, drawable)
    sprites.AsteroidField.containers = (updatable)
    sprites.Shot.containers = (shots, updatable, drawable)

    text.Score.containers = (drawable)

    player = sprites.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = text.Score(screen)
    asteroid_field = sprites.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.check_collision(s):
                    a.split()
                    s.kill()
                    score.increment()

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()