import pygame
import random

WIDTH, HEIGHT = 500, 700
FPS = 60

ROAD_LEFT = 100
ROAD_RIGHT = 400
LANES = 3
LANE_WIDTH = (ROAD_RIGHT - ROAD_LEFT) // LANES

LANE_X = [
    ROAD_LEFT + LANE_WIDTH//2,
    ROAD_LEFT + LANE_WIDTH//2 + LANE_WIDTH,
    ROAD_LEFT + LANE_WIDTH//2 + 2*LANE_WIDTH
]

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (180,180,180)
YELLOW = (255,200,0)
RED = (200,50,50)
BLUE = (50,50,200)
GREEN = (50,200,50)


# ---------------- PLAYER ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface((50,90), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0,10,50,70))
        pygame.draw.rect(self.image, BLACK, (5,0,40,20))
        pygame.draw.rect(self.image, BLACK, (5,70,40,20))

        self.rect = self.image.get_rect()
        self.rect.center = (LANE_X[1], HEIGHT - 100)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 6
        if keys[pygame.K_RIGHT]:
            self.rect.x += 6

        if self.rect.left < ROAD_LEFT:
            self.rect.left = ROAD_LEFT
        if self.rect.right > ROAD_RIGHT:
            self.rect.right = ROAD_RIGHT


# ---------------- TRAFFIC ----------------
class Traffic(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()

        self.image = pygame.Surface((50,90), pygame.SRCALPHA)
        pygame.draw.rect(self.image, BLUE, (0,10,50,70))

        self.rect = self.image.get_rect()
        self.rect.centerx = lane
        self.rect.y = -120

    def update(self, speed):
        self.rect.y += speed + 2
        if self.rect.top > HEIGHT:
            self.kill()


# ---------------- OBSTACLE ----------------
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()

        self.image = pygame.Surface((60,60))
        self.image.fill((100,100,100))

        self.rect = self.image.get_rect()
        self.rect.centerx = lane
        self.rect.y = -120

    def update(self, speed):
        self.rect.y += speed
        if self.rect.top > HEIGHT:
            self.kill()


# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.value = random.choice([1,2,3])
        size = 20 + self.value * 5

        self.image = pygame.Surface((size,size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (size//2, size//2), size//2)

        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(LANE_X)
        self.rect.y = -60

    def update(self, speed):
        self.rect.y += speed
        if self.rect.top > HEIGHT:
            self.kill()


# ---------------- POWER UP ----------------
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.type = random.choice(["nitro", "shield", "repair"])

        self.image = pygame.Surface((40,40))

        if self.type == "nitro":
            self.image.fill((255,100,0))
        elif self.type == "shield":
            self.image.fill((0,200,255))
        else:
            self.image.fill((0,255,100))

        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(LANE_X)
        self.rect.y = -80

    def update(self, speed):
        self.rect.y += speed
        if self.rect.top > HEIGHT:
            self.kill()


# ---------------- ROAD ----------------
def draw_road(screen, offset):
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (ROAD_LEFT, 0), (ROAD_LEFT, HEIGHT), 4)
    pygame.draw.line(screen, BLACK, (ROAD_RIGHT, 0), (ROAD_RIGHT, HEIGHT), 4)

    dash = 40
    gap = 25

    y = -dash + offset
    while y < HEIGHT:
        pygame.draw.line(screen, GRAY, (ROAD_LEFT + LANE_WIDTH, y),
                         (ROAD_LEFT + LANE_WIDTH, y+dash), 5)
        pygame.draw.line(screen, GRAY, (ROAD_LEFT + 2*LANE_WIDTH, y),
                         (ROAD_LEFT + 2*LANE_WIDTH, y+dash), 5)
        y += dash + gap


# ---------------- GAME LOOP ----------------
def run_game(screen, settings):

    clock = pygame.time.Clock()

    base_speed = 6
    speed = base_speed

    # FIX: цвет машины
    color_map = {
        "red": RED,
        "blue": BLUE,
        "green": GREEN
    }

    player = Player(color_map.get(settings["car_color"], RED))

    traffic = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group(player)

    score = 0
    coins_collected = 0
    distance = 0
    dash_offset = 0

    active_power = None
    power_timer = 0

    font = pygame.font.SysFont("Arial", 24)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

        # FIX: мягкое ускорение
        speed = base_speed + distance * 0.003

        # SAFE SPAWN
        lanes = LANE_X.copy()
        player_lane = min(LANE_X, key=lambda x: abs(x - player.rect.centerx))
        if player_lane in lanes:
            lanes.remove(player_lane)

        if len(traffic) < 1 and random.random() < 0.02:
            t = Traffic(random.choice(lanes))
            traffic.add(t)
            all_sprites.add(t)

        if len(obstacles) < 1 and random.random() < 0.02:
            o = Obstacle(random.choice(lanes))
            obstacles.add(o)
            all_sprites.add(o)

        if random.random() < 0.02:
            c = Coin()
            coins.add(c)
            all_sprites.add(c)

        if len(powerups) < 1 and random.random() < 0.005:
            p = PowerUp()
            powerups.add(p)
            all_sprites.add(p)

        player.update()

        for g in [traffic, obstacles, coins, powerups]:
            for obj in g:
                obj.update(speed)

        distance += speed * 0.1

        # POWER LOGIC
        if active_power == "nitro":
            speed += 3
            power_timer -= 1
            if power_timer <= 0:
                active_power = None

        # COLLISION
        hit_t = pygame.sprite.spritecollide(player, traffic, False)
        hit_o = pygame.sprite.spritecollide(player, obstacles, False)

        if hit_t or hit_o:
            if active_power == "shield":
                for obj in hit_t + hit_o:
                    obj.kill()
                active_power = None
            else:
                return ("game_over", score, coins_collected, int(distance))

        # COINS
        for c in pygame.sprite.spritecollide(player, coins, True):
            coins_collected += c.value
            score += c.value * 5

        # POWERUPS
        for p in pygame.sprite.spritecollide(player, powerups, True):

            if p.type == "nitro":
                active_power = "nitro"
                power_timer = 180

            elif p.type == "shield":
                active_power = "shield"

            elif p.type == "repair":
                for obj in obstacles:
                    obj.kill()
                for obj in traffic:
                    obj.kill()

        score += 1
        dash_offset = (dash_offset + speed) % 65

        draw_road(screen, dash_offset)

        for s in all_sprites:
            screen.blit(s.image, s.rect)

        if active_power == "shield":
            pygame.draw.circle(screen, (0,200,255), player.rect.center, 50, 3)

        screen.blit(font.render(f"Score: {score}", True, BLACK), (10,10))
        screen.blit(font.render(f"Coins: {coins_collected}", True, BLACK), (10,35))
        screen.blit(font.render(f"Distance: {int(distance)}", True, BLACK), (10,60))

        if active_power:
            screen.blit(font.render(f"Power: {active_power}", True, BLACK), (10,85))

        pygame.display.flip()
        clock.tick(FPS)