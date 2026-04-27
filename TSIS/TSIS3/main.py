import pygame
import os
from racer import run_game
from persistence import add_score, load_leaderboard, load_settings, save_settings

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2)

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer TSIS3")

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)

font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

settings = load_settings()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_PATH = os.path.join(BASE_DIR, "assets", "Music.mp3")


# ---------------- BUTTON ----------------
def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)

    if rect.collidepoint(pygame.mouse.get_pos()):
        color = (170,170,170)
    else:
        color = GRAY

    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    label = small_font.render(text, True, BLACK)
    screen.blit(label, (x + 20, y + 10))

    return rect


# ---------------- SETTINGS ----------------
def settings_screen():
    global settings

    while True:
        screen.fill(WHITE)

        screen.blit(font.render("SETTINGS", True, BLACK), (120, 80))

        sound_btn = draw_button(f"Sound: {'ON' if settings['sound'] else 'OFF'}", 130, 200, 240, 50)
        diff_btn = draw_button(f"Difficulty: {settings['difficulty']}", 130, 270, 240, 50)
        color_btn = draw_button(f"Car: {settings['car_color']}", 130, 340, 240, 50)

        back_btn = draw_button("Back", 170, 450, 160, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if sound_btn.collidepoint(event.pos):
                    settings["sound"] = not settings["sound"]

                elif diff_btn.collidepoint(event.pos):
                    if settings["difficulty"] == "easy":
                        settings["difficulty"] = "normal"
                    elif settings["difficulty"] == "normal":
                        settings["difficulty"] = "hard"
                    else:
                        settings["difficulty"] = "easy"

                elif color_btn.collidepoint(event.pos):
                    if settings["car_color"] == "red":
                        settings["car_color"] = "blue"
                    elif settings["car_color"] == "blue":
                        settings["car_color"] = "green"
                    else:
                        settings["car_color"] = "red"

                elif back_btn.collidepoint(event.pos):
                    save_settings(settings)
                    return "menu"

        clock.tick(60)


# ---------------- USERNAME ----------------
def get_username():
    name = ""

    while True:
        screen.fill(WHITE)

        screen.blit(small_font.render("Enter your name:", True, BLACK), (140, 200))
        screen.blit(font.render(name, True, BLACK), (140, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name if name else "Player"
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        clock.tick(60)


# ---------------- LEADERBOARD ----------------
def leaderboard_screen():
    data = load_leaderboard()

    while True:
        screen.fill(WHITE)

        screen.blit(font.render("LEADERBOARD", True, BLACK), (90, 50))

        y = 120
        for i, entry in enumerate(data):
            line = f"{i+1}. {entry['name']} - {entry['score']}"
            screen.blit(small_font.render(line, True, BLACK), (90, y))
            y += 40

        back_btn = draw_button("Back", 170, 550, 160, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "menu"

        clock.tick(60)


# ---------------- MENU ----------------
def main_menu():
    while True:
        screen.fill(WHITE)

        screen.blit(font.render("RACER GAME", True, BLACK), (90, 100))

        play_btn = draw_button("Play", 170, 250, 160, 50)
        board_btn = draw_button("Leaderboard", 170, 320, 160, 50)
        settings_btn = draw_button("Settings", 170, 390, 160, 50)
        quit_btn = draw_button("Quit", 170, 460, 160, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    return "play"
                if board_btn.collidepoint(event.pos):
                    return "leaderboard"
                if settings_btn.collidepoint(event.pos):
                    return "settings"
                if quit_btn.collidepoint(event.pos):
                    return "quit"

        clock.tick(60)


# ---------------- GAME OVER ----------------
def game_over_screen(score, coins, distance):
    name = get_username()
    if name:
        add_score(name, score, coins)

    while True:
        screen.fill(WHITE)

        screen.blit(font.render("GAME OVER", True, BLACK), (100, 120))
        screen.blit(small_font.render(f"Score: {score}", True, BLACK), (150, 200))
        screen.blit(small_font.render(f"Coins: {coins}", True, BLACK), (150, 240))
        screen.blit(small_font.render(f"Distance: {distance}", True, BLACK), (150, 280))

        retry_btn = draw_button("Retry", 170, 340, 160, 50)
        menu_btn = draw_button("Menu", 170, 410, 160, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.collidepoint(event.pos):
                    return "retry"
                if menu_btn.collidepoint(event.pos):
                    return "menu"

        clock.tick(60)


# ---------------- MAIN LOOP ----------------
def main():
    state = "menu"

    while True:

        if state == "menu":
            result = main_menu()

            if result == "play":
                state = "game"
            elif result == "leaderboard":
                state = "leaderboard"
            elif result == "settings":
                state = "settings"
            elif result == "quit":
                break

        elif state == "settings":
            result = settings_screen()
            if result == "menu":
                state = "menu"
            elif result == "quit":
                break

        elif state == "leaderboard":
            result = leaderboard_screen()
            if result == "menu":
                state = "menu"
            elif result == "quit":
                break

        elif state == "game":

            if settings["sound"] and os.path.exists(MUSIC_PATH):
                try:
                    pygame.mixer.music.load(MUSIC_PATH)
                    pygame.mixer.music.play(-1)
                except Exception as e:
                    print("Music error:", e)

            result = run_game(screen, settings)

            pygame.mixer.music.stop()

            if result == "quit":
                break

            elif result[0] == "game_over":
                score, coins, distance = result[1], result[2], result[3]
                state = "game_over"

        elif state == "game_over":
            result = game_over_screen(score, coins, distance)

            if result == "retry":
                state = "game"
            elif result == "menu":
                state = "menu"
            elif result == "quit":
                break

    pygame.quit()


if __name__ == "__main__":
    main()