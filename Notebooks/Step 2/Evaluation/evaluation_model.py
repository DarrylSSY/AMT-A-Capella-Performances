
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

    # Placeholder for frame and note evaluation metrics
    frame_eval = 0  # Replace this with your frame evaluation logic
    note_eval = 0  # Replace this with your note evaluation logic

    return onset_evaluation, frame_eval, note_eval

# Paths to the generated and ground truth MIDI files
generated_midi_file = "C:/Users/Enqi/Documents/GitHub/IS424/Notebooks/Step 2/working_code/audio/omg.mid"
ground_truth_midi_file = "C:/Users/Enqi/Documents/GitHub/IS424/Notebooks/Step 2/working_code/audio/output.mid"

# Evaluate the model
onset_eval, frame_eval, note_eval = evaluate_midi(generated_midi_file, ground_truth_midi_file)

# Print the evaluation results
print("Onset Evaluation:", onset_eval)
print("Frame Evaluation:", frame_eval)  # Print frame evaluation result
print("Note Evaluation:", note_eval)    # Print note evaluation result

# results below
# Onset Evaluation: OrderedDict([('F-measure', 0.21971830985915491), ('Precision', 0.195), ('Recall', 0.25161290322580643)])
# Frame Evaluation: 0
# Note Evaluation: 0

# ground_truth is converted by FL Studio

