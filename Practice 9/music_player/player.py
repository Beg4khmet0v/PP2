import os
import pygame


class MusicPlayer:
    """A simple music player using pygame.mixer.music."""

    def __init__(self, tracks):
        self.tracks = tracks
        self.current_index = 0
        self.is_playing = False

        if not self.tracks:
            raise ValueError("Playlist is empty. Add audio files to sample_tracks folder.")

        self.load_track()

    def load_track(self):
        """Load the current track into the mixer."""
        pygame.mixer.music.load(self.tracks[self.current_index])

    def play(self):
        """Play the current track."""
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        """Stop playback."""
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        """Switch to the next track and play it."""
        self.current_index = (self.current_index + 1) % len(self.tracks)
        self.load_track()
        self.play()

    def previous_track(self):
        """Switch to the previous track and play it."""
        self.current_index = (self.current_index - 1) % len(self.tracks)
        self.load_track()
        self.play()

    def get_current_track_name(self):
        """Return only the file name of the current track."""
        return os.path.basename(self.tracks[self.current_index])

    def get_playlist_position(self):
        """Return current track position as text."""
        return f"Track {self.current_index + 1} of {len(self.tracks)}"

    def get_status(self):
        """Return current playback status."""
        return "Playing" if self.is_playing else "Stopped"