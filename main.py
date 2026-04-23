import pygame
import constants
import sys
from player  import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}\n Screen height: {constants.SCREEN_HEIGHT}")

    #containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # adding to containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH /2 , constants.SCREEN_HEIGHT /2)
    field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
        #collision detection
        for a in asteroids:
            is_hit_player = a.collides_with(player)
            if is_hit_player:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for s in shots:
                is_hit_shot = a.collides_with(s)
                if is_hit_shot:
                    s.kill()
                    a.split()
                    log_event("asteroid_shot")

        #render block
        screen.fill((0,0,0))
        for d in drawable:
            d.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 #convert from miliseconds to seconds
        #print (dt)
        


if __name__ == "__main__":
    main()
