import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            GFX_ASTEROID_COLOR,
            self.position,
            self.radius,
            GFX_ASTEROID_LINE_WEIGHT
        )