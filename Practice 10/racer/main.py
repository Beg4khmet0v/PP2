import os
import sys
import random
import pygame

# -------------------------------------------------
# Pygame initialization
# -------------------------------------------------
pygame.init()
pygame.mixer.init()

# -------------------------------------------------
# Screen settings
# -------------------------------------------------
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# -------------------------------------------------
# Colors
# -------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (170, 170, 170)
LIGHT_GRAY = (220, 220, 220)
YELLOW = (255, 215, 0)
RED = (220, 50, 50)
GREEN = (40, 160, 40)

# -------------------------------------------------
# Road settings
# White background + simple road lines
# -------------------------------------------------
ROAD_LEFT = 90
ROAD_RIGHT = 410
ROAD_WIDTH = ROAD_RIGHT - ROAD_LEFT
LANE_COUNT = 3
LANE_WIDTH = ROAD_WIDTH // LANE_COUNT

LANE_CENTERS = [
    ROAD_LEFT + LANE_WIDTH // 2,
    ROAD_LEFT + LANE_WIDTH // 2 + LANE_WIDTH,
    ROAD_LEFT + LANE_WIDTH // 2 + 2 * LANE_WIDTH,
]

# -------------------------------------------------
# Game settings
# -------------------------------------------------
PLAYER_SPEED = 7
ENEMY_SPEED = 6
COIN_SPEED = 6
SPEED_INCREMENT = 0.5

coins_collected = 0
score = 0

# -------------------------------------------------
# Fonts
# -------------------------------------------------
font_small = pygame.font.SysFont("Arial", 24)
font_big = pygame.font.SysFont("Arial", 56)

# -------------------------------------------------
# Paths to assets
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

PLAYER_FILE = os.path.join(ASSETS_DIR, "player.avif")
ENEMY_FILE = os.path.join(ASSETS_DIR, "enemy.jpg")
CRASH_FILE = os.path.join(ASSETS_DIR, "crash.mp3")
MUSIC_FILE = os.path.join(ASSETS_DIR, "music.mp3")


# -------------------------------------------------
# Helper functions
# -------------------------------------------------
def create_fallback_car(size, color):
    """
    Create a simple car shape if image loading fails.
    This is a safety fallback so the game still works.
    """
    surf = pygame.Surface(size, pygame.SRCALPHA)
    w, h = size

    # Main body
    pygame.draw.rect(surf, color, (w * 0.2, h * 0.1, w * 0.6, h * 0.8), border_radius=12)

    # Cabin / windshield
    pygame.draw.rect(surf, (30, 30, 30), (w * 0.3, h * 0.2, w * 0.4, h * 0.25), border_radius=8)

    # Wheels
    pygame.draw.rect(surf, BLACK, (w * 0.08, h * 0.18, w * 0.12, h * 0.2), border_radius=5)
    pygame.draw.rect(surf, BLACK, (w * 0.8, h * 0.18, w * 0.12, h * 0.2), border_radius=5)
    pygame.draw.rect(surf, BLACK, (w * 0.08, h * 0.62, w * 0.12, h * 0.2), border_radius=5)
    pygame.draw.rect(surf, BLACK, (w * 0.8, h * 0.62, w * 0.12, h * 0.2), border_radius=5)

    return surf


def load_car_image(path, size, fallback_color):
    """
    Try to load and scale a car image.
    If loading fails, return a fallback car shape.
    """
    try:
        image = pygame.image.load(path)
        try:
            image = image.convert_alpha()
        except pygame.error:
            image = image.convert()

        image = pygame.transform.smoothscale(image, size)
        return image
    except Exception as e:
        print(f"Could not load image: {path}")
        print(f"Reason: {e}")
        return create_fallback_car(size, fallback_color)


def load_crash_sound(path):
    """
    Try to load crash sound.
    If it fails, return None.
    """
    try:
        return pygame.mixer.Sound(path)
    except Exception as e:
        print(f"Could not load crash sound: {path}")
        print(f"Reason: {e}")
        return None


def play_background_music(path):
    """
    Try to start background music in a loop.
    If it fails, the game will still work without music.
    """
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Could not load background music: {path}")
        print(f"Reason: {e}")


def draw_road(surface, dash_offset):
    """
    Draw a simple racing road using vertical lines and moving dashed lane lines.
    Background stays white, as requested.
    """
    surface.fill(WHITE)

    # Left and right road borders
    pygame.draw.line(surface, BLACK, (ROAD_LEFT, 0), (ROAD_LEFT, SCREEN_HEIGHT), 4)
    pygame.draw.line(surface, BLACK, (ROAD_RIGHT, 0), (ROAD_RIGHT, SCREEN_HEIGHT), 4)

    # Dashed lane separators
    lane_line_x1 = ROAD_LEFT + LANE_WIDTH
    lane_line_x2 = ROAD_LEFT + 2 * LANE_WIDTH

    dash_height = 40
    dash_gap = 25

    y = -dash_height + dash_offset
    while y < SCREEN_HEIGHT:
        pygame.draw.line(surface, GRAY, (lane_line_x1, y), (lane_line_x1, y + dash_height), 6)
        pygame.draw.line(surface, GRAY, (lane_line_x2, y), (lane_line_x2, y + dash_height), 6)
        y += dash_height + dash_gap

    # Optional top label
    title = font_small.render("Racer", True, BLACK)
    surface.blit(title, (15, 15))


