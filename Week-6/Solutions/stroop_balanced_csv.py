from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_r, K_g, K_o, K_b
from copy import deepcopy
import csv
from helpers import *
from constants import *

""" Helper functions """
def run_trial(block_id, trial_id, trial_type, word, color, correct_key, **kwargs):
    stim = stims[word][color]
    
    present_for(exp, fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS_RGOB)
    correct = key == int(correct_key)
    
    if not correct: present_for(exp, feedback_incorrect, t=1000)

    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_id', 'trial_id', 'trial_type', 'word', 'color', 'RT', 'correct'])
control.set_develop_mode()
control.initialize(exp)

""" Counterbalancing """
subject_id = 1

with open("cb.csv") as f:
    reader = csv.DictReader(f)
    trials = [row for row in reader if row["subject_id"] == str(subject_id)]

""" Stimuli """
instr_start = make_instructions(INSTR_START); instr_start.preload()
instr_mid = make_instructions(INSTR_MID); instr_mid.preload()
instr_end = make_instructions(INSTR_END); instr_end.preload()

fixation = stimuli.FixCross(); fixation.preload()
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT); feedback_incorrect.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

""" Experiment """
control.start(subject_id=subject_id)

present_instructions(exp, instr_start)
for trial in trials:
    if trial["trial_id"] == 1 and trial["block_id"] != N_BLOCKS:
        present_instructions(exp, instr_mid)
    run_trial(**trial)
present_instructions(exp, instr_end)

control.end()