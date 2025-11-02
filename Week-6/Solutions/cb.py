from itertools import permutations
from copy import deepcopy
import random, csv

def derangements(lst):
    """Returns permutations (of lst) where no element remains in its original position as a list."""
    ders = []
    for perm in permutations(lst):
        if all(original != perm[idx] for idx, original in enumerate(lst)):
            ders.append(perm)
    return ders

def subject_trials(subject_id):
    mismatch = MISMATCHES[(subject_id - 1) % len(MISMATCHES)]

    base = [{"word": w, "color": w} for w in COLORS] + [{"word": w, "color": c} for w, c in zip(COLORS, mismatch)]
    block_reps = N_TRIALS_IN_BLOCK // len(base)

    trials = []
    for b_index in range(1, N_BLOCKS + 1):
        block = base * block_reps 
        random.shuffle(block)
        
        for t_index, trial in enumerate(block, 1):
            trials.append({
                "subject_id": subject_id,
                "block_cnt": b_index,
                "trial_cnt": t_index,
                "trial_type": "match" if trial["word"] == trial["color"] else "mismatch",
                "word": trial["word"],
                "color": trial["color"],
                "correct_key": ord(trial["color"][0])
            })

    return trials

N_SUBJECTS = 90
N_BLOCKS = 2
N_TRIALS_IN_BLOCK = 16
COLORS = ["red", "green", "blue", "orange"]
MISMATCHES = derangements(COLORS)

all_trials = [trial for id in range(1, N_SUBJECTS + 1) for trial in subject_trials(id)]

cols = ["subject_id", "block_cnt", "trial_cnt", "trial_type", "word", "color", "correct_key"]
with open("cb.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(all_trials)