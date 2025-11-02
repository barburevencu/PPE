from expyriment.misc.constants import K_f, K_j, K_b, K_g, K_o, K_r

KEYS_FJ = [K_f, K_j]
KEYS_RGOB = [K_r, K_g, K_o, K_b]
TRIAL_TYPES = ["match", "mismatch"]
COLORS = ["red", "green", "blue", "orange"]
FACTORS = {"trial_type": TRIAL_TYPES, "word": COLORS}
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