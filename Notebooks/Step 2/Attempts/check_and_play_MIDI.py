import pygame

def play_midi(midi_file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(midi_file_path)
        print("MIDI file loaded successfully.")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
    except pygame.error as e:
        print(f"Error: {e}")

    pygame.quit()

if __name__ == "__main__":
    midi_file_path = 'C:/Users/Enqi/Documents/GitHub/IS424/Notebooks/Step 2/Attempts/attempt5/attempt5.mid'  # Replace this with the path to your MIDI file

    try:
        play_midi(midi_file_path)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()  # Stop playback if interrupted by the user
