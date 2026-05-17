import pygame

# Base Class for game objects
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
        # Must override
        pass

    def update(self, dt):
        # Must override
        pass

    def collides_with(self, other):
        r1 = self.radius
        r2 = other.radius
        combined_rad = r1 + r2
        self_pos = self.position
        other_pos = other.position
        distance = self_pos.distance_to(other_pos)
        colliding = distance < combined_rad
        return colliding

