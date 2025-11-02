from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import random

""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ["match", "mismatch"]
COLORS = ["red", "green", "blue", "orange"]

N_BLOCKS = 2
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do, F if they don't.\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """WELL DONE!"""
FEEDBACK_INCORRECT = """OOPS, THAT WAS INCORRECT!"""

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    correct = key == K_j if trial_type == "match" else key == K_f
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_id', 'trial_id', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} 
                 for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])
print(stims)

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
control.start(subject_id=9)

present_instructions(INSTR_START)
for block in range(1, N_BLOCKS + 1):
    for trial in range(1, N_TRIALS_IN_BLOCK + 1):
        trial_type = random.choice(TRIAL_TYPES)
        word = random.choice(COLORS)
        color = word if trial_type == "match" else random.choice([c for c in COLORS if c != word])
        run_trial(block, trial, trial_type, word, color)
    if block != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)

control.end()