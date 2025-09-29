from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED
control.set_develop_mode()

""" HELPER FUNCTIONS """
def create_grid(n_rows, n_cols, size, color, space, max_width, max_height):
    W = n_cols * size + (n_cols - 1) * space
    H = n_rows * size + (n_rows - 1) * space

    # Check current configuration fits
    if W > max_width or H > max_height:
        raise ValueError("The target grid does not on fit the screen")

    squares = []

    for row in range(n_rows):
        for col in range(n_cols):
            ## Compute position and correct for offset from expy coords
            pos_x = col * (size + space) - (W - size) // 2 
            pos_y = row * (size + space) - (H - size) // 2 
            squares.append(
                stimuli.Rectangle(
                    size=(size, size), 
                    position=(pos_x, pos_y), 
                    colour=color, 
                    corner_anti_aliasing=10)
                )
    
    return squares

def run_trial(squares, background_color):
    exp.screen.colour = background_color
    exp.screen.clear()
    for square in squares:
        square.present(False, False)
    exp.screen.update()
    exp.keyboard.wait()


""" GLOBAL SETTINGS """
exp = design.Experiment(name="Kanizsa rectangle")
control.initialize(exp)

# Grid parameters
n_rows, n_cols = 10, 12
size = 50
space = 10
color = C_BLACK
background_color = C_WHITE
max_width, max_height = exp.screen.size

""" CREATE STIMULI """
squares = create_grid(n_rows, n_cols, size, color, space, max_width, max_height)

""" RUN EXPERIMENT """
run_trial(squares, background_color)

# End the current session and quit expyriment
control.end()