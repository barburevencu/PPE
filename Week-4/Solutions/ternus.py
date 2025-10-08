from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED, C_GREEN, C_BLUE, C_YELLOW, K_SPACE
from drawing_functions import load, present_for

ALIAS = 10
RADIUS = 50; DISTANCE = RADIUS * 3; SPREAD = RADIUS * 9
TAG_COLORS = [C_YELLOW, C_RED, C_BLUE]

def make_circles():
    positions = range(-SPREAD // 2, SPREAD // 2, DISTANCE)
    return [stimuli.Circle(radius=RADIUS, position=(x_pos, 0), anti_aliasing=ALIAS) for x_pos in positions]

def add_tags(circles, tag_radius):
    tag_circles = [stimuli.Circle(radius=tag_radius, colour=col, anti_aliasing=ALIAS) for col in TAG_COLORS]
    for circle, tag in zip(circles, tag_circles):
        tag.plot(circle)

def run_trial(circle_frames=12, ISI=0, tags=False):
    circles = make_circles()
    if tags:
        add_tags(circles, tag_radius=RADIUS // 5)
    load(circles)

    while True:
        for dx in (SPREAD, -SPREAD):
            present_for(exp, circles, num_frames=circle_frames)
            present_for(exp, [], num_frames=ISI)
            circles[0].move((dx, 0))

        if exp.keyboard.check(K_SPACE):
            break

exp = design.Experiment(name="Ternus", background_colour=C_WHITE, foreground_colour=C_BLACK)

control.set_develop_mode()
control.initialize(exp)
control.start(subject_id=1)

trials = [{'ISI': 0}, {'ISI': 18}, {'ISI': 18, 'tags': True}]

for trial_params in trials:
    run_trial(**trial_params)

control.end()