# Session 3: Expyriment stimuli (what, how, where)

## Table of Contents
- [Exercise 1: Double buffer illustration](#exercise-1-double-buffer)
- [Exercise 2: Timing puzzle](#exercise-2-timing-puzzle)
- [Exercise 3: Drawing functions](#exercise-3-drawing-functions)
- [Exercise 4: Ternus illusion](#exercise-4-ternus-illusion)

## Exercise 1: Double buffer
Run `square_fixation.py`. The script should plot a fixation inside an empty square but it does something differently. Try to understand why it does not work, then fix it.

## Exercise 2: Timing puzzle
Have a look at `timing_puzzle.py` and try to predict what will happen. For how long will the fixation cross stay on-screen? Run the script to find out. After figuring out why it does not work, fix it such that the fixation cross is displayed for one second.

## Exercise 3: Drawing functions
Open `drawing_functions.py` and implement the following functions:

1. `load`: preload the stimuli passed as input
2. `timed_draw`: draw a list of (preloaded) stimuli on-screen, return the time it took to execute the drawing
3. `present_for`: draw and keep stimuli on-screen for time *t* in ms (be mindful of edge cases!)

Once you've implemented all three functions, run `drawing_functions.py`. If you implemented the functions correctly, the program will print "Well done!". Otherwise, it will show you the measured durations.

## Exercise 4: Ternus illusion
Write a `ternus.py` program that generates a [Ternus display](https://en.wikipedia.org/wiki/Ternus_illusion) similar to the program embedded [here](https://michaelbach.de/ot/mot-Ternus/). The `run_trial` function should have parameters for **circle radius**, **inter-stimulus interval** (ISI), and for whether to add **color tags** to the circles.

When run, the program should present three Ternus displays in succession:

1. Element motion without color tags (low ISI)
2. Group motion without color tags (high ISI)
3. Element motion with color tags (high ISI)

**Make sure it works on yourself!** Note that with some ISIs, you will get bistable perception—try squinting or fixating at the central circles to flip interpretation. 

**Don't forget to preserve the structure of expyriment scripts**: Global settings $\rightarrow$ Stimuli generation $\rightarrow$ Trial run

**Write functions**: `present_for`, `make_circles`, `add_tags`

**Aim for compact code (80–90 lines)**

**Hints**:
- In the loop for the display (e.g., `while True`, add a command that checks for user input and exits the loop if SPACE was pressed):
```python
from expyriment.misc.constants import K_SPACE # top of script
if exp.keyboard.check(K_SPACE): # inside the loop
    break
```

- Pay attention to how you implement ISI = 0
- Since a frame is 16.67 ms, it's best to use frames instead of times. Have the `present_for` function **take as input the number of frames** and convert to time in milliseconds internally. This will help you avoid rounding errors or passing in meaningless commands (such as present for 12 milliseconds).
- As we’ve seen with canvases, `expyriment` lets you plot stimuli onto the surface of other stimuli. You can add tags by plotting small circles on the surface of the big ones, but be mindful of two aspects:
    -  The big circles must be preloaded after the plotting of the tags
    - The positions of the tags must be set relative to the circles on top of which they’re plotted (easier than it sounds)