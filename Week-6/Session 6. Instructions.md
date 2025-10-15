# Session 5: Expyriment keyboard input and data collection

## Table of Contents
- [Exercise 1: Simple Stroop](#exercise-1-simple-stroop)
- [Exercise 2: Balanced Stroop](#exercise-2-balanced-stroop)

## Exercise 1: Simple Stroop
Open `stroop.py` and modify it as follows:

- participants' task is to decide via their keyboard whether word meaning and text color match (colors: red, blue, green, orange)
- at the end of each trial, participants should receive feedback depending on the accuracy of their choice
- for each trial, randomly choose a trial type (match/mismatch), one color word and one color for the font: use Python's [random](https://docs.python.org/3/library/random.html) or [expyriment.design.randomize](https://docs.expyriment.org/expyriment.design.randomize.html) modules
- there should be 32 trials in total, equally divided into 2 blocks

## Exercise 2: Balanced Stroop
Create a new script, stroop_balanced.py, that modifies stroop.py as follows:
- have participants decide the color the onscreen word is written in
- using the method you think is best, balance the design
- extend the Stroop to 128 trials in total, divided into 8 equally-sized blocks