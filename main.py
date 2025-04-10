import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Game object groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add game object to groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_program()

        # Update
        updateable.update(dt)

        # Check collision
        for obj in asteroids:
            if (obj.collides_with(player)):
                print("Game over!")
                close_program()

        # Draw
        screen.fill(GFX_SCREEN_BACKGROUND_COLOR)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit the game to 60 FPS
        dt = clock.tick(60) / 1000

def close_program() -> None:
    print("Exiting program...")
    sys.exit()




if __name__ == "__main__":
    main()
