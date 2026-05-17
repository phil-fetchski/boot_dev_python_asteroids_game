from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        scrn = screen
        clr = "white"
        position = self.position
        rad = self.radius
        pygame.draw.circle(scrn, clr, position, rad)

    def update(self, dt):
        self.position += self.velocity * dt
