import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroid_field):
        super().__init__(x, y, radius)
        self.asteroid_field = asteroid_field

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.asteroid_field.destroy_asteroid(self)
        
        if self.radius <  ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        velocity = self.velocity.rotate(random_angle) * ASTEROID_SPLIT_SPEED_MULTIPIER
        self.asteroid_field.spawn(new_radius, self.position, velocity)

        velocity = self.velocity.rotate(- random_angle) * ASTEROID_SPLIT_SPEED_MULTIPIER
        self.asteroid_field.spawn(new_radius, self.position, velocity)