# ground_truth is converted by FL Studio

import pretty_midi
import mir_eval

# Define a function to compute evaluation metrics
def evaluate_midi(wav_to_midi_file, ground_truth_midi_file):
    # Load the generated MIDI file
    generated_midi = pretty_midi.PrettyMIDI(wav_to_midi_file)

    # Load the ground truth MIDI file
    ground_truth_midi = pretty_midi.PrettyMIDI(ground_truth_midi_file)

    # Extract onset times from the generated and ground truth MIDI files
    generated_onsets = generated_midi.get_onsets()
    ground_truth_onsets = ground_truth_midi.get_onsets()

    # Calculate onset evaluation metrics
    onset_evaluation = mir_eval.onset.evaluate(ground_truth_onsets, generated_onsets)

    # Extract estimated pitch and corresponding times from generated MIDI file
    generated_est_times = []
    generated_est_freqs = []
    for instrument in generated_midi.instruments:
        for note in instrument.notes:
            generated_est_times.append(note.start)
            generated_est_freqs.append(note.pitch)

    # Extract ground truth pitch and corresponding times from ground truth MIDI file
    ground_truth_est_times = []
    ground_truth_est_freqs = []
    for instrument in ground_truth_midi.instruments:
        for note in instrument.notes:
            ground_truth_est_times.append(note.start)
            ground_truth_est_freqs.append(note.pitch)

    # Calculate pitch evaluation metrics
    pitch_evaluation = mir_eval.melody.evaluate(
        ground_truth_est_times, ground_truth_est_freqs,
        generated_est_times, generated_est_freqs)

    return onset_evaluation, pitch_evaluation

# Paths to the generated and ground truth MIDI files
generated_midi_file = "C:/Users/Enqi/Documents/GitHub/IS424/Notebooks/Step 2/Evaluation/attempt5.mid"
ground_truth_midi_file = "C:/Users/Enqi/Documents/GitHub/IS424/Notebooks/Step 2/Evaluation/ground_truth.mid"

# Evaluate the model
onset_eval, pitch_eval = evaluate_midi(generated_midi_file, ground_truth_midi_file)

# Print the evaluation results
print("Onset Evaluation:", onset_eval)
print("Pitch Evaluation:", pitch_eval)

