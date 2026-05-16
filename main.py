import pygame
from constants import *
from player import *
from circleshape import *
from logger import log_state

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for un_drawn in drawable:
            un_drawn.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
