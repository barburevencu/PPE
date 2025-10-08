from expyriment import design, control, stimuli
import random
import math

FPS  = 60
MSPF = 1000 / FPS # ms per frame

def to_frames(t):
    return math.ceil(t / MSPF)

def to_time(num_frames):
    return num_frames * MSPF

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(exp, stims):
    t0 = exp.clock.time # Initial time

    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    
    elapsed = exp.clock.time - t0 # Time it took to execute and present drawn stims
    return elapsed

def present_for(exp, stims, num_frames):
    if num_frames == 0:
        return

    dt = timed_draw(exp, stims)
    if dt > 0:
        t = to_time(num_frames)
        exp.clock.wait(t - dt)


if __name__ == "__main__":
    exp = design.Experiment()

    control.set_develop_mode()
    control.initialize(exp)

    fixation = stimuli.FixCross()

    n_squares = 20
    positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n_squares)]
    squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
    load([fixation] + squares)

    durations = []
    t0 = exp.clock.time

    for square in squares:
        if not square.is_preloaded:
            print("Preloading function not implemented correctly.")

        stims = [fixation, square] 
        present_for(exp, stims, num_frames=30)
        t1 = exp.clock.time
        durations.append(t1 - t0)
        t0 = t1

    if all(abs(d - 500) <= 1 for d in durations):
        print("Well done!")
    else:
        print(f"Timing off. Measured durations were: {durations}")

    control.end()