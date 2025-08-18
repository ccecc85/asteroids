import pygame # type: ignore
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        
        player1.draw(screen)
        player1.update(dt)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()
