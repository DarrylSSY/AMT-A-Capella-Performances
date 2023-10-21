import aubio
from midiutil import MIDIFile

# Load your acapella audio file
audio_file = 'path_to_acapella.wav'

# Initialize the pitch detection
pitch_o = aubio.pitch("yin", 2048, 2048, 44100)
pitch_o.set_unit("midi")

# Create a MIDI file
mid = MIDIFile()

# Open the audio file
with open(audio_file, 'rb') as f:
    time = 0
    while True:
        samples, read = f.read(2048), 2048
        pitch = pitch_o(samples)[0]
        if pitch > 0:
            # Adjust the velocity and duration as needed
            velocity = 64
            duration = 0.1  # You can adjust this based on your preference

            # Convert the pitch to a note number (MIDI note)
            note = int(pitch)

            # Add the note to the MIDI file
            mid.addNote(0, 0, note, time, duration, velocity)

        time += read / 44100  # Update the time position

# Save the MIDI file
output_midi_file = 'output.mid'
with open(output_midi_file, "wb") as output_file:
    mid.writeFile(output_file)
