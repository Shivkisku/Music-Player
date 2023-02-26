# Music-Player

The code defines a simple music player using the tkinter and pygame libraries in Python. The MusicPlayer class inherits from the tkinter Frame class and creates a GUI with three buttons for controlling music playback: Play, Pause, and Stop.

The Pygame mixer library is initialized in the constructor of the MusicPlayer class, which allows for loading and playing music files. When the Play button is clicked, the play_music method is called which loads and plays an MP3 file using Pygame mixer. The song_label label is updated to display the name of the currently playing song.

When the Pause button is clicked, the pause_music method is called which pauses the music playback. When the Stop button is clicked, the stop_music method is called which stops the music playback.

Finally, the code creates a Tkinter instance and the MusicPlayer class is instantiated as the main application, which runs until the user closes the window.
