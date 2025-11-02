from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
from copy import deepcopy
import random
from helpers import *
from constants import *

def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(exp, fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS_FJ)
    correct = key == K_j if trial_type == "match" else key == K_f
    
    if not correct: present_for(exp, feedback_incorrect, t=1000)

    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_id', 'trial_id', 'trial_type', 'word', 'color', 'RT', 'correct'])

""" Counterbalancing """
subject_id = 1
ders = derangements(COLORS)
mismatch = ders[(subject_id - 1) % len(ders)]

base = (
    [{"trial_type": "match", "word": c, "color": c} for c in COLORS] +
    [{"trial_type": "mismatch", "word": w, "color": c} for w, c in zip(COLORS, mismatch)]
)

block_repetitions = N_TRIALS_IN_BLOCK // len(base)
blocks = []

for block_id in range(1, N_BLOCKS + 1):
    block_trials = base * block_repetitions
    random.shuffle(block_trials)
    trials = [{"block_id": block_id, "trial_id": i, **t} for i, t in enumerate(block_trials, 1)]
    blocks.append(trials)

control.set_develop_mode()
control.initialize(exp)

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
for i, block in enumerate(blocks, 1):
    for trial in block:
        run_trial(**trial)
    if i != N_BLOCKS:
        present_instructions(exp, instr_mid)
present_instructions(exp, instr_end)

control.end()