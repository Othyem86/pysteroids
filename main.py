import pygame
from constants import *
from player import *

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        player.update(dt)

        # Draw
        screen.fill(GFX_SCREEN_BACKGROUND_COLOR)
        player.draw(screen)
        pygame.display.flip()

        # limit the game to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
