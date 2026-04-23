import pygame
import random
import sys

# ---------------------------------
# Game settings
# ---------------------------------
CELL_SIZE = 25           # Size of one square cell
COLUMNS = 24             # Number of cells horizontally
ROWS = 20                # Number of cells vertically

WIDTH = COLUMNS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

FPS_START = 6            # Starting snake speed (slower than before)
FOOD_PER_LEVEL = 4       # How many foods are needed for next level

# ---------------------------------
# Colors
# ---------------------------------
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
GREEN = (0, 170, 0)
DARK_GREEN = (0, 110, 0)
RED = (220, 50, 50)
GRAY = (180, 180, 180)
BLUE = (40, 90, 180)

# ---------------------------------
# Pygame initialization
# ---------------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Fonts
font_small = pygame.font.SysFont("Arial", 24)
font_big = pygame.font.SysFont("Arial", 50)


def build_border_walls():
    """
    Create border walls around the playing field.
    Food must not spawn on these cells.
    Snake dies if it hits them.
    """
    walls = set()

    # Top and bottom border
    for x in range(COLUMNS):
        walls.add((x, 0))
        walls.add((x, ROWS - 1))

    # Left and right border
    for y in range(ROWS):
        walls.add((0, y))
        walls.add((COLUMNS - 1, y))

    return walls


def get_random_food_position(snake, walls):
    """
    Generate a random food position that is:
    - not on the snake
    - not on a wall
    """
    free_cells = []

    for x in range(1, COLUMNS - 1):
        for y in range(1, ROWS - 1):
            cell = (x, y)
            if cell not in snake and cell not in walls:
                free_cells.append(cell)

    # If there are no free cells, return None
    if not free_cells:
        return None

    return random.choice(free_cells)


def draw_cell(position, color):
    """
    Draw one square cell on the screen.
    """
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)


def draw_grid():
    """
    Draw grid lines to make the board easier to see.
    """
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def draw_walls(walls):
    """
    Draw border walls.
    """
    for wall in walls:
        draw_cell(wall, BLUE)


def draw_snake(snake):
    """
    Draw the snake.
    Head is darker so it is easier to see.
    """
    for i, segment in enumerate(snake):
        if i == 0:
            draw_cell(segment, DARK_GREEN)
        else:
            draw_cell(segment, GREEN)


def draw_food(food_position):
    """
    Draw food.
    """
    if food_position is not None:
        draw_cell(food_position, RED)


def draw_text(score, level):
    """
    Draw score and level in the top area.
    """
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    level_text = font_small.render(f"Level: {level}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))


def show_end_screen(score, level, won):
    """
    Show final screen:
    - Game Over if player lost
    - You Win if player filled the field
    """
    screen.fill(WHITE)

    if won:
        title_text = font_big.render("You Win!", True, GREEN)
    else:
        title_text = font_big.render("Game Over", True, RED)

    score_text = font_small.render(f"Final Score: {score}", True, BLACK)
    level_text = font_small.render(f"Final Level: {level}", True, BLACK)
    hint_text = font_small.render("Press R to restart or ESC to quit", True, BLACK)

    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    level_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 35))
    hint_rect = hint_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 90))

    screen.blit(title_text, title_rect)
    screen.blit(score_text, score_rect)
    screen.blit(level_text, level_rect)
    screen.blit(hint_text, hint_rect)


def reset_game():
    """
    Create initial game state.
    """
    walls = build_border_walls()

    # Initial snake: 3 segments
    snake = [(8, 10), (7, 10), (6, 10)]

    # Start moving to the right
    direction = (1, 0)
    next_direction = (1, 0)

    score = 0
    level = 1
    speed = FPS_START
    won = False

    food_position = get_random_food_position(snake, walls)

    return snake, direction, next_direction, food_position, score, level, speed, walls, won


def main():
    # Create initial game state
    snake, direction, next_direction, food_position, score, level, speed, walls, won = reset_game()

    game_over = False
    running = True

    while running:
        # -----------------------------
        # Handle events
        # -----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    # Change snake direction with arrow keys
                    # Prevent moving directly backwards into itself
                    if event.key == pygame.K_UP and direction != (0, 1):
                        next_direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        next_direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        next_direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        next_direction = (1, 0)
                else:
                    # Restart or quit after game over
                    if event.key == pygame.K_r:
                        snake, direction, next_direction, food_position, score, level, speed, walls, won = reset_game()
                        game_over = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False

        # -----------------------------
        # Update game logic
        # -----------------------------
        if not game_over:
            # Apply the next direction
            direction = next_direction

            # Calculate new head position
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            # Check if snake leaves playing area
            # This is an extra safety check
            if not (0 <= new_head[0] < COLUMNS and 0 <= new_head[1] < ROWS):
                game_over = True

            # Check wall collision
            elif new_head in walls:
                game_over = True

            # Check collision with itself
            elif new_head in snake:
                game_over = True

            else:
                # Move snake: add new head
                snake.insert(0, new_head)

                # If snake eats food, do not remove tail
                if new_head == food_position:
                    score += 1

                    # Level increases every FOOD_PER_LEVEL foods
                    level = 1 + score // FOOD_PER_LEVEL

                    # Increase speed when level grows, but more smoothly
                    speed = FPS_START + (level - 1)

                    # Generate new food not on snake and not on wall
                    food_position = get_random_food_position(snake, walls)

                    # If there are no free cells left, the player wins
                    if food_position is None:
                        won = True
                        game_over = True
                else:
                    # Normal movement: remove last segment
                    snake.pop()

        # -----------------------------
        # Draw everything
        # -----------------------------
        screen.fill(WHITE)
        draw_grid()
        draw_walls(walls)
        draw_food(food_position)
        draw_snake(snake)
        draw_text(score, level)

        if game_over:
            show_end_screen(score, level, won)

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()