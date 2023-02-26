import tkinter as tk
import pygame.mixer

class MusicPlayer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create buttons for controlling music playback
        self.play_button = tk.Button(self, text="Play", command=self.play_music)
        self.play_button.pack(side="left")

        self.pause_button = tk.Button(self, text="Pause", command=self.pause_music)
        self.pause_button.pack(side="left")

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_music)
        self.stop_button.pack(side="left")

        # Create label for displaying current song
        self.song_label = tk.Label(self, text="No song selected.")
        self.song_label.pack(side="bottom")

    def play_music(self):
        # Load and play music file
        pygame.mixer.music.load("path/to/music/file.mp3")
        pygame.mixer.music.play()

        # Update label with current song
        self.song_label.configure(text="Now playing: file.mp3")

    def pause_music(self):
        # Pause music playback
        pygame.mixer.music.pause()

    def stop_music(self):
        # Stop music playback
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(master=root)
    app.mainloop()
