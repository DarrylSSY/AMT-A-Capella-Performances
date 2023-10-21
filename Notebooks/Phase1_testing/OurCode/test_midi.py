import pygame
import mimetypes

def is_midi_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type in ("audio/midi", "audio/x-midi")

def play_midi(midi_file_path):
    if not is_midi_file(midi_file_path):
        print("Error: Not a valid MIDI file.")
        return

    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(midi_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
    except pygame.error:
        print("Error: Could not load or play the MIDI file.")

    pygame.quit()

if __name__ == "__main__":
    midi_file_path = 'NGGYU.mid'  # Replace with the path to your MIDI file

    if is_midi_file(midi_file_path):
        play_midi(midi_file_path)
    else:
        print("Error: Not a valid MIDI file.")
