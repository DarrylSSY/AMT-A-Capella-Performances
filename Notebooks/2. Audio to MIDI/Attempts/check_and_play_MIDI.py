# checks if a file is a MIDI file and plays it if it is


import pygame
import mimetypes
import os

# def is_midi_file(file_path):
#     mime, _ = mimetypes.guess_type(file_path)
#     return mime == 'audio/midi'

def is_midi_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in ('.mid', '.midi')


def play_midi(midi_file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        if is_midi_file(midi_file_path):
            pygame.mixer.music.load(midi_file_path)
            print("MIDI file loaded successfully.")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
        else:
            print("Not a valid MIDI file. Cannot play.")
    except pygame.error as e:
        print(f"Error: {e}")

    pygame.quit()

if __name__ == "__main__":
    midi_file_path = 'C:/Users/Enqi/Documents/GitHub/IS424/Notebooks/Step 2/Attempts/attempt5/attempt5.mid'  # Replace this with the path to your MIDI file

    try:
        play_midi(midi_file_path)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()  # Stop playback if interrupted by the user
