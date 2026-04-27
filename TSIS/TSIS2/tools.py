import pygame
import math

# =========================
# SHAPE PREVIEW (outline)
# =========================
def draw_shape_preview(surface, tool, start, end, color, size):

    if tool == "rect":
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        w = abs(end[0] - start[0])
        h = abs(end[1] - start[1])
        pygame.draw.rect(surface, color, (x, y, w, h), size)

    elif tool == "circle":
        r = int(math.dist(start, end))
        pygame.draw.circle(surface, color, start, r, size)

    elif tool == "square":
        side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
        pygame.draw.rect(surface, color, (start[0], start[1], side, side), size)

    elif tool == "line":
        pygame.draw.line(surface, color, start, end, size)

    elif tool == "rtri":
        pts = [start, (start[0], end[1]), end]
        pygame.draw.polygon(surface, color, pts, size)

    elif tool == "etri":
        length = math.dist(start, end)
        h = (length * math.sqrt(3)) / 2

        p1 = start
        p2 = (start[0] + length, start[1])
        p3 = (start[0] + length / 2, start[1] - h)

        pygame.draw.polygon(surface, color, [p1, p2, p3], size)

    elif tool == "rhombus":
        cx = (start[0] + end[0]) // 2
        cy = (start[1] + end[1]) // 2

        dx = abs(end[0] - start[0]) // 2
        dy = abs(end[1] - start[1]) // 2

        pts = [
            (cx, cy - dy),
            (cx + dx, cy),
            (cx, cy + dy),
            (cx - dx, cy)
        ]

        pygame.draw.polygon(surface, color, pts, size)


# =========================
# FINAL DRAW
# =========================
def draw_final_shape(surface, tool, start, end, color, size):
    draw_shape_preview(surface, tool, start, end, color, size)


# =========================
# UI DRAW
# =========================
def draw_ui(screen, buttons, colors, brush_sizes, tool, color, brush_size, text_mode, font):

    # BACKGROUND TOOLBAR
    pygame.draw.rect(screen, (200, 210, 230), (0, 0, 800, 160))
    pygame.draw.line(screen, (100,100,100), (0, 160), (800, 160), 3)

    # TOOL BUTTONS
    for name, rect in buttons.items():
        fill = (210, 215, 225)
        if name == tool:
            fill = (140, 190, 255)

        pygame.draw.rect(screen, fill, rect)
        pygame.draw.rect(screen, (50, 50, 50), rect, 2)

        label = font.render(name.upper(), True, (30, 30, 30))
        screen.blit(label, (rect.x + 6, rect.y + 6))

    # COLOR PALETTE
    palette = {
        "black": (0,0,0),
        "red": (255,0,0),
        "green": (0,255,0),
        "blue": (0,0,255),
        "white": (255,255,255),
        "yellow": (255,255,0),
        "orange": (255,165,0),
        "purple": (128,0,128),
        "cyan": (0,255,255),
        "pink": (255,105,180),
    }

    for name, rect in colors.items():
        pygame.draw.rect(screen, palette[name], rect)

        border = 1
        if palette[name] == color:
            border = 3

        pygame.draw.rect(screen, (0,0,0), rect, border)

    # BRUSH SIZE
    sizes = [2, 5, 10]

    for i, (name, rect) in enumerate(brush_sizes.items()):
        pygame.draw.rect(screen, (240, 240, 245), rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)

        pygame.draw.circle(screen, (0,0,0), rect.center, sizes[i]//2)

        if brush_size == sizes[i]:
            pygame.draw.rect(screen, (0,0,0), rect, 3)

    # STATUS BAR
    pygame.draw.rect(screen, (240, 240, 245), (0, 570, 800, 30))

    names = {
        (255,255,255): "WHITE",
        (0,0,0): "BLACK",
        (255,0,0): "RED",
        (0,255,0): "GREEN",
        (0,0,255): "BLUE"
    }

    text = f"{tool.upper()} | {names.get(color,'CUSTOM')} | {brush_size}px"
    if text_mode:
        text += " | TEXT MODE"

    info = font.render(text, True, (40, 40, 40))
    screen.blit(info, (10, 575))


# =========================
# FLOOD FILL
# =========================
def flood_fill(canvas, x, y, new_color):

    target = canvas.get_at((x, y))
    if target == new_color:
        return

    w, h = canvas.get_size()
    stack = [(x, y)]

    while stack:
        px, py = stack.pop()

        if 0 <= px < w and 0 <= py < h:
            if canvas.get_at((px, py)) == target:
                canvas.set_at((px, py), new_color)

                stack.append((px+1, py))
                stack.append((px-1, py))
                stack.append((px, py+1))
                stack.append((px, py-1))