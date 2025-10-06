from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

#control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")
fixation.preload()
text.preload()

t0 = exp.clock.time
fixation.present()
t1 = exp.clock.time
dt = t1-t0

exp.clock.wait(1000 - dt)

text.present()
t2 = exp.clock.time

exp.clock.wait(1000 - dt)

duration = (t2 - t1)/1000
units = "second" if duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.keyboard.wait(2000)

control.end()