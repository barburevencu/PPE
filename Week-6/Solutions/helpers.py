from itertools import permutations
from expyriment import stimuli

""" Helper functions """
def derangements(values):
    """Return permutations where no element remains in its original position."""
    return [perm for perm in permutations(values) if all(a != b for a, b in zip(values, perm))]

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(exp, *stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(exp, *stims, t=1000):
    dt = timed_draw(exp, *stims)
    exp.clock.wait(t - dt)

def make_instructions(text):
    return stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")

def present_instructions(exp, instructions):
    instructions.present()
    exp.keyboard.wait()