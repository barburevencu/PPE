# Session 5: Expyriment keyboard input and data collection

## Table of Contents
- [Exercise 1: Find your blind spot](#exercise-1-blind-spot)
- [Exercise 2: Recording data](#exercise-2-recording-data)

## Exercise 1: Blind spot
Open `blindspot.py` and modify it as follows:

1. The position and size of the circle must be adjustable (position should be adjusted via keyboard arrows, and size via number keys: 1 = smaller, 2 = larger)
2. Add instructions at the beginning of each trial: `stimuli.TextScreen` (which eye to cover, where to fixate, how to adjust the circle, what to do when they’re done—press space to move on)
3. Modify run_trial so it takes a side as input (left or right) and runs the procedure for the left or right eye of the subject

The program should guide the participant toward finding their retinal blind spot. Have a look [here](https://www.youtube.com/watch?v=pJPHFTa5Las) for inspiration.

## Exercise 2: Recording data
### Exercise 2A: Minimal version
Modify `blindspot.py` to collect the following data **on each trial**:

- the eye whose blind spot was located
- the final radius of the circle, as set by the participant
- the final coordinates of the circle (separate columns for horizontal and vertical), as set by the participant

### Exercise 2B: Full version
Modify `blindspot.py` to collect the following data **on each key press**:

- trial type: the eye whose blind spot is being located
- last key pressed
- the current radius of the circle
- the current coordinates of the circle