#Example on how to use (written in CLI):
#python wav2midi_v1.py "./audio/alto.wav" output.mid

import sys
from aubio import source, notes
from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo

if len(sys.argv) < 3:
    print("Usage: %s <filename> <output> [samplerate]" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
midioutput = sys.argv[2]

downsample = 1
samplerate = 48000 // downsample
if len(sys.argv) > 3:
    samplerate = int(sys.argv[3])

win_s = 4096 // downsample
hop_s = 512 // downsample
tolerance = 0.3

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

notes_o = notes("default", win_s, hop_s, samplerate)

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

ticks_per_beat = mid.ticks_per_beat
bpm = 120
tempo = bpm2tempo(bpm)

tempo_message = MetaMessage('set_tempo', tempo=tempo)
track.append(tempo_message)

last_note = None
total_frames = 0

while True:
    samples, read = s()
    new_note = notes_o(samples)[0]
    if new_note != 0 and new_note != last_note:
        seconds = total_frames / float(samplerate)
        ticks = int(seconds * ticks_per_beat * bpm / 60)
        delta_ticks = max(0, ticks - sum(event.time for event in track))
        
        if last_note is not None:
            track.append(Message('note_off', note=int(last_note), velocity=0, time=int(delta_ticks)))
        track.append(Message('note_on', note=int(new_note), velocity=64, time=int(delta_ticks)))
        last_note = new_note

    total_frames += read
    if read < hop_s:
        break

if last_note is not None:
    seconds = total_frames / float(samplerate)
    ticks = int(seconds * ticks_per_beat * bpm / 60)
    delta_ticks = max(0, ticks - sum(event.time for event in track))
    track.append(Message('note_off', note=int(last_note), velocity=0, time=int(delta_ticks)))

mid.save(midioutput)
