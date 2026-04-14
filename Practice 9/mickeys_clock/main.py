import pygame
from clock import MickeyClock


WIDTH = 800
HEIGHT = 800
FPS = 60
BACKGROUND_COLOR = (240, 240, 240)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")

    frame_clock = pygame.time.Clock()
    mickey_clock = MickeyClock(WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        mickey_clock.draw(screen)

        pygame.display.flip()
        frame_clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()