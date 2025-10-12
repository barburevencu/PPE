from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_SPACE, K_1, K_2, K_DOWN, K_UP, K_LEFT, K_RIGHT

KEYS = [K_1, K_2, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE]
ADJUST_RADIUS = 5
STEP_SIZE = 5

KEYMAP = {
    K_1: ("1", "radius", -ADJUST_RADIUS),
    K_2: ("2", "radius", +ADJUST_RADIUS),
    K_DOWN: ("down", "move", (0, -STEP_SIZE)),
    K_UP: ("up", "move", (0, +STEP_SIZE)),  
    K_LEFT: ("left", "move", (-STEP_SIZE, 0)),
    K_RIGHT: ("right", "move", (+STEP_SIZE, 0)),
}

INSTRUCTION_TEMPLATE = """
While looking at the cross with your {eye_closed} eye closed, adjust the circle's position (using your keyboard arrows) and size (1: make smaller, 2: make bigger) until you can no longer see it.\n
When the circle becomes invisible, press SPACE.\n
Press any key to begin.
"""

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)

exp.add_data_variable_names(['eye', 'keypress', 'radius', 'x_coord', 'y_coord'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_instructions(eye):
    eye_closed = "left" if eye == "right" else "right"
    instructions = stimuli.TextScreen(text=INSTRUCTION_TEMPLATE.format(eye_closed=eye_closed), text_justification=0, heading="Instructions")
    instructions.preload()
    return instructions

def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(eye, radius=75):

    make_instructions(eye).present(); exp.keyboard.wait()

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=([300, 0] if eye == "left" else [-300, 0]))
    fixation.preload()

    circle = make_circle(radius)

    while True:
        fixation.present(clear=True, update=False)
        circle.present(clear=False, update=True)
        
        key, _ = exp.keyboard.wait(KEYS)
        if key == K_SPACE:
            break
        
        keypress, action, change = KEYMAP.get(key)

        if action == "move":
            circle.move(change)
        else:
            radius = max(1, radius + change)
            circle = make_circle(radius, circle.position)

        x, y = circle.position
        exp.data.add([eye, keypress, radius, x, y])

control.start(subject_id=1)

for eye in ["right", "left"]:
    run_trial(eye)
    
control.end()