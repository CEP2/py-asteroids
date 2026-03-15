import pygame
import constants
from player  import Player
from logger import log_state

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}\n Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH /2 , constants.SCREEN_HEIGHT /2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 #convert from miliseconds to seconds
        #print (dt)
        


if __name__ == "__main__":
    main()
