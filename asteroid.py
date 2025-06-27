import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        old_radius = self.radius
        velocity1 = 1.2 * self.velocity.rotate(random_angle)
        velocity2 = 1.2 * self.velocity.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
    
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    