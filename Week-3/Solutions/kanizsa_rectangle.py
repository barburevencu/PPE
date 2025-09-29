from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_DARKGREY

""" GLOBAL SETTINGS """
exp = design.Experiment(name = "Kanizsa rectangle", background_colour = C_DARKGREY)
control.set_develop_mode()
control.initialize(exp)

""" CREATE STIMULI """
def kanizsa_rectangle(aspect_ratio=1.5, rectangle_scaling_factor=2, circle_scaling_factor=12):
    """
    Create a Kanizsa rectangle illusion. Returns the list of inducers and occluder.
    """
    screen_w, _ = exp.screen.size

    # RECTANGLE
    width = screen_w // rectangle_scaling_factor
    height = width // aspect_ratio
    rectangle = stimuli.Rectangle(size=(width, height), colour=C_DARKGREY, corner_anti_aliasing=10)

    half_width = width // 2
    half_height = height // 2

    # CIRCLES
    radius = screen_w // circle_scaling_factor
    edges = []
    colors = []

    for x in (-half_width, half_width):
        for y in (-half_height, half_height):  
            edges.append((x, y))
            colors.append(C_WHITE if y < 0 else C_BLACK)
    
    circles = [stimuli.Circle(radius=radius, position=edge, colour=color, anti_aliasing=10) for edge, color in zip(edges, colors)]

    return circles + [rectangle]

stim_list = kanizsa_rectangle(aspect_ratio=1, rectangle_scaling_factor=2, circle_scaling_factor=12)

""" RUN EXPERIMENT """

# DRAW
exp.screen.clear()
for stim in stim_list:
    stim.present(False, False)
exp.screen.update()

# WAIT
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()