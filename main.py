import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    af = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for ast in asteroids:
            if ast.is_colliding(p):
                print('Game over!')
                sys.exit(0)
            for sh in shots:
                if ast.is_colliding(sh):
                    ast.split()
                    sh.kill()

        screen.fill('black')

        for draw_member in drawable:
            draw_member.draw(screen)
       
        pygame.display.flip()

        tick_time = game_clock.tick(60)
        dt = tick_time / 1000

        
if __name__ == "__main__":
    main()