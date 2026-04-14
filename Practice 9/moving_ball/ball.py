import pygame


class Ball:
    """A red ball that moves inside the screen boundaries."""

    def __init__(self, x, y, radius, screen_width, screen_height, step=20):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.step = step
        self.color = (255, 0, 0)  # Red

    def move_up(self):
        """Move the ball up if it stays inside the screen."""
        new_y = self.y - self.step
        if new_y - self.radius >= 0:
            self.y = new_y

    def move_down(self):
        """Move the ball down if it stays inside the screen."""
        new_y = self.y + self.step
        if new_y + self.radius <= self.screen_height:
            self.y = new_y

    def move_left(self):
        """Move the ball left if it stays inside the screen."""
        new_x = self.x - self.step
        if new_x - self.radius >= 0:
            self.x = new_x

    def move_right(self):
        """Move the ball right if it stays inside the screen."""
        new_x = self.x + self.step
        if new_x + self.radius <= self.screen_width:
            self.x = new_x

    def draw(self, screen):
        """Draw the ball on the given screen."""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)