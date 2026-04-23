from circleshape import *
import pygame
import constants
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen, color="white"):
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn_smaller_asteroid(self):
        new_asteroid = Asteroid(self.position.x, 
                                self.position.y, 
                                self.radius - constants.ASTEROID_MIN_RADIUS)
        new_asteroid.velocity = self.velocity * constants.ASTEROID_SPEED_UP_FACTOR
        new_asteroid.velocity = new_asteroid.velocity.rotate(random.uniform(20,50))
        

    def split(self):
        self.kill()
        #small asteroid
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            self.spawn_smaller_asteroid()
            self.spawn_smaller_asteroid()

