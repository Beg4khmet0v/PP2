import os
import math
from datetime import datetime
import pygame


class MickeyClock:
    """Clock that shows current minutes and seconds."""

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        base_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(base_dir, "images")

        self.clock_face = pygame.image.load(
            os.path.join(images_dir, "clock_face.jpg")
        ).convert()

        self.face_width = 650
        self.face_height = 650
        self.clock_face = pygame.transform.smoothscale(
            self.clock_face, (self.face_width, self.face_height)
        )

        self.face_rect = self.clock_face.get_rect(
            center=(screen_width // 2, screen_height // 2)
        )

        # Real center of the clock dial inside the image
        self.center = (
            self.face_rect.left + 325,
            self.face_rect.top + 395
        )

        self.minute_length = 140
        self.second_length = 180

        self.minute_color = (0, 0, 0)
        self.second_color = (0, 0, 0)

        self.minute_width = 8
        self.second_width = 4

    def get_time_angles(self):
        """Return minute and second hand angles based on current system time."""
        now = datetime.now()

        seconds = now.second
        minutes = now.minute + seconds / 60

        minute_angle = minutes * 6
        second_angle = seconds * 6

        return minute_angle, second_angle

    def angle_to_position(self, angle, length):
        """
        Convert clock angle to screen position.
        0 degrees points to 12 o'clock.
        """
        rad = math.radians(angle - 90)
        x = self.center[0] + length * math.cos(rad)
        y = self.center[1] + length * math.sin(rad)
        return int(x), int(y)

    def draw_hand(self, screen, angle, length, color, width):
        """Draw one clock hand."""
        end_pos = self.angle_to_position(angle, length)
        pygame.draw.line(screen, color, self.center, end_pos, width)

    def draw(self, screen):
        """Draw the clock face and the hands."""
        screen.blit(self.clock_face, self.face_rect)

        minute_angle, second_angle = self.get_time_angles()

        self.draw_hand(
            screen,
            minute_angle,
            self.minute_length,
            self.minute_color,
            self.minute_width
        )

        self.draw_hand(
            screen,
            second_angle,
            self.second_length,
            self.second_color,
            self.second_width
        )

        pygame.draw.circle(screen, (0, 0, 0), self.center, 8)