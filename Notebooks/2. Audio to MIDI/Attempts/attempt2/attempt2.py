#Example on how to use (written in CLI):
# python attempt2.py

import numpy as np
import aubio
from midiutil import MIDIFile
import librosa


# Load your acapella audio file
audio_file = 'C:/Users/Enqi/Documents/GitHub/IS424/Notebooks/Step 2/Attempts/attempt2/alto.wav'

# Find the sample rate
audio_data, sample_rate = librosa.load(audio_file, sr=None)

# Initialize the pitch detection
pitch_o = aubio.pitch("yin", 2048, 2048, sample_rate)
pitch_o.set_unit("midi")

# Create a MIDI file
mid = MIDIFile()

# Initialize time
time = 0

# Open the audio file
with open(audio_file, 'rb') as f:
    while True:
        # Read 2048 samples (bytes) from the audio file
        samples = f.read(2048)
        if not samples:
            break  # Break the loop if end of file is reached

        # Convert binary string to NumPy array of floats
        samples_float = np.frombuffer(samples, dtype=np.float32)

        # Ensure the input size is 2048 by zero-padding if necessary
        if len(samples_float) < 2048:
            samples_float = np.pad(samples_float, (0, 2048 - len(samples_float)), 'constant')

        # Perform pitch detection   
        pitch = pitch_o(samples_float)[0]
        if pitch > 0:
            # Adjust the velocity and duration as needed
            velocity = 64
            duration = 0.1  # You can adjust this based on your preference

            # Convert the pitch to a note number (MIDI note)
            note = int(pitch)

            # Add the note to the MIDI file
            mid.addNote(0, 0, note, time, duration, velocity)

        # Update the time position based on the number of samples read
        time += len(samples_float) / sample_rate

# Save the MIDI file
output_midi_file = 'attempt2.mid'
with open(output_midi_file, "wb") as output_file:
    mid.writeFile(output_file)


# corrupted midi file is created