def draw_texts(surface):
    """
    Draw score and coin counter.
    Coin counter is placed in the top-right corner.
    """
    global score, coins_collected, ENEMY_SPEED

    score_text = font_small.render(f"Score: {score}", True, BLACK)
    speed_text = font_small.render(f"Speed: {ENEMY_SPEED:.1f}", True, BLACK)
    coins_text = font_small.render(f"Coins: {coins_collected}", True, BLACK)

    surface.blit(score_text, (15, 50))
    surface.blit(speed_text, (15, 85))

    coins_rect = coins_text.get_rect(topright=(SCREEN_WIDTH - 15, 20))
    surface.blit(coins_text, coins_rect)


def game_over_screen(surface):
    """
    Show final game over screen.
    """
    surface.fill(WHITE)

    game_over_text = font_big.render("Game Over", True, RED)
    score_text = font_small.render(f"Final score: {score}", True, BLACK)
    coins_text = font_small.render(f"Coins collected: {coins_collected}", True, BLACK)

    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
    coins_rect = coins_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))

    surface.blit(game_over_text, game_over_rect)
    surface.blit(score_text, score_rect)
    surface.blit(coins_text, coins_rect)

    pygame.display.update()


# -------------------------------------------------
# Sprite classes
# -------------------------------------------------
class Player(pygame.sprite.Sprite):
    """
    Player car controlled by keyboard.
    """
    def __init__(self):
        super().__init__()
        self.image = load_car_image(PLAYER_FILE, (72, 128), RED)
        self.rect = self.image.get_rect()
        self.rect.center = (LANE_CENTERS[1], SCREEN_HEIGHT - 110)

    def update(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED

        # Move right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED

        # Keep player inside the road boundaries
        if self.rect.left < ROAD_LEFT + 10:
            self.rect.left = ROAD_LEFT + 10

        if self.rect.right > ROAD_RIGHT - 10:
            self.rect.right = ROAD_RIGHT - 10


class Enemy(pygame.sprite.Sprite):
    """
    Enemy car coming from the top.
    """
    def __init__(self):
        super().__init__()
        self.image = load_car_image(ENEMY_FILE, (72, 128), LIGHT_GRAY)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.centerx = random.choice(LANE_CENTERS)
        self.rect.y = random.randint(-300, -140)

    def update(self):
        global score
        self.rect.y += ENEMY_SPEED

        # If enemy leaves the screen, player gets score and enemy respawns
        if self.rect.top > SCREEN_HEIGHT:
            score += 1
            self.reset_position()


class Coin(pygame.sprite.Sprite):
    """
    Coin sprite.
    Coins appear randomly and can be collected by the player.
    """
    def __init__(self):
        super().__init__()

        # Transparent surface for drawing a yellow coin
        self.image = pygame.Surface((34, 34), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (17, 17), 14)
        pygame.draw.circle(self.image, BLACK, (17, 17), 14, 2)

        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(LANE_CENTERS)
        self.rect.y = random.randint(-120, -50)

    def update(self):
        self.rect.y += COIN_SPEED

        # Remove coin if it leaves the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# -------------------------------------------------
# Create game objects
# -------------------------------------------------
player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)

# -------------------------------------------------
# Sounds
# -------------------------------------------------
crash_sound = load_crash_sound(CRASH_FILE)
play_background_music(MUSIC_FILE)

# -------------------------------------------------
# Custom events
# -------------------------------------------------
INC_SPEED = pygame.USEREVENT + 1
SPAWN_COIN = pygame.USEREVENT + 2

# Increase speed every 4 seconds
pygame.time.set_timer(INC_SPEED, 4000)

# Try to spawn coins every 1200 milliseconds
pygame.time.set_timer(SPAWN_COIN, 1200)

# -------------------------------------------------
# Main game loop
# -------------------------------------------------
dash_offset = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Increase the game speed over time
        elif event.type == INC_SPEED:
            ENEMY_SPEED += SPEED_INCREMENT
            COIN_SPEED = ENEMY_SPEED

        # Randomly create coins
        elif event.type == SPAWN_COIN:
            # Do not allow too many coins on screen at once
            if len(coins) < 3:
                # Random chance makes them "randomly appearing"
                if random.random() < 0.75:
                    coin = Coin()
                    coins.add(coin)
                    all_sprites.add(coin)

    # Update moving lane dashes
    dash_offset = (dash_offset + int(ENEMY_SPEED)) % 65

    # Update sprites
    player.update()
    enemy.update()
    coins.update()

    # Check collision with coins
    collected = pygame.sprite.spritecollide(player, coins, True)
    if collected:
        coins_collected += len(collected)

    # Check collision with enemy
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.music.stop()

        if crash_sound is not None:
            crash_sound.play()

        game_over_screen(screen)
        pygame.time.delay(2200)
        running = False
        continue

    # Draw everything
    draw_road(screen, dash_offset)
    draw_texts(screen)

    # Draw all sprites
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()