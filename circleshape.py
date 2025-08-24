import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius