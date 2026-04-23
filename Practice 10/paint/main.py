import math
import pygame

# --------------------------------
# Window settings
# --------------------------------
WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 110
FPS = 60

# --------------------------------
# Colors
# --------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (120, 120, 120)
LIGHT_BLUE = (173, 216, 230)

COLOR_PALETTE = [
    (0, 0, 0),        # Black
    (255, 0, 0),      # Red
    (0, 180, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 255, 255)   # White
]

# --------------------------------
# Tool names
# --------------------------------
BRUSH = "brush"
RECTANGLE = "rectangle"
CIRCLE = "circle"
ERASER = "eraser"


def draw_toolbar(screen, font, small_font, current_tool, current_color, brush_size, tool_buttons, color_buttons):
    """
    Draw the top toolbar:
    - first row: tool buttons
    - second row: color palette and help text
    """
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, BLACK, (0, TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT), 2)

    # Draw tool buttons
    for tool_name, rect in tool_buttons.items():
        if tool_name == current_tool:
            pygame.draw.rect(screen, LIGHT_BLUE, rect)
        else:
            pygame.draw.rect(screen, WHITE, rect)

        pygame.draw.rect(screen, BLACK, rect, 2)

        text = font.render(tool_name.capitalize(), True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Draw color label
    colors_label = small_font.render("Colors:", True, BLACK)
    screen.blit(colors_label, (25, 72))

    # Draw color buttons
    for color, rect in color_buttons:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

        if color == current_color:
            pygame.draw.rect(screen, DARK_GRAY, rect, 4)

    # Draw brush size text
    size_text = font.render(f"Size: {brush_size}", True, BLACK)
    screen.blit(size_text, (870, 18))

    # Draw control hints
    hint_text = small_font.render(
        "B - Brush   R - Rectangle   C - Circle   E - Eraser   [ / ] - Change size",
        True,
        BLACK
    )
    screen.blit(hint_text, (430, 72))


def draw_preview_shape(screen, tool, color, start_pos, current_pos, width):
    """
    Draw shape preview while the mouse is being dragged.
    """
    x1, y1 = start_pos
    x2, y2 = current_pos

    if tool == RECTANGLE:
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(screen, color, rect, width)

    elif tool == CIRCLE:
        radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(screen, color, start_pos, radius, width)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint Program")
    clock = pygame.time.Clock()

    # Fonts
    font = pygame.font.SysFont("arial", 18)
    small_font = pygame.font.SysFont("arial", 14)

    # Main drawing canvas
    canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
    canvas.fill(WHITE)

    # Current settings
    current_tool = BRUSH
    current_color = BLACK
    brush_size = 5

    # Variables for drawing process
    drawing = False
    last_pos = None
    start_shape_pos = None
    current_mouse_pos = None

    # Tool buttons
    tool_buttons = {
        BRUSH: pygame.Rect(10, 15, 120, 50),
        RECTANGLE: pygame.Rect(145, 15, 150, 50),
        CIRCLE: pygame.Rect(310, 15, 120, 50),
        ERASER: pygame.Rect(445, 15, 120, 50),
    }

    # Color buttons
    color_buttons = []
    color_x = 95
    for color in COLOR_PALETTE:
        rect = pygame.Rect(color_x, 65, 32, 32)
        color_buttons.append((color, rect))
        color_x += 38

    running = True
    while running:
        for event in pygame.event.get():
            # Close window
            if event.type == pygame.QUIT:
                running = False

            # Keyboard controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_b:
                    current_tool = BRUSH
                elif event.key == pygame.K_r:
                    current_tool = RECTANGLE
                elif event.key == pygame.K_c:
                    current_tool = CIRCLE
                elif event.key == pygame.K_e:
                    current_tool = ERASER
                elif event.key == pygame.K_LEFTBRACKET:
                    brush_size = max(1, brush_size - 1)
                elif event.key == pygame.K_RIGHTBRACKET:
                    brush_size = min(50, brush_size + 1)

            # Mouse button pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                # Click on toolbar
                if my <= TOOLBAR_HEIGHT:
                    for tool_name, rect in tool_buttons.items():
                        if rect.collidepoint(mx, my):
                            current_tool = tool_name

                    for color, rect in color_buttons:
                        if rect.collidepoint(mx, my):
                            current_color = color

                # Click on canvas
                else:
                    drawing = True
                    canvas_pos = (mx, my - TOOLBAR_HEIGHT)
                    last_pos = canvas_pos
                    start_shape_pos = canvas_pos
                    current_mouse_pos = canvas_pos

                    # Draw one point immediately for brush/eraser
                    if current_tool == BRUSH:
                        pygame.draw.circle(canvas, current_color, canvas_pos, brush_size)
                    elif current_tool == ERASER:
                        pygame.draw.circle(canvas, WHITE, canvas_pos, brush_size)

            # Mouse movement
            elif event.type == pygame.MOUSEMOTION:
                mx, my = event.pos

                if drawing and my > TOOLBAR_HEIGHT:
                    canvas_pos = (mx, my - TOOLBAR_HEIGHT)
                    current_mouse_pos = canvas_pos

                    # Free drawing with brush
                    if current_tool == BRUSH and last_pos is not None:
                        pygame.draw.line(canvas, current_color, last_pos, canvas_pos, brush_size * 2)
                        pygame.draw.circle(canvas, current_color, canvas_pos, brush_size)
                        last_pos = canvas_pos

                    # Eraser draws with white color
                    elif current_tool == ERASER and last_pos is not None:
                        pygame.draw.line(canvas, WHITE, last_pos, canvas_pos, brush_size * 2)
                        pygame.draw.circle(canvas, WHITE, canvas_pos, brush_size)
                        last_pos = canvas_pos

            # Mouse button released
            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    drawing = False
                    mx, my = event.pos

                    if my > TOOLBAR_HEIGHT:
                        end_pos = (mx, my - TOOLBAR_HEIGHT)

                        # Final rectangle
                        if current_tool == RECTANGLE and start_shape_pos is not None:
                            x1, y1 = start_shape_pos
                            x2, y2 = end_pos
                            rect = pygame.Rect(
                                min(x1, x2),
                                min(y1, y2),
                                abs(x2 - x1),
                                abs(y2 - y1)
                            )
                            pygame.draw.rect(canvas, current_color, rect, brush_size)

                        # Final circle
                        elif current_tool == CIRCLE and start_shape_pos is not None:
                            radius = int(math.hypot(
                                end_pos[0] - start_shape_pos[0],
                                end_pos[1] - start_shape_pos[1]
                            ))
                            pygame.draw.circle(canvas, current_color, start_shape_pos, radius, brush_size)

                    last_pos = None
                    start_shape_pos = None
                    current_mouse_pos = None

        # Draw everything
        screen.fill(WHITE)
        draw_toolbar(screen, font, small_font, current_tool, current_color, brush_size, tool_buttons, color_buttons)
        screen.blit(canvas, (0, TOOLBAR_HEIGHT))

        # Draw preview for rectangle/circle while dragging
        if drawing and current_tool in (RECTANGLE, CIRCLE) and start_shape_pos and current_mouse_pos:
            preview_start = (start_shape_pos[0], start_shape_pos[1] + TOOLBAR_HEIGHT)
            preview_current = (current_mouse_pos[0], current_mouse_pos[1] + TOOLBAR_HEIGHT)
            draw_preview_shape(screen, current_tool, current_color, preview_start, preview_current, brush_size)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()