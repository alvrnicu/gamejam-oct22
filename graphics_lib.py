from tkinter import *
import time

# This is just so we have a stub to pass as a default key press handler
def empty_func():
    pass


# Create an object holding global state instead of using global variables.
# We could equivalently just access a global canvas.
class CanvasHolder:
    def __init__(self, canvas):
        self.canvas = canvas
        self.running = True


gc = CanvasHolder(None)


# helper drawing functions - just thin wrappers around Tkinter's equivalents, with less functionality
def draw_oval(x1, y1, x2, y2, fill):
    gc.canvas.create_oval(x1, y1, x2, y2, fill=fill)


def draw_circle(x, y, r, fill):
    draw_oval(x - r, y - r, x + r, y + r, fill=fill)


def draw_rectangle(x1, y1, x2, y2, fill):
    gc.canvas.create_rectangle(x1, y1, x2, y2, fill=fill)


def draw_text(x, y, text, anchor=None, font=None):
    gc.canvas.create_text(x, y, text=text, anchor=anchor, font=font)


def start_graphics(
    render_fn,
    wait_time=0.01,
    window_width=500,
    window_height=400,
    window_title="Graphics",
    key_press=empty_func,
):
    """
    Main driver for the helper graphics library. Takes a render function, and continually runs it until the program
    is interrupted.

    The intended use is that the caller calls start_graphics() with a function that displays one frame of
    the graphic. That function can use any sort of app state it wants to control what is rendered - e.g.
    to animate a bouncing ball, you'd have a variable for the height of the ball that changes during
    render_fn so that next time it's called, the ball is in a different position.

    In addition, the user can write a function for handling keyboard input. That function should accept a single
    argument - the code of the key being pressed (for the A key, it's just "a"; for the left arrow, it's "Left") -
    and update app state accordingly. This function wraps Tkinter so that key presses are converted to the
    key code directly, instead of returning a Tkinter.Event -- this is done to keep things simplest for
    beginner students, but it sacrifices some flexibility and readability.

    @param render_fn: a function that displays one frame of the animation (or the sole frame for a static
        graphic). Should not take any parameters.
    @param wait_time: time in seconds between frames. Default of 100 FPS.
    @param window_width: width, in pixels(?) of the graphics window
    @param window_height: height, in pixels(?) of the graphics window
    @param window_title: displayed title of the graphics window
    @param key_press: optional function for handling keyboard input.
    """

    def handle_key_press(evt):
        return key_press(evt.keysym)

    def on_window_close():
        gc.running = False

    tk = Tk()
    tk.protocol("WM_DELETE_WINDOW", on_window_close)
    gc.canvas = Canvas(tk, width=window_width, height=window_height, bd=0, bg="papaya whip")
    gc.canvas.pack()
    gc.canvas.bind_all("<KeyPress>", handle_key_press)

    while gc.running:
        gc.canvas.delete("all")
        render_fn()
        tk.update_idletasks()
        tk.update()
        time.sleep(wait_time)
