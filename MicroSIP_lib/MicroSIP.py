from pyautogui import *
from pygetwindow import *

class Microsip:
    def __init__(self):
        self.program: Win32Window = getWindowsWithTitle("MicroSIP")[0]

    def get_size(self):
        return (self.program.size.width, self.program.size.height)

    def get_position(self):
        return (self.program.top, self.program.left)

    def move_mouse(self, x: int, y: int, duration: float = 0.0, mouse_click: bool = False):
        moveTo(x, y, duration=duration)

        if mouse_click:
            click()

        return self

    def focus(self):
        if self.program == None: return

        self.program.activate()
        self.program.show()

    def locate(self, image: str):
        return locateOnScreen(image)