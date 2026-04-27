import pygame
from datetime import datetime
from tools import draw_ui, flood_fill, draw_shape_preview, draw_final_shape

pygame.init()

# -----------------------
# WINDOW
# -----------------------
WIDTH, HEIGHT = 800, 600
TOOLBAR_HEIGHT = 160

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS Paint")

clock = pygame.time.Clock()

# -----------------------
# COLORS
# -----------------------
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

# -----------------------
# CANVAS
# -----------------------
canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

# -----------------------
# STATE
# -----------------------
tool = "pencil"
color = BLACK
brush_size = 2

drawing = False
start_pos = (0,0)
current_pos = (0,0)
prev_pos = None

text_mode = False
text_pos = None
text_value = ""

# -----------------------
# UI SETUP
# -----------------------
buttons = {
    "pencil": pygame.Rect(10,10,80,30),
    "line": pygame.Rect(100,10,80,30),
    "rect": pygame.Rect(190,10,80,30),
    "circle": pygame.Rect(280,10,80,30),
    "square": pygame.Rect(370,10,80,30),
    "rtri": pygame.Rect(460,10,80,30),
    "etri": pygame.Rect(550,10,80,30),
    "rhombus": pygame.Rect(640,10,80,30),
    "fill": pygame.Rect(10,50,80,30),
    "eraser": pygame.Rect(100,50,80,30),
    "text": pygame.Rect(190,50,80,30),
}

colors_dict = {
    "black": pygame.Rect(10,90,30,30),
    "red": pygame.Rect(50,90,30,30),
    "green": pygame.Rect(90,90,30,30),
    "blue": pygame.Rect(130,90,30,30),
    "white": pygame.Rect(170,90,30,30),
    "yellow": pygame.Rect(210,90,30,30),
    "orange": pygame.Rect(250,90,30,30),
    "purple": pygame.Rect(290,90,30,30),
    "cyan": pygame.Rect(330,90,30,30),
    "pink": pygame.Rect(370,90,30,30),
}

brush_sizes = {
    "small": pygame.Rect(10,130,60,25),
    "medium": pygame.Rect(80,130,60,25),
    "large": pygame.Rect(150,130,60,25),
}

font = pygame.font.SysFont(None, 20)
text_font = pygame.font.SysFont(None, 24)

# -----------------------
# MAIN LOOP
# -----------------------
running = True

while running:
    mx, my = pygame.mouse.get_pos()

    canvas_x = mx
    canvas_y = my - TOOLBAR_HEIGHT

    # BACKGROUND
    screen.fill((240, 240, 245))

    # CANVAS
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ---------- KEYBOARD ----------
        elif event.type == pygame.KEYDOWN:

            if text_mode:
                if event.key == pygame.K_RETURN:
                    if text_value:
                        txt = text_font.render(text_value, True, color)
                        canvas.blit(txt, text_pos)
                    text_mode = False
                    text_value = ""

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_value = ""

                else:
                    text_value += event.unicode

            else:
                if event.key == pygame.K_1:
                    brush_size = 2
                elif event.key == pygame.K_2:
                    brush_size = 5
                elif event.key == pygame.K_3:
                    brush_size = 10

                elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    name = datetime.now().strftime("paint_%H%M%S.png")
                    pygame.image.save(canvas, name)
                    print("Saved:", name)

        # ---------- MOUSE DOWN ----------
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if my < TOOLBAR_HEIGHT:

                for name, rect in buttons.items():
                    if rect.collidepoint(mx, my):
                        tool = name
                        text_mode = False

                color_map = {
                    "black": BLACK, "red": RED, "green": GREEN,
                    "blue": BLUE, "white": WHITE,
                    "yellow": (255,255,0),
                    "orange": (255,165,0),
                    "purple": (128,0,128),
                    "cyan": (0,255,255),
                    "pink": (255,105,180),
                }

                for name, rect in colors_dict.items():
                    if rect.collidepoint(mx, my):
                        color = color_map[name]

                size_map = {"small":2, "medium":5, "large":10}
                for name, rect in brush_sizes.items():
                    if rect.collidepoint(mx, my):
                        brush_size = size_map[name]

            else:
                if tool == "fill":
                    flood_fill(canvas, canvas_x, canvas_y, color)

                elif tool == "text":
                    text_mode = True
                    text_pos = (canvas_x, canvas_y)
                    text_value = ""

                else:
                    drawing = True
                    start_pos = (canvas_x, canvas_y)
                    current_pos = (canvas_x, canvas_y)
                    prev_pos = (canvas_x, canvas_y)

        # ---------- MOUSE MOVE ----------
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = (canvas_x, canvas_y)

            if tool == "pencil":
                pygame.draw.line(canvas, color, prev_pos, current_pos, brush_size)

            elif tool == "eraser":
                pygame.draw.line(canvas, WHITE, prev_pos, current_pos, brush_size)

            prev_pos = current_pos

        # ---------- MOUSE UP ----------
        elif event.type == pygame.MOUSEBUTTONUP:

            if drawing:
                if tool not in ["pencil", "eraser", "fill", "text"]:
                    draw_final_shape(canvas, tool, start_pos, current_pos, color, brush_size)

                drawing = False

    # ---------- PREVIEW ----------
    if drawing and tool not in ["pencil", "eraser", "fill", "text"]:
        preview = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT), pygame.SRCALPHA)
        draw_shape_preview(preview, tool, start_pos, current_pos, (100,100,255,120), brush_size)
        screen.blit(preview, (0, TOOLBAR_HEIGHT))

    # ---------- TEXT PREVIEW ----------
    if text_mode and text_pos:
        preview_txt = text_font.render(text_value, True, color)
        screen.blit(preview_txt, (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT))

    # ---------- TOOLBAR BACKGROUND ----------
    pygame.draw.rect(screen, (200, 210, 230), (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, (100,100,100), (0, TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT), 3)

    # ---------- UI ----------
    draw_ui(screen, buttons, colors_dict, brush_sizes, tool, color, brush_size, text_mode, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()