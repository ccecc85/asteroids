import pygame # type: ignore
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # Asteroid's rotation in degrees

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        # Asteroids move in straight lines
        self.position += self.velocity * dt

    def split(self):
        # Create two smaller asteroids
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_rotation_angle = random.uniform(20,50)

        vect1 = self.velocity.rotate(new_rotation_angle)
        vect2 = self.velocity.rotate(-new_rotation_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vect1 * 1.2

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vect2 * 1.2
