import os
import pygame
from player import MusicPlayer


# Window settings
WIDTH = 800
HEIGHT = 400
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 215, 0)
FPS = 60


def load_music_files(folder_path):
    """Load all supported audio files from the given folder."""
    supported_formats = (".wav", ".mp3")
    tracks = []

    if not os.path.exists(folder_path):
        return tracks

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(supported_formats):
            full_path = os.path.join(folder_path, file_name)
            tracks.append(full_path)

    tracks.sort()
    return tracks


def draw_text(screen, font, text, color, x, y):
    """Render text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()

    font_title = pygame.font.SysFont("arial", 36)
    font_main = pygame.font.SysFont("arial", 28)
    font_small = pygame.font.SysFont("arial", 22)

    # Absolute path based on the location of this file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    music_folder = os.path.join(base_dir, "music", "sample_tracks")

    tracks = load_music_files(music_folder)

    if not tracks:
        print("No music files found in music/sample_tracks/")
        pygame.quit()
        return

    player = MusicPlayer(tracks)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()
                elif event.key == pygame.K_q:
                    running = False

        screen.fill(BACKGROUND_COLOR)

        draw_text(screen, font_title, "Music Player", HIGHLIGHT_COLOR, 280, 30)
        draw_text(screen, font_main, f"Current track: {player.get_current_track_name()}", TEXT_COLOR, 80, 110)
        draw_text(screen, font_main, f"Status: {player.get_status()}", TEXT_COLOR, 80, 160)
        draw_text(screen, font_main, f"Playlist position: {player.get_playlist_position()}", TEXT_COLOR, 80, 210)

        draw_text(screen, font_small, "Controls:", HIGHLIGHT_COLOR, 80, 280)
        draw_text(screen, font_small, "P = Play", TEXT_COLOR, 80, 315)
        draw_text(screen, font_small, "S = Stop", TEXT_COLOR, 200, 315)
        draw_text(screen, font_small, "N = Next", TEXT_COLOR, 320, 315)
        draw_text(screen, font_small, "B = Previous", TEXT_COLOR, 430, 315)
        draw_text(screen, font_small, "Q = Quit", TEXT_COLOR, 610, 315)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    main()