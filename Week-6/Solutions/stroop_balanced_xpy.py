from expyriment import control, design, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE, K_b, K_g, K_o, K_r

from helpers import *
from constants import *

""" Run trial function """
def run_trial(block_id, trial_id, trial):
    trial_type, word, color, correct_key = (
        trial.factor_dict[k] for k in ("trial_type", "word", "color", "correct_key")
    )

    present_for(exp, fixation, t=500)
    trial.stimuli[0].present()
    key, rt = exp.keyboard.wait(KEYS_RGOB)
    correct = key == correct_key
    if not correct: present_for(exp, feedback_incorrect, t=1000)
    exp.data.add([block_id, trial_id, trial_type, word, color, key, rt, correct])

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_id', 'trial_id', 'trial_type', 'word', 'color', 'key', 'RT', 'correct'])
exp.add_bws_factor("assignment", derangements(COLORS))

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
instr_start = make_instructions(INSTR_START); instr_start.preload()
instr_mid = make_instructions(INSTR_MID); instr_mid.preload()
instr_end = make_instructions(INSTR_END); instr_end.preload()

fixation = stimuli.FixCross(); fixation.preload()
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT); feedback_incorrect.preload()

""" Counterbalancing """
subject_id = 1
COLOR_CROSSINGS = exp.get_permuted_bws_factor_condition("assignment", subject_id)
dict_colors = dict(zip(COLORS, COLOR_CROSSINGS))

""" Design """
for block_id in range(1, N_BLOCKS + 1):
    block = design.Block(f"Block {block_id}")
    for _ in range(2):
        block.add_trials_full_factorial(FACTORS)
    block.shuffle_trials(method=0, max_repetitions=None, n_segments=2)
    
    for trial in block.trials:
        trial_type = trial.get_factor("trial_type")
        word = trial.get_factor("word")

        color = word if trial_type == "match" else dict_colors[word]
        trial.set_factor("color", color)
        trial.set_factor("correct_key", ord(color[0]))

        trial.add_stimulus(stimuli.TextLine(word, text_colour=color))
        trial.preload_stimuli()
    
    exp.add_block(block)

""" Experiment """
control.start(subject_id=subject_id)

instr_start.present()
exp.keyboard.wait()

for block_id, block in enumerate(exp.blocks, 1):
    for trial_id, trial in enumerate(block.trials, 1):
        run_trial(block_id, trial_id, trial)
    if block_id != N_BLOCKS:
        instr_mid.present()
        exp.keyboard.wait()

instr_end.present()
exp.keyboard.wait()

control.end()