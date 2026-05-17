import random
from circleshape import *
from logger import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x 
        self.y = y
        self.radius = radius

    def draw(self, screen):
        scrn = screen
        clr = "white"
        position = self.position
        rad = self.radius
        pygame.draw.circle(scrn, clr, position, rad)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rot_angle = random.uniform(20, 50)
            rot_1 = self.velocity.rotate(rot_angle)
            rot_2 = self.velocity.rotate(-rot_angle)
            speed_multiplier = 1.2
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
            ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
            ast_1.velocity = rot_1 * speed_multiplier
            ast_2.velocity = rot_2 * speed_multiplier

            




