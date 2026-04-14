import pygame
from ball import Ball


# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)  # White
FPS = 60


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Ball")

    clock = pygame.time.Clock()

    # Create the ball in the center of the screen
    ball = Ball(
        x=SCREEN_WIDTH // 2,
        y=SCREEN_HEIGHT // 2,
        radius=25,
        screen_width=SCREEN_WIDTH,
        screen_height=SCREEN_HEIGHT,
        step=20
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move_up()
                elif event.key == pygame.K_DOWN:
                    ball.move_down()
                elif event.key == pygame.K_LEFT:
                    ball.move_left()
                elif event.key == pygame.K_RIGHT:
                    ball.move_right()

        screen.fill(BACKGROUND_COLOR)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()